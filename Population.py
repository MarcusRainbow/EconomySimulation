import random
import math
from typing import Callable, Tuple, List
import matplotlib.pyplot as plt 

def simulation(
    simulations: int, 
    draws: int,
    population: int, 
    game: Callable[[float, float, bool], Tuple[float, float]]) -> Tuple[List[float], List[float]]:

    total = [0.0] * population
    total_2 = [0.0] * population
    for _ in range(simulations):
        amount = [100.0] * population
        for _ in range(draws):
            first = random.randrange(0, population)
            second = random.randrange(0, population)
            choice = bool(random.getrandbits(1))
            amount[first], amount[second] = game(amount[first], amount[second], choice)

        amount.sort()
        for i in range(population):
            a = amount[i]
            total[i] = total[i] + a
            total_2[i] = total_2[i] + a * a
    
    n = float(simulations)
    mean = [0.0] * population
    stdev = [0.0] * population
    for i in range(population):
        t = total[i]
        mean[i] = t / n
        stdev[i] = math.sqrt((total_2[i] - t * t / n ) / (n - 1))
    return mean, stdev

def arithmetic_game(prev1: float, prev2: float, draw: bool) -> Tuple[float, float]:
    WIN = 20
    if draw:
        return prev1 + WIN, prev2 - WIN
    else:
        return prev1 - WIN, prev2 + WIN

def geometric_game(prev1: float, prev2: float, draw: bool) -> Tuple[float, float]:
    WIN = 0.2
    smallest = min(prev1, prev2)
    win = WIN * smallest
    if draw:
        return prev1 + win, prev2 - win
    else:
        return prev1 - win, prev2 + win

def graph(points: List[float], axis: str):
    x = range(len(points))
    plt.plot(x, points) 
    #plt.xlabel('x - axis') 
    plt.ylabel(axis)
    #plt.title(title)
    #plt.show(block = False) 

def test_simulate_arithmetic() -> List[float]:
    SIMULATIONS = 10000
    DRAWS = 10000
    POPULATION = 100
    mean, stdev = simulation(SIMULATIONS, DRAWS, POPULATION, arithmetic_game)
    #print(f"test_simulate_arithmetic: mean={mean} stdev={stdev}")
    graph(mean, "test_simulate_arithmetic: means")

def test_simulate_geometric():
    SIMULATIONS = 10000
    DRAWS = 10000
    POPULATION = 100
    mean, stdev = simulation(SIMULATIONS, DRAWS, POPULATION, geometric_game)
    #print(f"test_simulate_geometric: mean={mean} stdev={stdev}")
    graph(mean, "test_simulate_geometric: means")

if __name__ == "__main__":
    test_simulate_arithmetic()
    test_simulate_geometric()
    plt.show()

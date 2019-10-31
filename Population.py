import random
import math
import numpy as np
from typing import Callable, Tuple, List
import matplotlib.pyplot as plt 

def simulation(
    simulations: int, 
    draws: int,
    population: int, 
    game: Callable) -> Tuple[List[float], List[float]]:

    # run the simulations
    amount = np.full((simulations, population), 100.0)
    rows = np.arange(simulations)
    for _ in range(draws):
        winners = np.random.randint(population, size=simulations)
        losers = np.random.randint(population, size=simulations)
        game(amount, rows, winners, losers)

    # sort each row of the amount matrix
    # print(f"after simulation: {amount}")
    sorted = np.sort(amount)
    # print(f"after sort: {amount}")

    return np.mean(sorted, axis=0)

def arithmetic_game(amount, rows, winners, losers):
    # print(f"arithmetic_game({amount}, {winners}, {losers})")
    WIN = 20
    amount[rows, winners] += WIN
    amount[rows, losers] -= WIN
    # print(f"    results: {amount}")

def geometric_game(amount, rows, winners, losers):
    # print(f"arithmetic_game({amount}, {winners}, {losers})")
    WIN = 0.2
    winnings = np.minimum(amount[rows, winners], amount[rows, losers]) * WIN
    amount[rows, winners] += winnings
    amount[rows, losers] -= winnings
    # print(f"    results: {amount}")

# def geometric_game(prev1: float, prev2: float, draw: bool) -> Tuple[float, float]:
#     WIN = 0.2
#     smallest = min(prev1, prev2)
#     win = WIN * smallest
#     if draw:
#         return prev1 + win, prev2 - win
#     else:
#         return prev1 - win, prev2 + win

def graph(points: List[float], axis: str):
    x = range(len(points))
    plt.plot(x, points) 
    #plt.xlabel('x - axis') 
    plt.ylabel(axis)
    #plt.title(title)
    #plt.show(block = False) 

def test_simulate_arithmetic() -> List[float]:
    SIMULATIONS = 10000
    DRAWS = 100
    POPULATION = 100
    mean = simulation(SIMULATIONS, DRAWS, POPULATION, arithmetic_game)
    #print(f"test_simulate_arithmetic: mean={mean} stdev={stdev}")
    graph(mean, "test_simulate_arithmetic: means")

def test_simulate_geometric():
    SIMULATIONS = 10000
    DRAWS = 10000
    POPULATION = 100
    mean = simulation(SIMULATIONS, DRAWS, POPULATION, geometric_game)
    #print(f"test_simulate_geometric: mean={mean} stdev={stdev}")
    graph(mean, "test_simulate_geometric: means")

if __name__ == "__main__":
    test_simulate_arithmetic()
    test_simulate_geometric()
    plt.show()

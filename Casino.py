import random
import math
from typing import Callable, Tuple

def simulation(simulations: int, draws: int, game: Callable[[float, bool], float]) -> Tuple[float, float]:
    total = 0.0
    total_2 = 0.0
    for _ in range(simulations):
        amount = 100.0
        for _ in range(draws):
            choice = bool(random.getrandbits(1))
            amount = game(amount, choice)
            #print(f"amount={amount} choice={choice}")
        total = total + amount
        total_2 = total_2 + amount * amount
    
    n = float(simulations)
    mean = total / n

    # stdev = sqrt(sum(x - mean)^2 / (n - 1))
    #       = sqrt(sum(x^2 - 2 x mean + mean^2) / (n - 1))
    #       = sqrt((sum(x^2) - 2 mean sum(x) + mean^2) / (n - 1))
    #       = sqrt((sum(x^2) - 2 sum(x)^2 / n + n sum(x)^2 / n^2) / (n - 1))
    #       = sqrt((sum(x^2) - sum(x)^2 / n) / (n - 1))
    stdev = math.sqrt((total_2 - total * total / n ) / (n - 1))
    return mean, stdev

def arithmetic_game(prev: float, draw: bool) -> float:
    WIN = 2
    if draw:
        return prev + WIN
    else:
        return prev - WIN

def geometric_game(prev: float, draw: bool) -> float:
    WIN = 0.02
    if draw:
        return prev * (1.0 + WIN)
    else:
        return prev / (1.0 + WIN)

def test_simulate_arithmetic():
    SIMULATIONS = 100000
    DRAWS = 10
    mean, stdev = simulation(SIMULATIONS, DRAWS, arithmetic_game)
    print(f"test_simulate_arithmetic: mean={mean} stdev={stdev}")

def test_simulate_geometric():
    SIMULATIONS = 100000
    DRAWS = 10
    mean, stdev = simulation(SIMULATIONS, DRAWS, geometric_game)
    print(f"test_simulate_geometric: mean={mean} stdev={stdev}")

if __name__ == "__main__":
    test_simulate_arithmetic()
    test_simulate_geometric()

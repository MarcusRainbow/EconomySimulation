import random
import math
import numpy as np
from typing import Callable, Tuple

def simulation(simulations: int, draws: int, game: Callable) -> Tuple[float, float]:

    amount = np.full(simulations, 100.0)
    for _ in range(draws):
        draws = np.random.randint(2,size=simulations) != 0
        game(amount, draws)

    return np.mean(amount), np.std(amount)

def arithmetic_game(amount, draws) -> float:
    WIN = 2
    amount[draws] += WIN
    amount[np.logical_not(draws)] -= WIN

def geometric_game(amount, draws) -> float:
    WIN = 0.02
    amount[draws] *= (1.0 + WIN)
    amount[np.logical_not(draws)] /= (1.0 + WIN)

def test_simulate_arithmetic():
    SIMULATIONS = 10000
    DRAWS = 100
    mean, stdev = simulation(SIMULATIONS, DRAWS, arithmetic_game)
    print(f"test_simulate_arithmetic: mean={mean} stdev={stdev}")

def test_simulate_geometric():
    SIMULATIONS = 10000
    DRAWS = 100
    mean, stdev = simulation(SIMULATIONS, DRAWS, geometric_game)
    print(f"test_simulate_geometric: mean={mean} stdev={stdev}")

if __name__ == "__main__":
    test_simulate_arithmetic()
    test_simulate_geometric()

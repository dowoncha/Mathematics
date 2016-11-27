# filename: best_prize.py
# author: Dowon Cha
# summary: Simulation of the best prize problem
# Given n prizes in random order, choose the best prize.

import numpy as np
import matplotlib.pyplot as plt

def choose_best_prize(prizes):
    # Choose the best prize from the array of prizes
    # prizes array of prizes
    # return prize
    # Guess n / e
    guess = int(len(prizes) / np.exp(1))
    # Slice prizes to get all prizes indexed [0, n/e)
    observed = prizes[0:guess]

    # For each prize > n/e, choose the first one that is better than observed
    for prize in np.nditer(prizes[guess:len(prizes)]):
        if (np.greater_equal(prize, observed).all()):
            return prize

    return prizes[0]

if __name__ == "__main__":
    trials = 2000
    n = 100
    # Generate n random prizes
    # Uniform distribution
    prizes = np.random.uniform(size=n)
    # Normal distribution
    # mu = 50
    # sigma = 10
    # exponential
    # prizes = np.random.exponential(scale=2.0, size=n)

    result = np.zeros(trials)

    # We are going to do trials
    for trial in range(trials):
        # Shuffle list of prizes
        np.random.shuffle(prizes)
        # Choose the best prize from the prizes
        prize = choose_best_prize(prizes)
        # Add result to sample dataset
        result[trial] = prize

    plt.hist(result, bins=20)
    plt.title("Best Prize Problem")
    plt.xlabel("Prize")
    plt.ylabel("Frequency")

    fig = plt.gcf()
    plt.show()

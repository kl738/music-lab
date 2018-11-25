#!/usr/bin/env python
'''
TODO: plot of GINI index coefficient, plot of means of market shares of all songs
'''
'''
This program runs the music lab model based on equations 
specified by Xiaochen's writeup. Assumes there are five songs where:
QA = 0.5
QB = 0.3
QC = 0.1
QD = 0.05
QE = 0.05 (represents all other songs collectively)

Author - Kevin Lin (kl738)
'''

import numpy as np
import time
import random
import matplotlib.pyplot as plt


'''
Helper decorator to time function calls.
'''
def timeit(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        result = func(*args, **kwargs)
        e = time.time()
        print("Time elapsed:", e-s)
        return result
    return wrapper

'''
Calculates theoretical model.
Arguments:
    p - probability of convergence
    iterations - number of iterations to run, represents time or people
Returns:
    list of market shares over time for QA
'''
def theoretical(p, iterations, mover):
    # probs represents probability of downloading song i number of times.
    QA = 0.5
    if mover == "random":
        market_shares = [0.5]
        probs = [0.5,0.5]
    elif mover == "A":
        market_shares = [1]
        probs = [0,1]
    elif mover == "B":
        market_shares = [0]
        probs = [1,0]
    for n in range(2, iterations+1):
        if n % 100000==0:
            print("Theoretical Iteration:",n)
        # calculate all values for nth iteration recursively
        new_probs = [0] * (n+1)
        total = 0
        for j in range(len(new_probs)):
            if j == 0:
                new_probs[j] = probs[j] * (p + (1-p)*(1-QA))
            elif j == n:
                new_probs[j] = probs[j-1] * (p * (j-1)/(n-1) + (1-p)*QA)
            else:
                new_probs[j] = probs[j] * (p * (n-j-1)/(n-1) + (1-p)*(1-QA)) + probs[j-1] * (p * (j-1)/(n-1) + (1-p)*QA)
            total += new_probs[j] * j
        # updating market shares
        market_shares.append(total/n)
        # setting probs to new_probs
        probs = new_probs
    return market_shares

'''
Simulate a random walk based on same assumptions of Q and given p and iterations.
Arguments:
    p - probability of convergence
    iterations - number of iterations to run, represents time or people
Returns:
    list of market shares over time for QA
'''
def simulate(p, iterations, mover):
    probs = [0.5, 0.3, 0.1, 0.05, 0.05]
    counts = [0] * 5
    market_shares = []
    for iteration in range(iterations):
        r = random.random()
        r2 = random.random()
        # first mover randomly picks based on distribution
        # if iteration == 0:
        #     cumulative = np.cumsum(probs)
        #     for i, c in enumerate(cumulative):
        #         if r < c:
        #             counts[i] += 1
        #             break
        # first mover randomly picked uniformly
        if iteration == 0:
            if mover == "random":
                i = random.randint(0,4)
                counts[i] += 1
            elif mover == "A":
                counts[0] += 1
            elif mover == "B":
                counts[1] += 1
        # nth person picks based on others or on intrinsic preferences
        else:
            if r < p:
                total = sum(counts)
                cumulative = np.cumsum(counts)
                normed = []
                n = len(cumulative)
                for i in range(n):
                    normed.append(cumulative[i]/total)
                for i, c in enumerate(normed):
                    if r2 < c:
                        counts[i] += 1
                        break
            else:
                cumulative = np.cumsum(probs)
                for i, c in enumerate(cumulative):
                    if r2 < c:
                        counts[i] += 1
                        break
        # update market share
        # print(counts)
        market_shares.append(counts[0]/(iteration+1))
    return market_shares

def graph(simulations, theoretical, length, title, filename):
    plt.clf()
    x = list(range(1,length+1))
    for y in simulations:
        plt.plot(x,y,color = 'k', linewidth = 1)
    plt.plot(x, theoretical, color = 'r', linewidth = 1)
    plt.xlabel('Participants')
    plt.ylabel('Market Share')
    plt.title(title)
    plt.savefig(filename)

def experiment(iterations,p,mover,title, filename):
    print(title)
    exit(0)
    simulations = []
    for i in range(100):
        print("Simulation Iteration:", i)
        s = simulate(p, iterations, mover)
        simulations.append(s)
    t = theoretical(p, iterations, mover)
    graph(simulations, t, iterations, title, filename)

def main():
    iterations = 5000
    experiment(iterations,0.5,"random","Random first mover, p=0.5","rand_first_mover_p_0.5.png")
    experiment(iterations,0.9,"random","Random first mover, p=0.9","rand_first_mover_p_0.9.png")
    experiment(iterations,0.5,"A","A first mover, p=0.5","A_first_mover_p_0.5.png")
    experiment(iterations,0.9,"A","A first mover, p=0.9","A_first_mover_p_0.9.png")
    experiment(iterations,0.5,"B","B first mover, p=0.5","B_first_mover_p_0.5.png")
    experiment(iterations,0.9,"B","B first mover, p=0.9","B_first_mover_p_0.9.png")
if __name__ == "__main__":
    main()


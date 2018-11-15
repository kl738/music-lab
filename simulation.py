#!/usr/bin/env python

'''
This program runs the music lab model on a theoretical model based on equations 
specified by Xiaochen's writeup. Assumes there are five songs where:
QA = 0.5
QB = 0.3
QC = 0.1
QD = 0.05
QE = 0.05 (represents all other songs collectively)
'''

'''
Helper decorator to time function calls.
'''

'''
Arguments:
    p - probability of convergence
    iterations - number of iterations to run, represents time or people
Returns:
    list of market shares over time for QA
'''
def theoretical(p, iterations = 5000):
    # probs represents probability of downloading song i number of times.
    QA = 0.5
    market_shares = [0.5]
    probs = [0.5,0.5]
    for n in range(2, iterations+1):
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

def simulate(p, iterations = 5000):
    pass
def graph(lst):
    pass
def main():
    t = theoretical(0.5)
    # print(t)
if __name__ == "__main__":
    main()


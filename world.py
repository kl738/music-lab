import numpy as np

"""
The World class describes a single instance of an independent world in the
Music Lab study.
"""
class World:
    def __init__(self, c, p):
        """Initializing world with items and people."""
        self.c = c
        self.p = p
        self.generateItems(c)
        self.generatePeople(p)
    def generateItems(self, c):
        """
        Generates cultural items with a normally distributed intrinsic value
        and a list of 0s to represent the number of times each item has been
        "listened" to.
        """
        self.itemValues = np.random.normal(50, 10, size = c)
        self.itemCounts = [0] * c
    def generatePeople(self, p):
        """
        Generates simulated people with a normally distributed susceptibility
        range from 0(least susceptible) to 1(most susceptible) and a random
        order of preference for the cultural items.
        """
        self.peopleSuscepts = np.random.normal(.5, .1, size = p)
        self.peoplePrefs = [np.random.permutation(self.c) for _ in range(p)]
    def simulate(self):
        """
        Simulates the world for all people, by randomly generating a permutation
        of people to specify the order. Then, based on the susceptibility of that
        person, either pick between his own preferences or the listen counts of
        others. Also, probabilistically pick the between the top 4 in either list
        with p=0.4,0.3,0.2,0.1 respectively. Must be at least 4 items.
        """
        order = np.random.permutation([i for i in range(self.p)])
        for i in order:
            flag = False
            susc = np.random.random_sample()
            if susc <= self.peopleSuscepts[i]:
                flag = True
            choice = np.random.random_sample()
            if choice < 0.4:
                itemChoice = 0
            elif choice < 0.7:
                itemChoice = 1
            elif choice < 0.9:
                itemChoice = 2
            else:
                itemChoice = 3
            if flag:
                s = sorted(enumerate(self.itemCounts),key=lambda x: x[1], reverse = True)
                item = s[itemChoice][0]
                self.itemCounts[item] += 1
            else:
                item = self.peoplePrefs[i][itemChoice]
                self.itemCounts[item] += 1
            print(self.itemCounts)

def simple_test():
    w = World(4,5)
    print(w.itemValues)
    print(w.itemCounts)
    print(w.peopleSuscepts)
    print(w.peoplePrefs)
    w.simulate()

if __name__ == "__main__":
    simple_test()

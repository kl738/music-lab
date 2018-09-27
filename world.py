import numpy as np
import random

class World:
    def __init__(self, d, n, s, v, e, p, c):
        """
        d = dimensions
        n = number of agents
        s = number of songs
        v = variation among agents
        e = epsilon
        p = probability of imitation
        c = convergence parameter
        """
        self.d = d
        self.n = n
        self.s = s
        self.v = v
        self.e = e
        self.p = p
        self.c = c
        self.setSongs()
        self.setPeople()
        self.setScores()
        self.setPreferences()
    def setSongs(self):
        """sets scores for dimensions for each songs"""
        self.songs = [np.random.uniform(0,1,self.d) for _ in range(self.s)]
    def setPeople(self):
        """sets the weights of people, random and invariant for each dimension"""
        self.RW = [np.random.uniform(0,1,self.d) for _ in range(self.n)]
        self.IW = [np.random.uniform(0,1,self.d)] * self.n
    def setScores(self):
        """
        sets scores for each song by each person based on weighted sum calc.
        W(i,d)=(1-V)*IW(d) + V*RW(d)
        S(i,s) = sum from d=1 to D of [W(i,d)*(s,d)] + e
        scores[i] is the list of scores of songs for person i
        """
        self.scores = []
        for i in range(self.n):
            temp = []
            for song in self.songs:
                score = 0
                for j,d in enumerate(song):
                    score += (1-self.v)*self.IW[i][j]*d + self.v * self.RW[i][j]*d
                if np.random.rand() < .5:
                    temp.append(score + self.e)
                else:
                    temp.append(score - self.e)
            self.scores.append(temp)
    def setPreferences(self):
        """
        preferences[i] is the preference list of person i. songs are represented
        by their original index in self.songs
        """
        self.preferences = []
        for scorelst in self.scores:
            scorelst = list(enumerate(scorelst))
            scorelst.sort(reverse = True, key = lambda x: x[1])
            temp = []
            for i,j in scorelst:
                temp.append(i)
            self.preferences.append(temp)
    def simulate(self):
        """
        Simulates music lab experiment with urn model.
        1. generates random permutation of people, people are later chosen at
           time step without replacement
        2. at each time step with probabibilty p, a person will pick from the urn
           uniformly, else pick his own top preference.
        3. if past 'c' songs are the same, then model has converged, and return
           urn
        4. if all 'n' people have gone, and model has converged, then there is no
           convergence, return urn
        """
        self.urn = []
        np.random.permutation(self.preferences)
        while self.preferences:
            if len(self.urn) < self.c-1:
                pass
            else:
                flag = True
                for i in range(len(self.urn)-c+1, len(self.urn)):
                    if self.urn[i] != self.urn[i-1]:
                        flag = False
                if flag:
                    return self.urn, self.urn(len(self.urn)-1)
            person = self.preferences.pop()
            if self.urn == []:
                self.urn.append(person[0])
            else:
                if np.random.rand() < p:
                    choice = random.choice(self.urn)
                    self.urn.append(choice)
                else:
                    self.urn.append(person[0])
        return self.urn, -1

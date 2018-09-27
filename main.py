from world import World

def simple_test():
    w = World(2,100,10,1,0.1,.7,5)
    print(w.songs)
    print(w.RW)
    print(w.IW)
    print(w.scores)
    print(w.preferences)
    print(w.simulate())
if __name__ == "__main__":
    simple_test()

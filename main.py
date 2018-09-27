from world import World

def simple_test():
    w = World(2,5,3,1,0,1,5)
    print(w.songs)
    print(w.RW)
    print(w.IW)
    print(w.scores)
    print(w.preferences)
if __name__ == "__main__":
    simple_test()

from world import World

def simple_test():
    w = World(4,1000)
    print(w.itemValues)
    w.simulate()
    print(w.itemCounts)
    print(w.spearman)

if __name__ == "__main__":
    simple_test()

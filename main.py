from markov import Node

def main():
    print("Mach Presto")
    n = Node("Das")
    m = Node("Haus")
    o = Node("Dorf")
    n.add_successor(m)
    n.add_successor(o)
    print(n.next())

if __name__ == "__main__":
    main()

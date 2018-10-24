from markov import Node, NodeMap

def main():
    # print("Mach Presto")
    # n = Node("Das")
    # m = Node("Haus")
    # o = Node("Dorf")
    # n.add_successor(m)
    # n.add_successor(o)
    # print(n.next())

    nodemap = NodeMap()

    sentences = [
        "I thought not",
        "It's not a story the Jedi would tell you",
        "It's a Sith legend"
    ]

    for s in sentences:
        nodemap.parse_sentence(s)
    
    print(str(nodemap))

if __name__ == "__main__":
    main()

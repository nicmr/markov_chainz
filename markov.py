class Node:
    def __init__(self, name):
        self.__name = name
        self.probs = {}

    def name(self):
        """Returns the name of `self`"""
        return self.__name

    def probability(self):
        """Returns the probability of the next node"""

    def add_successor(self, other_node, occurences=1):
        """Adds a new successor to the node, updating instead if the node already exists.
            Optionally, occurences may be set to any uint number
            to add multiple occurences of the successor node"""
        self.probs[other_node]  = self.probs.get(other_node, 0) + occurences

    def next(self):
        """Randomly chooses one of the possible following nodes"""
        sum = 0
        for k in self.probs.values():
            sum += k
        return sum

    def merge(self, other_node):
        """Merges the information of self and other_nodes into self.
        Please be aware it is not required for both nodes to have an identical name,
        and check for that requirement yourself should it be desired."""

        for key, value in other_node.probs.items():
            self.add_successor(key, value)

    def __hash__(self):
        return hash(self.name())

    def __eq__(self, other):
        return self.name() == other.name()

    def __str__(self):
        list = []
        for key, value in self.probs.items():
            list.append("\t")
            list.append(key.name())
            list.append(str(value))
            list.append("\n")
        return self.name() + " ".join(list)

class NodeMap:
    def __init__(self):
        self.nodes = {}

        # add beginning of sentence symbol
        self.nodes["^"] = Node("^")
        # add end of sentence symbol
        self.nodes["$"] = Node("$")

    def update(self, key, other_node):
        """Updates the node found for key string with the information in other_node"""
        node = self.nodes.get(key)
        if node:
            self.nodes[key] = node.merge(other_node)
        else:
            self.nodes[key] = other_node

    def parse_sentence(self, sentence):
        """Parses sentence and maps onto self"""

        #separate words at whitespace
        words = sentence.split(" ")

        #transform all words into nodes
        new_nodes = list(map(lambda x: Node(x), words))

        # Start of sentence symbol to first word
        start = Node("^")
        start.add_successor(new_nodes[0])
        self.update(start.name(), start)

        # last word to end of sentence symbol
        last = new_nodes[-1]
        end = Node("$")
        last.add_successor(end)
        self.update(last.name(), last)

        # all other words and their successors
        for i in range(0, len(new_nodes)-1):
            node = new_nodes[i]
            node.add_successor(new_nodes[i+1])
            self.update(node.name(), node)



    def __str__(self):
        list = []
        for _, node in self.nodes.items():
            list.append(str(node))
            list.append("\n")
        return "".join(list)
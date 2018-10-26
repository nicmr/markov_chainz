class Node:
    def __init__(self, name):
        self.__name = name
        self.probs = {}

    def name(self):
        """Returns the name of `self`"""
        return self.__name

    def probability(self, node):
        """Returns the probability of node to be the next node"""
        
    def sum(self):
        """Returns the sum of all values found in self.probs"""
        sum = 0
        for k in self.probs.values():
            sum += k
        
        return sum

    def add_successor(self, successor, occurences=1):
        """Adds a new successor to the node, merging the successor instead if it already exists.
            Optionally, occurences may be set to any uint number
            to add multiple occurences of a successor node"""
        self.probs[successor]  = self.probs.get(successor, 0) + occurences

    def next(self):
        """Randomly chooses one of the possible following nodes"""
        
        
        #CONCEPT #1
        #sum determines integer range for RNG
        #walk through probs, subtracting the corresponding integer value of each entry from rng number
        #until rng = 0
        #then choose current entry
        #PRO:   - relatively simple
        #CON:   - iteration through hashmap inefficient
        #       - iteration through unordered collctions not guaranteed to be in order
        #       -> these might be solved by using a treemap instead (possibly requiring own implementation)

        #stub

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

    def update(self, other_node):
        """Updates an equal node in self with the information in other_node,
        adding other_node to self if no equal node is found"""

        #TODO: rework from map to set, a string key is not needed as determination of node equality
        #       is already provided with the __eq__ function

        key = other_node.name()
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
        self.update(start)

        # last word to end of sentence symbol
        last = new_nodes[-1]
        end = Node("$")
        last.add_successor(end)
        self.update(last)

        # all other words and their successors
        for i in range(0, len(new_nodes)-1):
            node = new_nodes[i]
            node.add_successor(new_nodes[i+1])
            self.update(node)

    def __str__(self):
        list = []
        for _, node in self.nodes.items():
            list.append(str(node))
            list.append("\n")
        return "".join(list)
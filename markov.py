class Node:
    def __init__(self, name):
        self.name = name
        self.probs = {}

    def probability(self):
        """Returns the probability of the next node"""

    def add_successor(self, other_node):
        """Adds a new successor to the node"""
        self.probs[other_node]  = self.probs.get(other_node, 0) + 1

    def next(self):
        """Chooses the following word from the probability"""
        sum = 0
        for k in self.probs.values():
            sum += k
        return sum


    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        import json
        #str(len(self.probs.keys()))
        list = []
        for key, value in self.probs.items():
            list.append(str(key))
            list.append(str(value))
        return self.name + " ".join(list)









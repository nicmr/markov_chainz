from markov import Node, NodeMap


# tests for Node
# test names are the name of the tested function prefixed by "test"

def test_name():
    s = "samplename"
    node = Node(s)
    assert node.name() == s

# will fail if test_name() fails
def test_add_successor():
    s = "samplename"
    s2 = "successorname"

    node = Node(s)
    successor = Node(s2)

    node.add_successor(successor)

    assert successor in list(node.probs.keys())

# will fail if add_succesor fails
def test_merge():
    s = "samplename"
    s2 = "successorname"

    s3 = "other_successorname"

    node = Node(s)
    successor = Node(s2)
    node.add_successor(successor)

    other = Node(s)
    other_succesor = Node(s3)
    other.add_successor(other_succesor)

    node.merge(other)

    assert other_succesor in list(node.probs.keys())


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
    s = "sample_name"
    s2 = "successor_name"

    s3 = "other_successor_name"

    node = Node(s)
    successor = Node(s2)
    node.add_successor(successor)

    other = Node(s)
    other_succesor = Node(s3)
    other.add_successor(other_succesor)

    node.merge(other)

    assert other_succesor in list(node.probs.keys())



# tests for NodeMap

def test_update():
    s = "sample_name"
    s2 = "succesor_name"

    nodemap = NodeMap()
    node = Node(s)
    successor = Node(s2)

    nodemap.update(node)

    assert node in list(nodemap.nodes.values())
    assert s in list(nodemap.nodes.keys())
    assert not nodemap.nodes.get(s).probs

    node.add_successor(successor)

    #TODO: the following tests fail, possibly hinting at a bug in update
    # might have to do with copy / clone semantics

    
    # nodemap.update(node)
    # assert node in list(nodemap.nodes.values())
    # assert s in list(nodemap.nodes.keys())
    #assert nodemap.nodes.get(s).probs.get(successor)
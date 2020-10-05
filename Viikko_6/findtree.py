from collections import namedtuple

def count(node1, node2):
    # TODO

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree1 = Node(Node(None,None),Node(None,None))
    tree2 = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree1,tree2)) # 1
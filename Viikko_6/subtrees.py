from collections import namedtuple

def diff(node):
    # TODO

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(diff(tree)) # 3
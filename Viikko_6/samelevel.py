from collections import namedtuple

def count(node, level):
    if not node or level <= 0:
        return 0 # tyhjä puu
    elif level == 1:
        return 1 # juuritasolla 1 solmu
    else:
        return count(node.left, level - 1) + count(node.right, level - 1)

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree,1)) # 1
    print(count(tree,2)) # 1
    print(count(tree,3)) # 2
    print(count(tree,4)) # 0
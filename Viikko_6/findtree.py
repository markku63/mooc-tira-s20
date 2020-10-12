from collections import namedtuple

def same(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    return same(node1.left,node2.left) and same(node1.right,node2.right)

def count(node1, node2):
    if not node2:
        return 0
    elif same(node1, node2):
        return 1
    else:
        return count(node1, node2.left) + count(node1, node2.right)

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree1 = Node(Node(None,None),Node(None,None))
    tree2 = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree1,tree2)) # 1
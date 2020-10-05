from collections import namedtuple

def same(node1, node2):
    if not node1 and not node2: # molemmat tyhjiä
        return True
    elif (not node1) ^ (not node2):
        return False 
    elif not node1.left and not node1.right and not node2.left and not node2.right:
        # molemmat lehtiä
        return True
    elif node1.left and node1.right and node2.left and node2.right:
        # molemmilla kaksi alipuuta
        return same(node1.left, node2.left) and same(node1.right, node2.right)

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree1 = Node(None,Node(Node(None,None),Node(None,None)))
    tree2 = Node(Node(Node(None,None),Node(None,None)),None)
    tree3 = Node(None,Node(Node(None,None),Node(None,None)))
    print(same(tree1,tree2)) # False
    print(same(tree1,tree3)) # True
    print(same(tree2,tree3)) # False
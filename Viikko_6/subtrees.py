from collections import namedtuple

def count(node):
    if not node:
        return 0
    elif not node.left and not node.right:
        return 1
    else:
        return 1 + count(node.left) + count(node.right)

def diff(node):
    if not (node and (node.left or node.right)):
        # Tyhjä solmu tai lehti
        return 0
    else:
        return max(diff(node.left), diff(node.right), abs(count(node.left) - count(node.right)))

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(diff(tree)) # 3
    tree = Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=Node(left=Node(left=None, right=None), right=None)))
    print(diff(tree)) # 3
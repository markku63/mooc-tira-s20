from collections import namedtuple

def diff(node):
    if not (node and (node.left or node.right)):
        return 0
    elif not node.right:
        return diff(node.left) + 1
    elif not node.left:
        return diff(node.right) + 1
    else:
        return max(diff(node.left), diff(node.right))

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(diff(tree)) # 3
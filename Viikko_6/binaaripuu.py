from collections import namedtuple

Node = namedtuple("Node",["left","right"])

def height(node):
    if not node:
        return -1
    return 1 + max(height(node.left), height(node.right))

if __name__ == "__main__":
    node4 = Node(None, None)
    node5 = Node(None, None)
    node7 = Node(None, None)
    node8 = Node(None, None)
    node2 = Node(node4, None)
    node6 = Node(node7, node8)
    node3 = Node(node5, node6)
    node1 = Node(node2, node3)

    print(height(node1)) # 3

    tree = Node(
            Node(Node(Node(Node(Node(Node(Node(Node(Node(None, None), None), None), None), None), None), None), None), None), None
    )

    print(height(tree)) # 9
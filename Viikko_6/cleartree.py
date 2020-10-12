from collections import namedtuple

def count(node):
    if not node:
        return 0
    elif not node.left and not node.right:
        return 1
    else:
        # käydään läpi jokainen solmu postorderissa
        # poistetaan lehti ja 
        # kutsutaan count() jäljellä olevalle puulle
        return count(node.left) + count(node.right)

if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 2
    tree = Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=Node(left=Node(left=None, right=None), right=None)), right=None), right=Node(left=Node(left=None, right=None), right=None)), right=None)
    print(count(tree)) # 63
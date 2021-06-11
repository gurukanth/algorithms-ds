class Node:
    left
    right
    value:int

    def __init__(self, value):
        self.value = value

    def left(self, node):
        self.left = node
    
    def right(self, node):
        self.right = node


class BinaryTree:
    root:Node

    def __init__(self, root:Node):
        self.root = root
    
    def search(value:int):
        if not root:
            return None
        elif root.value == value:
            return root
        elif value < root.value:
            return search(root.left)
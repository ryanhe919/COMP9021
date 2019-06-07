class Tree:
    def __init__(self, value = None):
        self.value = value
        if value is None:
            self.left_subtree = None
            self. right_subtree = None
        else:
            self.left_subtree = Tree()
            self.right_subtree = Tree()

""" Node module """

class Node:
    """ Node class """
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None # mindre än
        self.right = None # större än


    def has_parent(self):
        """ Check if node has a parent, return Bool """
        return self.parent is not None


    def has_left_child(self):
        """ Check if node has a left child, return Bool """
        if self.left:
            return True
        return False
        #return self.left is not None


    def has_right_child(self):
        """ Check if node has a right child, return Bool """
        if self.right:
            return True
        return False
        #return self.right is not None


    def has_both_children(self):
        """ Check if node has both left and right child, return Bool """
        if self.left and self.right:
            return True
        return False


    def is_left_child(self):
        """ return bool if node is left child to parent """
        if self.parent:
            if self.parent.key > self.key:
                return True
        return False


    def is_right_child(self):
        """ return bool if node is right child to parent """
        if self.parent:
            if self.parent.key < self.key:
                return True
        return False


    def is_leaf(self):
        """ return True if node does not 
        have a right nor right child, else return False """
        if self.left is None and self.right is None:
            return True
        return False


    def __lt__(self, other):
        """ return True if a node is less then other, else False """
        if self.key < other.key:
            return True
        return False


    def __gt__(self, other):
        """ return True if a node is greater then other, else False """
        if self.key > other.key:
            return True
        return False


    def __eq__(self, other):
        """ return True if a node is == other, else False """
        if self.key == other.key:
            return True
        return False


if __name__ == "__main__":
    node1 = Node(5, "första")
    node2 = Node(5, "första")
    node1.left = node2
    print(node2.is_leaf())

    # node1.parent = node2


    # print(node1.is_right_child())

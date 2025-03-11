""" Binary search Tree module """
# DENNA ÄR DEN SENASTE
# DELA UPP KONTROLLER I REMOVE TILL EGNA METODER
from node import Node


class BinarySearchTree:
    """ BST Class"""
    def __init__(self):
        self.root = None


    def insert(self, key, value):
        """ Insert node to tree """
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(self.root, key, value)


    @classmethod
    def _insert(cls, node, key, value):
        """ insert node in the right location """
        if key < node.key:
            if node.has_left_child():
                cls._insert(node.left, key, value)
            else:
                node.left = Node(key, value, node)
        elif key > node.key:
            if node.has_right_child():
                cls._insert(node.right, key, value)
            else:
                node.right = Node(key, value, node)
        else:
            node.value = value # ersätt nyckel med nya värdet


    def inorder_traversal_print(self):
        """ Printa trädet i storleksorderning om det inte är tomt """
        if not self.root:
            return "Empty tree"

        return self._inorder_traversal_print(self.root)


    @classmethod
    def _inorder_traversal_print(cls, node):
        """ Private metod som traverserar trädet recursivt """

        # print(node.key) PRE ORDER
        if node.has_left_child():
            cls._inorder_traversal_print(node.left)

        print(node.key) # IN ORDER

        if node.has_right_child():
            cls._inorder_traversal_print(node.right)

        #print(node.key) # POST ORDER


    def get(self, key):
        """ Return the value of key if 
        key exists, else raise KeyError """
        return self._get(self.root, key)

    @classmethod
    def _get(cls, node, key):
        """ Return the value of key if 
        key exists, else raise KeyError """
        # print(node.key)
        if not node:
            raise KeyError
        if key == node.key:
            print(f"get(key) är samma som node.key, {node.value}")
            return node.value

        if not node.is_leaf():
            if key < node.key:
                return cls._get(node.left, key)

            if key > node.key:
                return cls._get(node.right, key)
        raise KeyError


    def remove(self, key):
        """ Return the value of the removed key
        if key exists. Else raise KeyError """
        if not self.root:
            raise KeyError

        # Om key är root
        if self.root.is_leaf():
            root_value = self.root.value
            self.root = None
            return root_value

        # Annars hitta key
        node = self._find_node_with_key(self.root, key)

        # Return borttaget värde
        value = node.value

        # Uppdatera trädet
        if node and node.is_leaf():
            print(f"Node {node.key} är ett löv")
            self._remove_leaf(node)
        # Om båda barn
        elif node and node.has_both_children():
            print(f"Noden {node.key} har båda barnen")
            smallest_child = self._find_smallest_child(node.right)
            node.key = smallest_child.key
            node.value = smallest_child.value

            # Om minsta noden är ett löv
            if smallest_child.is_leaf():
                print(f"Noden {node.key} som har två barn, har ett löv"+
                      f" som minsta barn, {smallest_child.key}")
                self._remove_leaf(smallest_child)
            else:
                self._remove_node_with_one_kid(smallest_child)

        # Om ett barn
        elif node and not node.has_both_children():
            print(f"Noden {node.key} har ett barn")
            self._remove_node_with_one_kid(node)

        return value


    def _find_node_with_key(self, node, key):
        """ Find a node with a given key """
        # samma värde
        if key == node.key:
            return node
        # gå vänster
        if key < node.key:
            return self._find_node_with_key(node.left, key)
        # key är större, gå höger
        return self._find_node_with_key(node.right, key)


    def _remove_leaf(self, node):
        """ Remove node with no kids """
        if node.is_left_child():
            node.parent.left = None
        else:
            node.parent.right = None
        return node.value


    def _remove_node_with_one_kid(self, node):
        """ Remove a node that has one child """
        if node.has_left_child():
            child = node.left
        else:
            child = node.right

        if node.has_parent():
            if node.is_left_child():
                node.parent.left = child
            else:
                node.parent.right = child
            child.parent = node.parent
        elif not node.has_parent():
            self.root = child
            self.root.parent = None

        return node.value


    @classmethod
    def _find_smallest_child(cls, node):
        """ Find the node with the smallest key in left leg """
        if node.left:
            return cls._find_smallest_child(node.left)
        return node


    def size(self):
        """ Return the size of the BST as int"""
        return self._size(self.root)


    @classmethod
    def _size(cls, node):
        if node is None:
            return 0
        return 1 + cls._size(node.left) + cls._size(node.right)


if __name__ == "__main__":
    #import treevizer  # TA BORT VID INLÄMNING AV KMOM
    bst = BinarySearchTree()

    values1 = [3, 8, 5, 6, 1, 0, 2, 4, 9, 7]

    # ta bort alla noder i träd
    values2 = [9, 5, 2, 15, 4, 3, 11, 12, 10, 0, 1, 14, 16, 7, 8, 6]
    for i in values2:
        bst.insert(i, str(i))

    # ta bort i ordning
    remove = [5, 0, 2, 3, 14, 16, 4, 15, 1, 6, 12, 10, 7, 11, 8, 9]

    print("Vi tar bort 5 ")
    print("storlek före remove", bst.size(), "\n")
    print(f"Borttaget värde: {bst.remove(5)}")
    print("storlek efter remove", bst.size(), "\n")

   # treevizer.to_png(bst.root)

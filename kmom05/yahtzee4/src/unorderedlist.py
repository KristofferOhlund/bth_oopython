"""
Module for the unordered list
"""

from src.node import Node
from src.errors import MissingIndex, MissingValue


class UnorderedList:
    """LinkedList class"""
    def __init__(self):
        self._head = None # Blir en lista då noder pekar på varandra
        # node.data = värde
        # node.next = nästa nod

    def append(self, value):
        """Method to append data to _head"""
        if self._head is None:
            self._head = Node(value)
            # self._head har nu en node med attribute data, next
        else:
            current_node = self._head
            while current_node.has_next():
                current_node = current_node.next # sätt nuvarande node till värdet för node.next
            current_node.next = Node(value) # node har inget next, skapa det utifrån value

    def set(self, index, data):
        """Overwrite element at index, with data.
        If index does not exist, raise Missing Index exception."""
        if self._head:
            counter = 0
            current = self._head
            while current.has_next() and counter < index:
                current = current.next
                counter += 1
            if counter == index:
                temp = current.next
                current = Node(data)
                current.next = temp
                self._head = current
            else:
                raise MissingIndex ("Index finns inte")
        else:
            raise MissingIndex ("Index finns inte, head är tomt")


    def remove(self, data):
        """Remove node with same data, else raise MissingValue"""
        remove_at_index = self.index_of(data) # Value exists at index
        if remove_at_index is not None:
            current = self._head

            # Om första index ska bort
            if remove_at_index == 0:
                self._head = current.next

            # Om sista index ska bort
            elif remove_at_index == self.size() -1:
                remove_at_index -= 1
                counter = 0
                while current.has_next() and counter < remove_at_index:
                    current = current.next
                    counter += 1

                if counter == remove_at_index:
                    current.next = None

            # Om övriga index ska bort
            else:
                counter = 0
                while current.has_next() and counter < remove_at_index:
                    previous = current
                    current = current.next
                    counter += 1

                if counter == remove_at_index:
                    self._head = previous
                    if self._head.has_next():
                        self._head.next = current.next


    def index_of(self, value):
        """If value in self._head, return its index.
        Else raise MissingValue"""
        if self._head is not None:
            current = self._head
            index = 0
            while not self.check_equal(current.data, value):
                if current.has_next():
                    current = current.next
                    index += 1
                else:
                    raise MissingValue(f"'{value}' finns inte i listan, index of")
            return index
        raise MissingValue(f"{value} finns inte i listan")


    def check_equal(self, answer, value):
        """Return answer == value"""
        return answer == value


    def size(self):
        """Return the number of elements in self._head, 0 if empty"""
        if self._head is not None:
            current = self._head
            count = 1
            while current.has_next():
                current = current.next
                count +=1
            return count
        return 0


    def get(self, index):
        """Method to return data at the specified index"""
        if self._head is not None:
            count = 0
            current_node = self._head
            while current_node.has_next() and count < index:
                current_node = current_node.next
                count += 1
            if count == index:
                return current_node.data
            # count är mindre än index, men current_node har inte next
            raise MissingIndex("Index finns inte i LL")
        # head är None
        raise MissingIndex ("Index finns inte i LL")


    def print_list(self):
        """Print all values in self._head"""
        if self._head is not None:
            current = self._head
            while current.data:
                print(current.data)
                if current.has_next():
                    current = current.next
                else:
                    break


    def __str__(self):
        """Return string representation of the UnorderedList object"""
        return str(self._head)


if __name__ == "__main__":
    ul = UnorderedList()
    ul.append("one")
    ul.append("two")
    ul.append("three")
    ul.append('(magnus, 44)')
    print(ul.index_of("(magnus, 44)"))

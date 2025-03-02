""" Queue module """

class Queue:
    """ Queue class """
    def __init__(self, data=None):
        self._items = data or []

    def is_empty(self):
        """ If queue is empty, return True, else False"""
        if not self._items:
            return True
        return False

    def enqueue(self, item):
        """ add to queue """
        self._items.append(item)

    def dequeue(self):
        """ Remove queue """
        try:
            return self._items.pop(0)

        except IndexError:
            return "Empty list."

    def peek(self):
        """ Peek to see who's next """
        return self._items[0]

    def size(self):
        """ Return the len of items"""
        return len(self._items)

    def to_list(self):
        """ Return queue as list """
        queue = []
        for player in self._items:
            queue.append(player)
        return queue
    

    @classmethod
    def from_session(cls, data):
        """ Create a queue instance from current data """
        return cls(data)


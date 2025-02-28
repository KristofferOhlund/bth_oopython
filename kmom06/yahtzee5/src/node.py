"""
Node module
"""

class Node:
    """Node class"""
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next

    def has_next(self):
        """Check self.next, return bool"""
        return self.next is not None

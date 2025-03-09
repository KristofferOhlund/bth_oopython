"""
Module for testing the recursive insertion for sort
"""

# För att kunna testa privata attribut och metoder
# pylint: disable=protected-access

import unittest
from src.unorderedlist import UnorderedList

from src.sort import recursive_insertion


class TestSort(unittest.TestCase):
    """ Submodule for unittests, 
    derives from unittest.TestCase. 
    Submodule is for testing the sort method """
    def setUp(self):
        self.ul = UnorderedList()


    def test_empty_list(self):
        """ Test sort an empty list """
        empty_entries = recursive_insertion([], self.ul.size())
        self.assertEqual(empty_entries, -1)

    def test_recursive_sort(self):
        """ Test to sort a UnorderedList recursivly """
        self.ul.append(88)
        self.ul.append(77)
        self.ul.append(12)
        self.ul.append(16)
        self.ul.append(25)

        recursive_insertion(self.ul, self.ul.size())

        result = []

        for i in range(self.ul.size()):
            result.append(self.ul.get(i))

        self.assertListEqual(result, [12, 16, 25, 77, 88])


    def test_sort_recursive_reversed(self):
        """ Test to sort an UnorderList with reversed order,
        sorting the UL from smallest to biggest """
        self.ul.append(88)
        self.ul.append(77)
        self.ul.append(65)
        self.ul.append(55)
        self.ul.append(45)
        self.ul.append(35)
        self.ul.append(23)

        recursive_insertion(self.ul, self.ul.size())

        result = []

        for i in range(self.ul.size()):
            result.append(self.ul.get(i))

        self.assertListEqual(result, [23, 35, 45, 55, 65, 77, 88])

    def test_sort_tuple_int(self):
        """ Test to sort an UnorderList with reversed order,
        sorting the UL from smallest to biggest """
        self.ul.append((88, "hej"))
        self.ul.append((98, "hej"))
        self.ul.append((11, "hej"))
        self.ul.append((25, "hej"))
        self.ul.append((1, "hej"))


        recursive_insertion(self.ul, self.ul.size())

        result = []

        for i in range(self.ul.size()):
            result.append(self.ul.get(i))

        self.assertListEqual(result, [(1, "hej"), (11, "hej"), (25, "hej"),
                                      (88, "hej"), (98, "hej")])


    def test_sort_str(self):
        """ Test to sort an UnorderList with reversed order,
        sorting the UL from smallest to biggest """
        self.ul.append("hej")
        self.ul.append("jag")
        self.ul.append("är")
        self.ul.append("ett")
        self.ul.append("test")


        recursive_insertion(self.ul, self.ul.size())

        result = []

        for i in range(self.ul.size()):
            result.append(self.ul.get(i))

        self.assertListEqual(result, ['ett', 'hej', 'jag', 'test', 'är'])

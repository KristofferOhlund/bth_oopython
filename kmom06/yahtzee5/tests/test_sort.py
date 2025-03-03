"""
Module for testing the recursive insertion for sort
"""

# För att kunna testa privata attribut och metoder
# pylint: disable=protected-access

import unittest
from src.leaderboard import Leaderboard
from src.unorderedlist import UnorderedList

from src.sort import recursive_insertion


class TestSort(unittest.TestCase):
    """ Submodule for unittests, 
    derives from unittest.TestCase. 
    Submodule is for testing the sort method """
    def setUp(self):
        self.ul = UnorderedList()


    def test_empty_list(self):
        """ Test to add an empty list"""
        empty_entries = recursive_insertion([], self.ul.size())
        self.assertEqual(empty_entries, -1)

    def test_sort(self):
        """ Test to sort leaderboard"""
        lb = Leaderboard()


        lb.add_entry(98,'Rubi')
        lb.add_entry(54,'Kristoffer')
        lb.add_entry(90,'Janne')


        lb_sorted = recursive_insertion(lb.entries, lb.entries.size())

        result = []

        for i in range(lb_sorted.size()):
            result.append(lb_sorted.get(i))

        self.assertListEqual(result, [(54, 'Kristoffer'), (90, 'Janne'), (98, 'Rubi')])

"""
Module for testing the Hand class
"""

# För att kunna testa privata attribut och metoder
# pylint: disable=protected-access

import unittest
from src.unorderedlist import UnorderedList
from src.errors import MissingIndex, MissingValue


class TestDie(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """Setup """
        self.ul = UnorderedList()
        self.ul.append('A')
        self.ul.append('B')
        self.ul.append('C')
        self.ul.append('D')


    def test_get_exception(self):
        """ Test leaderboard wether an exception is raised if index
        does not exist. """
        with self.assertRaises(MissingIndex) as _e:
            self.ul.get(9)  # add again -> ValueError is raised


    def test_get_value(self):
        """ Test leaderboard wether a value is returned when value exists. """
        self.assertEqual(self.ul.get(0), "A")


    def test_get_value_2(self):
        """ Test leaderboard wether a value is returned when value exists. """
        self.assertEqual(self.ul.get(2), "C")


    def test_remove_exception(self):
        """ Test leaderboard if exception is raised when remove is
        used on a value that does nt exists"""
        with self.assertRaises(MissingValue) as _e:
            self.ul.remove("farfar")


    def test_remove_first_value(self):
        """ Test leaderboard if remove method removes the correct value 
        when index is 0 """

        self.ul.remove("A")
        list_values = []
        for idx in range(self.ul.size()):
            list_values.append(self.ul.get(idx))
        self.assertListEqual(list_values, ["B", "C", "D"])


    def test_remove_last_value(self):
        """ Test leaderboard if remove method removes the correct value 
        when index is is -1 """

        self.ul.remove("D")
        list_values = []
        for idx in range(self.ul.size()):
            list_values.append(self.ul.get(idx))
        self.assertListEqual(list_values, ["A", "B", "C"])


    def test_remove_middle_value(self):
        """ Test leaderboard if exception is raised when remove is
        used on a value that does not exists"""

        self.ul.remove("C")
        list_values = []
        for idx in range(self.ul.size()):
            list_values.append(self.ul.get(idx))
        self.assertListEqual(list_values, ["A", "B", "D"])

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
        self.ul.append('one')
        self.ul.append('two')
        self.ul.append('three')


    def test_get_exception(self):
        """ Test leaderboard wether an exception is raised if index
        does not exist. """
        with self.assertRaises(MissingIndex) as _e:
            self.ul.get(9)  # add again -> ValueError is raised


    def test_get_value(self):
        """ Test leaderboard wether a value is returned when value exists. """
        self.assertEqual(self.ul.get(0), "one")


    def test_get_value_2(self):
        """ Test leaderboard wether a value is returned when value exists. """
        self.assertEqual(self.ul.get(2), "three")


    def test_remove_exception(self):
        """ Test leaderboard if exception is raised when remove is
        used on a value that does nt exists"""
        with self.assertRaises(MissingValue) as _e:
            self.ul.remove("farfar")


    def test_remove_value(self):
        """ Test leaderboard if exception is raised when remove is
        used on a value that does not exists"""

        self.ul.remove("three")
        self.assertListEqual(self.ul.print_list(), ["one", "two"])

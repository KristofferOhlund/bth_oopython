""" Module for testing the Scoreboard class"""

import unittest
from src.hand import Hand
from src.scoreboard import Scoreboard

class TestScoreboard(unittest.TestCase):
    """ Submodule for unittests, 
    derives from unittest.TestCase. 
    Submodule is for testing the Scoreboard module """

    def setUp(self):
        """ Initialize a hand object, available for all tests in module"""
        self.sb = Scoreboard()


    def test_add_points_yahtzee(self):
        """ Test to add a points for a given rule """
        hand = Hand([3, 3, 3, 3, 3])
        rule = "Yahtzee"
        self.sb.add_points(rule, hand)
        self.assertEqual(self.sb.get_points(rule), 50)

    def test_add_points_small_straight(self):
        """ Test ScoreBoard add points with small_straight rule"""
        hand = Hand([1, 2, 3, 4, 6])
        rule = "Small Straight"
        self.sb.add_points(rule, hand)
        self.assertEqual(self.sb.get_points(rule), 30)

    def test_add_points_three_of_a_kind(self):
        """ Test ScoreBoard add points with Three Of A Kind rule"""
        hand = Hand([2, 2, 2, 4, 4])
        rule = "Three Of A Kind"
        self.sb.add_points(rule, hand)
        self.assertEqual(self.sb.get_points(rule), 14)

    def test_rule_used(self):
        """ Test whether exception is raised when a rule
        already used get points. """
        hand = Hand([3, 3, 3, 3, 3])
        rule = "Yahtzee"
        self.sb.add_points(rule, hand) # add points once
        with self.assertRaises(ValueError) as _e:
            self.sb.add_points(rule, hand) # add again -> ValueError is raised

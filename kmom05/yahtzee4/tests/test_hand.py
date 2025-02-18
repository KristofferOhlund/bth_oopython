"""
Module for testing the Hand class
"""

# För att kunna testa privata attribut och metoder
# pylint: disable=protected-access

import unittest
import random
from src.hand import Hand


class TestDie(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """Setup that runs before every testcase"""
        random.seed("startvalue")  # Set start seed value


    def test_hand_no_arg(self):
        """Test if hand correctly creates an object with 5 dices"""
        hand = Hand()
        self.assertEqual(str(hand), "1, 2, 4, 1, 5")


    def test_hand_with_arg(self):
        """Test if hand """
        hand = Hand([1, 2, 3, 4, 5])
        self.assertEqual(str(hand), "1, 2, 3, 4, 5")


    def test_hand_to_list(self):
        """Test if hand creates an object storing 5 dices.
        Each dice should have the value of 1.
        Calls hand.tostring method, answer should be [1, 2, 4, 1, 5]"""
        hand = Hand()
        self.assertListEqual(hand.to_list(), [1, 2, 4, 1, 5])


    def test_hand_roll_arg(self):
        """ Test to roll hand with argument, only dice with index should be rolled. """
        # Arrange
        # new seed value to avoid that 1 is rolled 1, compare setUp seed value
        random.seed(3)
        hand = Hand([1, 1, 1, 1, 1])

        # Act
        hand.roll([0, 1, 3])

        # Assert
        self.assertListEqual(hand.to_list(), [2, 5, 1, 5, 1])


    def test_hand_roll_no_arg(self):
        """ Test if all dices gets rerolled when no argument"""
        # Arrange
        random.seed(3)  # new seed value to avoid that 1 is rolled 1, compare setUp seed value
        hand = Hand([1, 1, 1, 1, 1])

        # Act
        hand.roll()

        # Assert
        self.assertListEqual(hand.to_list(), [2, 5, 5, 2, 3])

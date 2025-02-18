"""
Module for testing the Die class
"""

# För att kunna testa privata attribut och metoder
# pylint: disable=protected-access

import unittest
import random
from src.die import Die

class TestDie(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """Setup that runs before every testcase"""
        random.seed("startvalue") # Sets value to 1

    def test_die_no_arg(self):
        """Testing if Die argument recieves
        a random value when no argument is used for the constructor."""

        die = Die()
        self.assertEqual(die.get_value(), 1)

    def test_die_with_low_arg(self):
        """Testing if Die value is MIN_ROLL_VALUE when arg is to small."""

        die = Die(-3)
        self.assertEqual(die.get_value(), 1)

    def test_die_with_high_arg(self):
        """Testing if Die value is MAX_ROLL_VALUE when arg is to high."""

        die = Die(19)
        self.assertEqual(die.get_value(), 6)

    def test_die_new_roll(self):
        """Testing if Die.roll rolls a random value"""
        random.seed("newvalue")
        die = Die(6)
        self.assertEqual(die.roll(), 3)

    def test_die_get_name(self):
        """Test if get_name returns correct name"""

        die = Die(6)
        self.assertEqual(die.get_name(), "six")

    def test_die_false(self):
        """Test if __eq__ method in Die returns False,
        Compare Die object values"""

        die = Die(1)
        die2 = Die(2)

        self.assertEqual(die == die2, False)

    def test_die_true(self):
        """Test if __eq__ method in Die returns True,
        Compare Die object values"""

        die = Die(1)
        die2 = Die(1)

        self.assertEqual(die == die2, True)

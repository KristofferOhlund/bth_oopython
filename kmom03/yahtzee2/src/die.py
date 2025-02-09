"""
Module for representing a Dice with number 1-6.
"""

from random import randint

class Die:
    """Class representing a Dice object."""

    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6

    # Dic storing names for each value
    VALUE_NAMES = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
    }

    def __init__(self, value=None):
        self._value = value

        if not value:
            self._value = self.roll()
        else:
            if value > Die.MAX_ROLL_VALUE:
                self._value = Die.MAX_ROLL_VALUE
            elif value < Die.MIN_ROLL_VALUE:
                self._value = Die.MIN_ROLL_VALUE

    def get_name(self):
        """Returns the name of the current dice value"""
        return Die.VALUE_NAMES[self._value]

    def get_value(self):
        """Returns the current value of the dice"""
        return self._value

    def roll(self):
        """Roll a random value between MAX and MIN roll value"""
        random_number = randint(Die.MIN_ROLL_VALUE, Die.MAX_ROLL_VALUE)
        self._value = random_number
        return self._value

    def __eq__(self, other):
        """If Die or INT == other, return True, else False"""
        if isinstance(other, Die):
            return self._value == other._value
        return self._value == other


    def __str__(self):
        """Return current value of the dice as string"""
        return str(self._value)

"""Rules module for the Yahtzee game"""

from abc import ABC, abstractmethod


class Rule(ABC):
    """Abstract class"""

    @abstractmethod
    def points(self, hand):
        """Abstract method to calculate points from a hand object"""


    @staticmethod
    def same_of_a_kind(list_of_values, times):
        """Static method for finding x y times.
        If times == 3, find an equal value 3 times.
        If times == 4, find an equal value 4 times.
        If value is found equal to times, 
        return the sum of all values, else return 0"""
        min_value = 1
        max_value = 6
        limit = times

        for number in range(min_value, max_value +1):
            if list_of_values.count(number) >= limit:
                return sum(list_of_values)
        return 0


class SameValueRule(Rule):
    """Class for SameValueRule"""
    def __init__(self, value, name):
        self.value = value
        self.name = name

    def points(self, hand):
        """Returns the total points where die objects have the same value.
        as self.value.
        If 5 dices have the value of 5, return 25"""
        values = hand.to_list()
        return values.count(self.value) * self.value


class Ones(SameValueRule):
    """Class represnenting the Ones rule"""
    def __init__(self):
        super().__init__(1, "Ones")


class Twos(SameValueRule):
    """Class representing the Twos rule"""

    def __init__(self):
        super().__init__(2, "Twos")


class Threes(SameValueRule):
    """Class representing the Threes rule"""

    def __init__(self):
        super().__init__(3, "Threes")


class Fours(SameValueRule):
    """Class representing the Fours rule"""

    def __init__(self):
        super().__init__(4, "Fours")


class Fives(SameValueRule):
    """Class representing the Fives rule"""

    def __init__(self):
        super().__init__(5, "Fives")


class Sixes(SameValueRule):
    """Class representing the Sixes rule"""

    def __init__(self):
        super().__init__(6, "Sixes")


class ThreeOfAKind(Rule):
    """Class representing the rule Three of a kind"""
    def __init__(self):
        self.name = "Three Of A Kind"
        self.find_count = 3

    def points(self, hand):
        """Return the sum of all values, if 3 equal are found.
        Else return 0"""

        return Rule.same_of_a_kind(hand.to_list(), self.find_count)


class FourOfAKind(Rule):
    """Class representing the rule Three of a kind"""
    def __init__(self):
        self.name = "Four Of A Kind"
        self.find_count = 4

    def points(self, hand):
        """Return the sum of all values, if 4 equal are found.
        Else return 0"""

        return Rule.same_of_a_kind(hand.to_list(), self.find_count)


class FullHouse(Rule):
    """Class representing the Full House rule"""
    def __init__(self):
        self.name = "Full House"

    def points(self, hand):
        """Full house requires atleast 3 of the same value 
        and 2 same of another value. 
        Full House: [3, 3, 3, 2, 2]
        Not Full House: [3, 3, 3, 2, 1]"""

        values = hand.to_list()
        three_equal = False
        two_equal = False

        for value in range(1, 7):
            if values.count(value) == 3:
                three_equal = True
            if values.count(value) == 2:
                two_equal = True

        if three_equal and two_equal:
            return 25
        return 0


class SmallStraight(Rule):
    """Rule representing Small Straight"""
    def __init__(self):
        self.name = "Small Straight"


    def points(self, hand):
        """Small straight requiers atleast 4 consecutive numbers"""
        numbers = sorted(set(hand.to_list())) # remove duplicates, sort list
        consecutive_numbers = 0

        for num in range(len(numbers) -1):
            if numbers[num] + 1 == numbers[num + 1]:
                consecutive_numbers += 1

        # Length of numbers may vary,
        # Makes sure 2,3,4,5 is small straight
        # and also 1,2,3,4,6
        if consecutive_numbers >= 3:
            return 30
        return 0


class LargeStraight(Rule):
    """Class representing a Large Straight"""
    def __init__(self):
        self.name = "Large Straight"

    def points(self, hand):
        """Large straight requiers 5 consecutive numbers"""

        numbers = sorted(hand.to_list())
        consecutive_numbers = 0

        for num in range(len(numbers) - 1):
            if numbers[num] + 1 == numbers[num + 1]:
                consecutive_numbers += 1

        # Length of numbers may vary,
        # Makes sure 2,3,4,5 is small straight
        # and also 1,2,3,4,6
        if consecutive_numbers == 4:
            return 40
        return 0


class Yahtzee(Rule):
    """Class representing the rule Yahtzee"""
    def __init__(self):
        self.name = "Yahtzee"

    def points(self, hand):
        """If any number between 1-6 is found 5 times
        in hand, return 50"""

        numbers = hand.to_list()

        for number in range(1, 7):
            if numbers.count(number) == 5:
                return 50
        return 0


class Chance(Rule):
    """Class representing the Chance rule"""
    def __init__(self):
        self.name = "Chance"


    def points(self, hand):
        """Return the sum of all dice values"""
        return sum(hand.to_list())

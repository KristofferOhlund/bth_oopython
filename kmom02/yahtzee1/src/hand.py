"""
Module for creating a class holding 5 dices
"""

from src.die import Die

class Hand:
    """ Hand class for holding 5 dices """
    def __init__(self, dice_list=None):
        self.dice = dice_list  # 1, 2, 3, 4,5

        # Skapa 5 tärningar om inget argument
        if not self.dice:
            self.dice = [Die(), Die(), Die(), Die(), Die()]
        else:
            dices = []
            for int_val in dice_list:
                dices.append(Die(int_val))
            self.dice = dices

    def roll(self, indexes=None):
        """Rullar endast tärningar med index = index"""
        # Rullar alla tärningar
        if not indexes:
            for dice in self.dice:
                dice.roll()
        else:
            for i in indexes:
                self.dice[i].roll()

    def __str__(self):
        """Returnera en komma separerad sträng med värden"""
        dice_strings = []
        for dice in self.dice:
            dice_strings.append(str(dice))

        return ", ".join(dice_strings)

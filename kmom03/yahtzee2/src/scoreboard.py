"""Module for the scoreboard"""

from src import rules

class Scoreboard:
    """Scoreboard class, keeping track of rules and points."""
    def __init__(self, game_data=None):
        self._game_data = game_data
        self.rules = {
            "Ones": rules.Ones(),
            "Twos": rules.Twos(),
            "Threes": rules.Threes(),
            "Fours": rules.Fours(),
            "Fives": rules.Fives(),
            "Sixes": rules.Sixes(),
            "Three Of A Kind": rules.ThreeOfAKind(),
            "Four Of A Kind": rules.FourOfAKind(),
            "Full House": rules.FullHouse(),
            "Small Straight": rules.SmallStraight(),
            "Large Straight": rules.LargeStraight(),
            "Yahtzee": rules.Yahtzee(),
            "Chance": rules.Chance(),
        }

        # Create default value for game_data
        if not self._game_data:
            self.game_data = {
                    "Ones": -1,
                    "Twos": -1,
                    "Threes": -1,
                    "Fours": -1,
                    "Fives": -1,
                    "Sixes": -1,
                    "Three Of A Kind": -1,
                    "Four Of A Kind": -1,
                    "Full House": -1,
                    "Small Straight": -1,
                    "Large Straight": -1,
                    "Yahtzee": -1,
                    "Chance": 55,
                }


    def get_total_points(self):
        """Return total points from ScoreBoard as int"""
        points = 0
        for score in self._game_data.values():
            if score != -1:
                points += score
        return points


    def add_points(self, rule_name, hand):
        """Add points for rule_name"""
        if self._game_data[rule_name] == -1:
            self._game_data[rule_name] = self.rules[rule_name].points(hand)
        else:
            raise ValueError(f"{rule_name} has been used!")


    def get_points(self, rule_name):
        """Return points from rule = rule_name
        Example: returns points from the rule 'Ones'."""
        return self._game_data[rule_name]


    def finished(self):
        """Game has finished, returns Bool"""
        if -1 not in self._game_data.values():
            return True
        return False


    @classmethod
    def from_dict(cls, score_board_dict):
        """Classmethod to create a ScoreBoard with points from score_board_dict"""
        return cls(score_board_dict)

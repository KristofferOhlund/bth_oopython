""" Manager module """

from src.scoreboard import Scoreboard


class Manager:
    """ Manager to store player objects.
     Each players is represented by a dictionary:

    {"player": player,
    "hand": Hand().to_list(),
    "scoreboard": Scoreboard().game_data,
    "rolls": 0 }
    
    """
    def __init__(self, data = None):
        self._players = data or []
        self._winner = None


    def update_key_on_index(self, index, key, value):
        """ Replace a key in index with new value. """
        self._players[index][key] = value


    def replace_obj_at_index(self, index, obj):
        """ replace an object at index, with new object """
        self._players[index] = obj


    def get_player(self, index):
        """ Return a player object. """
        return self._players[index]


    def get_winner(self):
        """ Method for calculating the winner. Returns winner object """
        max_p = 0
        for idx, obj in enumerate(self._players):
            player = Scoreboard().from_dict(obj["scoreboard"])
            if player.get_total_points() > max_p:
                max_p = player.get_total_points()
                self._winner = self._players[idx]
        return self._winner


    def all_done(self):
        """ Check if all players are done, return bool """
        for obj in self._players:
            scoreboard = Scoreboard().from_dict(obj["scoreboard"])
            if scoreboard.finished():
                continue
            return False
        return True


    def to_list(self):
        """ return a list of tuple were each tuple
         is a player object """
        tuples = []
        for player in self._players:
            tuples.append(player)
        return tuples


    @classmethod
    def from_data(cls, data):
        """ Create a manager instance from data.
        Each player represented as tuple where index 0 
        is the hand object, index 1 is the scoreboard. """
        tups = []
        for row in data:
            tups.append((row))
        return cls(tups)


    def __str__(self):
        """Returnera rader med alla spelar object """
        players = []
        for player in self._players:
            players.append(str(player))

        return "\n ".join(players)

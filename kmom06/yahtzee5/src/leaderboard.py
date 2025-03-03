"""
Leaderboard module
"""
import json
from src.unorderedlist import UnorderedList


class Leaderboard:
    """Leaderboard class"""
    def __init__(self, entries = None):
        self.entries = UnorderedList()

        if isinstance(entries, list):
            for entry in entries:
                self.entries.append(entry)

    def save(self, filename="./src/topplista.json"):
        """Save to filename"""
        prepare_json = []
        for value in range(self.entries.size()):
            points, name = self.entries.get(value)
            prepare_json.append({
                "points": points,
                "name": name
            })

        with open(filename, "w", encoding="utf-8") as writer:
            json.dump(prepare_json, writer, indent=4)


    def add_entry(self, score:int, name:str,):
        """Add entry to leaderboard"""
        self.entries.append((score, name))


    def remove_entry(self, index:int):
        """Remove entry from leaderbaord"""
        data = self.entries.get(index)
        self.entries.remove(data)


    @classmethod
    def load(cls, filename="./src/topplista.json"):
        """Loads a file from the server.
        Create and return a Leaderboard instance"""
        with open(filename, encoding="utf-8") as reader:
            json_data = json.load(reader)

        list_of_tuple = []
        if json_data:
            for value in json_data:
                list_of_tuple.append((value["points"], value["name"]))

        return cls(list_of_tuple)

"""
This module proves an interface for reading and writing json files
which track the state of the game.
"""
import os
import json
from typing import Any

from dungeon.creature import Creature


DEFAULT_PATH = "game_state.json"


class GameState():
    def __init__(self, path: str = DEFAULT_PATH):
        if os.path.exists(path):
            with open(path, "r") as f:
                saved_state = json.load(f)
        else:
            saved_state = {}
        self.creatures = [c for c in saved_state.get("creatures", [])]
        self.path = path

    def update_participants(self, participants: dict[str, Creature]):
        for creature in self.creatures:
            participant = participants.get(creature["name"])
            if participant is not None:
                participant.health = creature["health"]
                participant.mana = creature["mana"]

    def write(self, participants: dict[str, Creature]):
        game_state = {
            "creatures": [
                {
                    "name": creature.name,
                    "health": creature.health,
                    "mana": creature.mana
                } for _, creature in participants.items()
            ]
        }
        with open(self.path, "w") as f:
            json.dump(game_state, f)

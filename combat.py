import argparse
import logging
import sys

from actions import ACTIONS, get_action
from game_state import GameState
from party import PARTY
from creature import Creature
from species import get_species
from roll import roll


logging.basicConfig(level=logging.INFO, stream=sys.stdout)

NPCS = [
    Creature(
        name="human_1",
        species=get_species("human"),
    )
]
PARTICIPANTS = {creature.name: creature for creature in NPCS + PARTY}
PARSER = argparse.ArgumentParser()
PARSER.add_argument("actor", choices=PARTICIPANTS.keys())
PARSER.add_argument("action", choices=ACTIONS.keys())
PARSER.add_argument("subject", choices=PARTICIPANTS.keys())
PARSER.add_argument("details", nargs="*")


def process_action(action: str):
    action = get_action(PARSER.parse_args(action.split()), PARTICIPANTS)
    action.skill_check_and_resolve()


if __name__ == "__main__":
    game_state = GameState()
    game_state.update_participants(PARTICIPANTS)
    actions = [
        "chad melee_attack human_1",
        "chad cast_spell human_1 fire_bolt",
    ]
    for action in actions:
        process_action(action)
    game_state.write(PARTICIPANTS)

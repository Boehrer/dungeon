import argparse
import logging
import sys

from dungeon.actions import ACTIONS, get_action
from dungeon.creature import Creature
from dungeon.game_state import GameState
from dungeon.roll import roll
from dungeon.species import human, halfling, elf, goblin
from dungeon.spells.spells import fire_bolt, fire_blast, shield
from dungeon.stats import STRENGTH, DEXTERITY, MAGIC
from dungeon.weapon import get_weapon


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

PARTY = [
    Creature(
        name="chad",
        species=human,
        weapon=get_weapon("common_sword"),
    ),
    Creature(
        name="sam",
        species=halfling,
        weapon=get_weapon("common_sword"),
    ),
    Creature(
        name="ren",
        species=elf,
        weapon=get_weapon("common_sword"),
        spells=[fire_bolt]
    ),
]
from dungeon.places.entry_room import NPCS

PARTICIPANTS = {creature.name: creature for creature in PARTY + NPCS}

PARSER = argparse.ArgumentParser()
PARSER.add_argument("actor", choices=PARTICIPANTS.keys())
PARSER.add_argument("action", choices=ACTIONS.keys())
PARSER.add_argument("subject", choices=PARTICIPANTS.keys())
PARSER.add_argument("details", nargs="*")
PARSER.add_argument("--roll", type=int)


def process_action(action: str):
    args = PARSER.parse_args(action.split())
    action = get_action(args, PARTICIPANTS)
    if args.roll is None:
        skill_check = roll()
    else:
        skill_check = args.roll
    difficulty = action.get_difficulty()
    if skill_check >= difficulty:
        logger.info(f"Passed skill check {skill_check}/{difficulty}")
        action.resolve()
    else:
        logger.info(f"Failed skill check {skill_check}/{difficulty}")


if __name__ == "__main__":
    game_state = GameState()
    game_state.update(PARTICIPANTS)
    actions = [
        "ren cast goblin_1 fire_bolt other --roll 20",
    ]
    for action in actions:
        process_action(action)
        game_state.write(PARTICIPANTS)

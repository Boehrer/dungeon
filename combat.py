from argparse import ArgumentParser
import logging
import sys

from dungeon.actions import ACTIONS
from dungeon.creature import Creature
from dungeon.game_state import GameState
from dungeon.roll import roll
from dungeon.species import human, halfling, elf, goblin
from dungeon.spells.spells import fire_bolt, fire_blast, shield
from dungeon.stats import STRENGTH, DEXTERITY, MAGIC
from dungeon.weapon import get_weapon
from dungeon.party import PARTY
from dungeon.places.entry_room import NPCS


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


PARTICIPANTS = {creature.name: creature for creature in PARTY + NPCS}


def get_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("actor", choices=PARTICIPANTS.keys())
    parser.add_argument("action", choices=ACTIONS.keys())
    parser.add_argument("subject", choices=PARTICIPANTS.keys())
    parser.add_argument("details", nargs="*")
    parser.add_argument("--roll", type=int)
    return parser


if __name__ == "__main__":
    parser = get_parser()
    game_state = GameState()
    game_state.update(PARTICIPANTS)
    actions = [
        "ren cast goblin_1 fire_bolt other --roll 20",
    ]
    for action in actions:
        args = parser.parse_args(action.split())
        actor = PARTICIPANTS[args.actor]
        subject = PARTICIPANTS[args.subject]
        skill_check = args.roll
        if skill_check is None:
            skill_check = roll.roll()
        cls = ACTIONS[args.action]
        action = cls(actor=actor, subject=subject, details=args.details)
        action.attempt(roll=skill_check)
        game_state.write(PARTICIPANTS)

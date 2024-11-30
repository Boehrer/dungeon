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

PARTICIPANTS = {
    "chad": Creature(
        name="chad",
        species=human,
        weapon=get_weapon("common_sword"),
        buffs={STRENGTH: 1},
        spells=[],
    ),
    "sam": Creature(
        name="sam",
        species=halfling,
        weapon=get_weapon("common_bow"),
        buffs={DEXTERITY: 1},
        spells=[],
    ),
    "ren": Creature(
        name="ren",
        species=elf,
        weapon=get_weapon("common_staff"),
        buffs={MAGIC: 1},
        spells=[fire_bolt, shield],
    ),
    "gog": Creature(
        name="gog",
        weapon=get_weapon("common_sword"),
        species=goblin,
    ),
    "rog": Creature(
        name="rog",
        weapon=get_weapon("common_sword"),
        species=goblin,
    ),
}
PARSER = argparse.ArgumentParser()
PARSER.add_argument("actor", choices=PARTICIPANTS.keys())
PARSER.add_argument("action", choices=ACTIONS.keys())
PARSER.add_argument("subject", choices=PARTICIPANTS.keys())
PARSER.add_argument("details", nargs="*")


def process_action(action: str):
    action = get_action(PARSER.parse_args(action.split()), PARTICIPANTS)
    skill_check = roll()
    if skill_check >= action.get_difficulty():
        logger.info("passed skill check")
        action.resolve()
    else:
        logger.info("failed skill check")


if __name__ == "__main__":
    game_state = GameState()
    game_state.update(PARTICIPANTS)
    actions = [
        "chad melee_attack gog",
        "ren cast_spell chad shield",
        "sam ranged_attack gog",
        "gog melee_attack chad",
        "rog melee_attack chad"
    ]
    for action in actions:
        process_action(action)
    game_state.write(PARTICIPANTS)

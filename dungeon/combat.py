import argparse
import logging
import sys

from dungeon.actions import ACTIONS, get_action
from dungeon.buff import Buff
from dungeon.creature import Creature
from dungeon.game_state import GameState
from dungeon.roll import roll
from dungeon.species import get_species
from dungeon.spells.spells import fire_bolt, shield
from dungeon.stats import STRENGTH
from dungeon.weapon import get_weapon


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

PARTICIPANTS = {
    "chad": Creature(
        name="chad",
        species=get_species("human"),
        weapon=get_weapon("common_sword"),
        buffs={STRENGTH: 1},
        spells=[
            fire_bolt,
            shield
        ]
    ),
    "human_1": Creature(
        name="human_1",
        species=get_species("human"),
    ),
    "human_2": Creature(
        name="human_2",
        species=get_species("human"),
    )
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
    game_state.update_participants(PARTICIPANTS)
    actions = [
        "chad melee_attack human_1",
        "chad cast_spell chad shield",
        "human_1 melee_attack chad",
        "human_1 melee_attack chad",
    ]
    for action in actions:
        process_action(action)
    game_state.write(PARTICIPANTS)

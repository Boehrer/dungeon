import argparse
import logging
import sys

from creature import Creature
from weapons import MELEE, RANGED, MAGIC as MAGIC_DAMAGE_TYPE
from roll import roll

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


class Action:
    def __init__(self, actor: Creature, subject: Creature):
        self.actor = actor
        self.subject = subject

    def get_difficulty(self):
        return 10

    def skill_check_and_resolve(self):
        skill_check = roll()
        logger.info(f"rolled {skill_check}")
        if skill_check >= self.get_difficulty():
            logger.info("passed skill check")
            self.resolve()
        else:
            logger.info("failed skill check")

    def resolve(self):
        raise NotImplementedError

    @classmethod
    def from_parsed_args(cls, args: argparse.Namespace, participants: dict[str, Creature]):
        actor = participants[args.actor]
        subject = participants[args.subject]
        return cls(actor=actor, subject=subject)


class MeleeAttack(Action):
    def resolve(self):
        damage = self.actor.get_damage(damage_type=MELEE)
        self.subject.apply_damage(damage)
        logger.info(f"{self.actor.name} attacked {self.subject.name} for {damage} HP")


ACTIONS = {
    "melee_attack": MeleeAttack
}


def get_action(args: argparse.Namespace, participants: dict[str, Creature]) -> Action:
    cls = ACTIONS[args.action]
    return cls.from_parsed_args(args, participants)

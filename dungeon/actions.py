import argparse
import logging
import sys

from dungeon.creature import Creature
from dungeon.effect import Damage
from dungeon.weapons import MELEE, RANGED, MAGIC as MAGIC_DAMAGE_TYPE

logger = logging.getLogger(__name__)


class Action:
    def __init__(self, actor: Creature, subject: Creature, details: list[str]):
        self.actor = actor
        self.subject = subject
        self.details = details
        self.validate()

    def get_difficulty(self):
        return 1

    def resolve(self):
        raise NotImplementedError

    def validate(self):
        if not self.actor.is_alive():
            raise ValueError("The dead can't perform an action")

    @classmethod
    def from_parsed_args(
        cls, args: argparse.Namespace, participants: dict[str, Creature]
    ):
        actor = participants[args.actor]
        subject = participants[args.subject]
        return cls(actor=actor, subject=subject, details=args.details)


class MeleeAttack(Action):
    damage_type = MELEE

    def resolve(self):
        amplitude = self.actor.get_damage(damage_type=self.damage_type)
        damage_effect = Damage(
            amplitude=amplitude,
        )
        logger.info(
            f"{self.actor.name} attacked {self.subject.name} with {self.damage_type}"
        )
        self.subject.add_effect(damage_effect)


class RangedAttack(MeleeAttack):
    damage_type = RANGED

    def validate(self):
        super().validate()
        if self.actor.weapon is None or self.actor.weapon.damage_type != RANGED:
            raise ValueError(
                f"{self.actor.name} attempted a ranged attack without a ranged weapon"
            )


class CastSpell(Action):
    def resolve(self):
        spell_name = self.details[0]
        spell = self.actor.cast(spell_name)
        logger.info(
            f"{self.actor.name} cast {spell_name} on {self.subject.name}"
        )
        spell.apply(self.subject)

    def validate(self):
        super().validate()
        spell_name = self.details[0]
        spell = self.actor.get_spell(spell_name)
        if spell is None:
            raise ValueError(f"Actor does not have the spell {spell_name}")
        if self.actor.mana < spell.cost:
            raise ValueError(
                "Spell requires {spell.cost} mana, but actor only has {self.actor.mana}"
            )


ACTIONS = {
    "melee_attack": MeleeAttack,
    "ranged_attack": RangedAttack,
    "cast_spell": CastSpell,
}


def get_action(
    args: argparse.Namespace, participants: dict[str, Creature]
) -> Action:
    cls = ACTIONS[args.action]
    return cls.from_parsed_args(args, participants)

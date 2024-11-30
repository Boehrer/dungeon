from dungeon.creature import Creature
from dungeon.spells.spell import Spell
from dungeon.effect import MagicShield as MagicShieldEffect, Shield as ShieldEffect


class Shield(Spell):
    def apply(self, subject: Creature):
        shield_effect = ShieldEffect(
            amplitude=self.amplitude,
        )
        subject.add_effect(shield_effect)


class MagicShield(Spell):
    def apply(self, subject: Creature):
        shield_effect = MagicShieldEffect(
            amplitude=self.amplitude,
        )
        subject.add_effect(shield_effect)

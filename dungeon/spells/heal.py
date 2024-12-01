from dungeon.creature import Creature
from dungeon.spells.spell import Spell
from dungeon.effect import Heal as HealEffect


class Heal(Spell):
    def apply(self, subject: Creature):
        heal_effect = HealEffect(
            amplitude=self.amplitude,
        )
        subject.add_effect(heal_effect)

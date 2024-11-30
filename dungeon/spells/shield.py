from dungeon.creature import Creature
from dungeon.spells.spell import Spell
from dungeon.effect import Shield as ShieldEffect


class Shield(Spell):
    def apply(self, subject: Creature):
        shield_effect = ShieldEffect(
            amplitude=self.amplitude,
        )
        subject.add_effect(shield_effect)

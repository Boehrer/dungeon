from dungeon.creature import Creature
from dungeon.spell import Spell
from dungeon.effect import Damage


class FireSpell(Spell):
    def apply(self, subject: Creature):
        damage_effect = Damage(
            amplitude=self.amplitude,
            duration=0,
        )
        subject.add_effect(damage_effect)

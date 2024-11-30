import logging
from typing import Self

logger = logging.getLogger(__name__)


class Effect:
    persist: bool

    def __init__(self, amplitude: int):
        self.amplitude = amplitude
        self.validate()

    def affect(self, effect: Self) -> Self:
        """
        affect other effects
        """
        return effect

    def apply(self, subject: "Creature"):
        """
        affects the subject
        """
        pass

    def validate(self):
        pass


class Damage(Effect):
    persist = False

    def apply(self, subject: "Creature"):
        subject.health -= self.amplitude
        logger.info(f"{subject.name} took {self.amplitude} damage")

    def validate(self):
        if self.amplitude <= 0:
            raise ValueError("damage amplitude must be positive")


class MagicDamage(Damage):
    pass


class Shield(Effect):
    persist = True

    def can_block(self, damage: Effect) -> bool:
        return isinstance(damage, Damage)

    def affect(self, effect: Self) -> Self:
        if self.can_block(effect):
            original_damage = effect.amplitude
            effect.amplitude = max(original_damage - self.amplitude, 0)
            self.amplitude -= original_damage
            if self.amplitude <= 0:
                self.persist = False
        return effect

    def validate(self):
        if self.amplitude <= 0:
            raise ValueError("shield amplitude must be positive")

class MagicShield(Shield):
    def can_block(self, damage: Effect) -> bool:
        return isinstance(damage, MagicDamage)

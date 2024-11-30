import logging
from typing import Self

logger = logging.getLogger(__name__)


class Effect:
    def __init__(self, amplitude: int, duration: int):
        self.duration = duration
        self.amplitude = amplitude
        self.pop = False
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
    def apply(self, subject: "Creature"):
        subject.health -= self.amplitude
        logger.info(f"{subject.name} took {self.amplitude} damage")

    def validate(self):
        if self.amplitude <= 0:
            raise ValueError("damage amplitude must be positive")


class Shield(Effect):
    def affect(self, effect: Self) -> Self:
        if isinstance(effect, Damage):
            original_damage = effect.amplitude
            effect.amplitude = max(original_damage - self.amplitude, 0)
            self.amplitude -= original_damage
            if self.amplitude <= 0:
                self.pop = True
        return effect

    def validate(self):
        if self.amplitude <= 0:
            raise ValueError("shield amplitude must be positive")

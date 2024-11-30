import logging
from typing import Self

logger = logging.getLogger(__name__)


class Effect:
    def __init__(self, amplitude: int, duration: int):
        self.duration = duration
        self.amplitude = amplitude

    def affect(self, effect: Self) -> Self:
        """
        Affect other effects
        """
        return effect

    def apply(self, subject: "Creature"):
        raise NotImplementedError


class Damage(Effect):
    def apply(self, subject: "Creature"):
        subject.health -= self.amplitude
        logger.info(f"{subject.name} took {self.amplitude} damage")

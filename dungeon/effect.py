import logging
from typing import Self

logger = logging.getLogger(__name__)


registry = {}


def register_class(cls):
    registry[cls.__name__] = cls
    return cls


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

    def to_json(self):
        return {"amplitude": self.amplitude, "class": self.__class__.__name__}

    @classmethod
    def from_json(cls, data: dict):
        return registry[data["class"]](amplitude=data["amplitude"])


@register_class
class Damage(Effect):
    persist = False

    def apply(self, subject: "Creature"):
        subject.health -= self.amplitude
        logger.info(f"{subject.name} took {self.amplitude} damage ({subject.health}/{subject.max_health})")

    def validate(self):
        if self.amplitude <= 0:
            raise ValueError("damage amplitude must be positive")


@register_class
class MagicDamage(Damage):
    pass


@register_class
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


@register_class
class MagicShield(Shield):
    def can_block(self, damage: Effect) -> bool:
        return isinstance(damage, MagicDamage)


@register_class
class Heal(Effect):
    persist = False

    def apply(self, subject: "Creature"):
        healing = min(subject.max_health - subject.health, self.amplitude)
        subject.health += healing
        logger.info(f"{subject.name} healed for {healing} HP ({subject.health}/{subject.max_health})")

    def validate(self):
        if self.amplitude <= 0:
            raise ValueError("heal amplitude must be positive")

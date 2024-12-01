from unittest.mock import Mock

from dungeon.potions.potion import Potion


def test_potion(creature):
    """
    When a creature drinks a potion the potion's effect should be added to
    the creature
    """
    effect = Mock()
    potion = Potion(effect=effect)
    potion.drink(creature)
    assert effect in creature.effects
    effect.apply.assert_called_once()

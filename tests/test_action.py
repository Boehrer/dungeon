import pytest
from unittest.mock import Mock

from dungeon.actions import Action, MeleeAttack, RangedAttack, CastSpell
from dungeon.creature import Creature
from dungeon.species import human
from dungeon.spells.spells import fire_bolt
from dungeon.weapon import Weapon
from dungeon.weapons import MELEE, RANGED, MAGIC


@pytest.fixture
def other_creature():
    return Creature(
        name="other_creature",
        species=human,
    )


def test_get_difficulty(creature, other_creature):
    """
    difficulty should default to 10
    """
    action = Action(actor=creature, subject=other_creature, details=[])
    assert action.get_difficulty() == 10


def test_validate(creature, other_creature):
    """
    dead creatures should not be able to act
    """
    creature.health = 0
    assert not creature.is_alive()
    with pytest.raises(ValueError):
        Action(actor=creature, subject=other_creature, details=[])


def test_melee_attack(creature, other_creature):
    """
    resolving a melee attack should reduce subjects health by an expected
    amount
    """
    action = MeleeAttack(creature, other_creature, [])
    initial_health = other_creature.health
    action.resolve()
    assert initial_health - creature.get_damage(MELEE) == other_creature.health


def test_ranged_attack(creature, other_creature):
    """
    A value error should be raised if RangedAttack is instantiating with an
    actor without a ranged weapon resolving a ranged attack should reduce
    subjects health by an expected amount
    """
    with pytest.raises(ValueError):
        action = RangedAttack(creature, other_creature, [])
    creature.weapon = Weapon("", 0, RANGED)
    action = RangedAttack(creature, other_creature, [])
    initial_health = other_creature.health
    action.resolve()
    assert (
        initial_health - creature.get_damage(RANGED) == other_creature.health
    )


def test_cast_spell(creature, other_creature):
    """
    errors should be raised if the given spell cannot be cast for some reason,
    otherwise the spell should be applied to the subject
    """
    with pytest.raises(IndexError):
        action = CastSpell(creature, other_creature, details=[])
    with pytest.raises(ValueError):
        action = CastSpell(creature, other_creature, details=["fire_bolt"])
    creature.spells = [fire_bolt]
    creature.mana = 0
    with pytest.raises(ValueError):
        action = CastSpell(creature, other_creature, details=["fire_bolt"])
    creature.mana = 1
    action = CastSpell(creature, other_creature, details=["fire_bolt"])
    fire_bolt.apply = Mock()
    action.resolve()
    fire_bolt.apply.assert_called_once()
    fire_bolt.apply.assert_called_with(other_creature)

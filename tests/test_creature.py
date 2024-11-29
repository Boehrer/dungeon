import pytest

from dungeon.creature import Creature
from dungeon.species import get_species
from dungeon.spells import fire_bolt
from dungeon.stats import STRENGTH, DEXTERITY, MAGIC as MAGIC_STAT
from dungeon.weapon import Weapon
from dungeon.weapons import MELEE, RANGED, MAGIC as MAGIC_DAMAGE_TYPE


@pytest.fixture
def creature():
    return Creature(
        name="human",
        species=get_species("human"),
    )


def test_get_damage(creature):
    """
    melee damage should scale with strength,
    ranged damage should scale with dexterity,
    magic damage should scale with magic,
    weapons should increase a creature's
    damage of the weapon's damage type.
    """
    assert creature.get_damage(MELEE) == creature.stats[STRENGTH]
    assert creature.get_damage(RANGED) == creature.stats[DEXTERITY]
    assert creature.get_damage(MAGIC_DAMAGE_TYPE) == creature.stats[MAGIC_STAT]
    weapon = Weapon(
        name="melee_weapon",
        damage=1,
        damage_type=MELEE
    )
    creature.weapon = weapon
    assert creature.get_damage(MELEE) == creature.stats[STRENGTH] + weapon.damage
    assert creature.get_damage(RANGED) == creature.stats[DEXTERITY]
    assert creature.get_damage(MAGIC_DAMAGE_TYPE) == creature.stats[MAGIC_STAT]


def test_apply_damage(creature):
    """
    apply damage should reduce the health of creatures
    """
    initial_health = creature.health
    damage = 1
    creature.apply_damage(damage, MELEE)
    assert creature.health == initial_health - damage


def test_is_alive(creature):
    """
    if a creature has 0 or less health it should be dead
    """
    creature.health = 1
    assert creature.is_alive()
    creature.health = 0
    assert not creature.is_alive()
    creature.health = -1
    assert not creature.is_alive()


def test_get_spells(creature):
    """
    get spells should return None if the creature does not have the
    specified spell. It should return the specified spell if it has
    it.
    """
    assert creature.get_spell("fire_bolt") is None
    creature.spells = [fire_bolt]
    assert creature.get_spell("fire_bolt") == fire_bolt


def test_cast(creature):
    """
    casting a spell should fail if the creature does not have the spell,
    casting a spell should fail if the spells cost exceeds the creature's mana,
    casting a spell should reduce the creatures mana, the spell which was cast
    should be returned.
    """
    with pytest.raises(ValueError):
        creature.cast("fire_bolt")
    creature.spells = [fire_bolt]
    creature.mana = 0
    with pytest.raises(ValueError):
        creature.cast("fire_bolt")
    creature.mana = 1
    spell = creature.cast("fire_bolt")
    assert spell == fire_bolt
    assert creature.mana == 0

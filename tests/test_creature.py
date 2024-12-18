import copy
import pytest
from unittest.mock import Mock

from dungeon.creature import Creature
from dungeon.effect import Effect
from dungeon.species import human
from dungeon.spells.spells import fire_bolt
from dungeon.stats import STRENGTH, DEXTERITY, MAGIC as MAGIC_STAT
from dungeon.weapon import Weapon
from dungeon.weapons import MELEE, RANGED, MAGIC as MAGIC_DAMAGE_TYPE


def test_stats():
    buffs = {STRENGTH: 1, DEXTERITY: 2, MAGIC_STAT: 3}
    creature = Creature(
        name="test_creature",
        species=human,
        buffs=buffs,
    )
    for stat in [STRENGTH, DEXTERITY, MAGIC_STAT]:
        assert creature.stats[stat] == human.base_stats[stat] + buffs[stat]


def test_add_effect(creature):
    """
    effects should be passed to effect.affect for each pre-existing effect,
    effects with persist=True should persist,
    effects with persist=False should not persist,
    effect.apply should be called at the end of add_effect
    """
    mocked_effect = Mock()
    mocked_effect.affect.side_effect = lambda x: x
    pre_existing_effects = [mocked_effect, copy.deepcopy(mocked_effect)]
    creature.effects = pre_existing_effects
    effect = Mock()
    effect.persist = False
    creature.add_effect(effect)
    pre_existing_effects[0].affect.assert_called_once()
    pre_existing_effects[0].affect.assert_called_with(effect)
    pre_existing_effects[1].affect.assert_called_once()
    pre_existing_effects[1].affect.assert_called_with(effect)
    effect.apply.assert_called_once()
    assert effect not in creature.effects
    effect.persist = True
    creature.add_effect(effect)
    assert effect in creature.effects


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

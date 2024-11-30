from dungeon.effect import Damage, MagicDamage, MagicShield, Shield


def test_damage(creature):
    """
    The damage effect should reduce a creatures health when applied
    """
    amplitude = 2
    effect = Damage(amplitude=amplitude)
    initial_health = creature.health
    effect.apply(creature)
    assert creature.health == initial_health - amplitude


def test_shield(creature):
    """
    * shields should reduce the next damage effect
    * shields should not persist after being depleted
    * shields should persist until they have been ued up completely
    * shields should not trigger healing if the shield value exceeds incoming
        damage
    """
    shield_amplitude = 1
    shield = Shield(amplitude=shield_amplitude)
    creature.add_effect(shield)
    damage_amplitude = 2
    damage = Damage(amplitude=damage_amplitude)
    creature.add_effect(damage)
    assert creature.health == creature.max_health - damage_amplitude + shield_amplitude
    assert len(creature.effects) == 0
    initial_health = creature.health
    shield_amplitude = 2
    shield = Shield(amplitude=shield_amplitude)
    creature.add_effect(shield)
    damage_amplitude = 1
    damage = Damage(amplitude=damage_amplitude)
    creature.add_effect(damage)
    assert shield.amplitude == shield_amplitude - damage_amplitude
    assert shield in creature.effects
    assert creature.health == initial_health


def test_magic_shield(creature):
    """
    * magic shields should only block magic damage
    """
    shield_amplitude = 1
    shield = MagicShield(amplitude=shield_amplitude)
    creature.add_effect(shield)
    damage_amplitude = 2
    damage = Damage(amplitude=damage_amplitude)
    creature.add_effect(damage)
    assert creature.health == creature.max_health - damage_amplitude
    damage = MagicDamage(amplitude=damage_amplitude)
    creature.health = creature.max_health
    creature.add_effect(damage)
    assert creature.health == creature.max_health - damage_amplitude + shield_amplitude

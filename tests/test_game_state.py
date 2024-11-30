from dungeon.creature import Creature
from dungeon.game_state import GameState
from dungeon.species import human
from dungeon.effect import Shield

def test_write_and_update(tmp_path):
    tmp_file = tmp_path / "test"
    game_state = GameState(path=tmp_file)
    effect = Shield(amplitude=2)
    creature = Creature(
        name="creature",
        effects=[effect],
        species=human,
    )
    creature.health = 1
    creature.mana = 1
    game_state.write({"creature": creature})
    game_state = GameState(path=tmp_file)
    creature = Creature(
        name="creature",
        species=human,
    )
    participants = {"creature": creature}
    assert creature.health != 1
    assert creature.mana != 1
    game_state.update(participants)
    assert creature.health == 1
    assert creature.mana == 1
    assert len(creature.effects) == 1
    effect = creature.effects[0]
    assert isinstance(effect, Shield)
    assert effect.amplitude == effect.amplitude

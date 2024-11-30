from dungeon.spells.fire import Fire
from dungeon.spells.shield import Shield
from dungeon.spells.heal import Heal


fire_bolt = Fire(
    name="fire_bolt",
    cost=1,
    amplitude=1,
)
fire_blast = Fire(
    name="fire_blast",
    cost=2,
    amplitude=2,
)
fire_beam = Fire(
    name="fire_beam",
    cost=3,
    amplitude=3,
)
shield = Shield(name="shield", cost=1, amplitude=1)
heal = Heal(name="heal", cost=2, amplitude=1)
all_spells = [fire_bolt, fire_blast, fire_beam, shield, heal]

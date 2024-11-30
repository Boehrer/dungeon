from dungeon.buff import Buff
from dungeon.creature import Creature
from dungeon.species import get_species
from dungeon.weapon import get_weapon
from dungeon.stats import STRENGTH
from dungeon.spells.spells import fire_bolt


CHAD = Creature(
    name="chad",
    species=get_species("human"),
    weapon=get_weapon("common_sword"),
    buffs=[
        Buff(STRENGTH, memo="first_buff")
    ],
    spells=[
        fire_bolt,
    ]
)
PARTY = [
    CHAD
]

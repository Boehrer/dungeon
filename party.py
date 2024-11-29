from buff import Buff
from creature import Creature
from species import get_species
from weapon import get_weapon
from stats import STRENGTH
from spells import fire_bolt


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

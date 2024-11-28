from buff import Buff
from creature import Creature
from species import get_species
from weapon import get_weapon
from spell import get_spell
from stats import STRENGTH


CHAD = Creature(
    name="chad",
    species=get_species("human"),
    weapon=get_weapon("common_sword"),
    buffs=[
        Buff(STRENGTH, memo="first_buff")
    ],
    spells=[
        get_spell("magic_shield")
    ]
)
PARTY = [
    CHAD
]

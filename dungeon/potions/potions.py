from dungeon.effect import Renew, Heal
from dungeon.potions.potion import Potion


small_health_pot = Potion(
    effect=Heal(amplitude=1)
)
medium_health_pot = Potion(
    effect=Heal(amplitude=2)
)
large_health_pot = Potion(
    effect=Heal(amplitude=3)
)
small_mana_pot = Potion(
    effect=Heal(amplitude=1)
)
medium_mana_pot = Potion(
    effect=Heal(amplitude=2)
)
large_mana_pot = Potion(
    effect=Heal(amplitude=3)
)

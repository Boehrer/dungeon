from dungeon.effect import Effect
from dungeon.creature import Creature


class Potion:
    def __init__(self, effect: Effect):
        self.effect = effect


    def drink(self, creature: Creature) -> Effect:
        creature.add_effect(self.effect)

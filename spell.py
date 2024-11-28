from spells import SPELLS


class Spell:
    def __init__(
        self,
        name: str,
        cost: int,
        range_: str,
        effect: str,
        amplitude: int
    ):
        self.name = name
        self.cost = cost
        self.range = range_
        self.effect = effect
        self.amplitude = amplitude


def get_spell(name: str) -> Spell:
    spell_dict = SPELLS[name]
    return Spell(
        name=name,
        cost=spell_dict["cost"],
        range_=spell_dict["range"],
        effect=spell_dict["effect"],
        amplitude=spell_dict["amplitude"]
    )

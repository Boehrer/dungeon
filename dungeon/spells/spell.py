class Spell:
    def __init__(
        self,
        name: str,
        cost: int,
        amplitude: int
    ):
        self.name = name
        self.cost = cost
        self.amplitude = amplitude

    def apply(self):
        raise NotImplementedError

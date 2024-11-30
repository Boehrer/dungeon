import pytest

from dungeon.creature import Creature
from dungeon.species import human


@pytest.fixture
def creature():
    return Creature(
        name="creature",
        species=human,
    )

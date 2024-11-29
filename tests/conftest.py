import pytest

from dungeon.creature import Creature
from dungeon.species import get_species


@pytest.fixture
def creature():
    return Creature(
        name="creature",
        species=get_species("human"),
    )

from dungeon.spells.spells import all_spells


def test_spells(creature):
    for spell in all_spells:
        spell.apply(creature)

FAR = 3
NEAR = 2
CLOSE = 1
SPELLS_THAT_COUNTER_MAGIC = {
    "magic_shield": {
        "cost": 1,
        "range": NEAR,
        "effect": "magic_shield",
        "amplitude": 1,
    },
    "magic_barrier": {
        "cost": 2,
        "range": NEAR,
        "effect": "magic_shield",
        "amplitude": 2,
    },
    "counter_spell": {
        "cost": 3,
        "range": FAR,
        "effect": "counter_spell",
        "amplitude": 1
    },
}
SPELLS_THAT_COUNTER_DAMAGE = {
    "shield": {
        "cost": 2,
        "range": NEAR,
        "effect": "shield",
        "amplitude": 1,
    },
}
SPELLS_THAT_DEAL_DAMAGE = {
    "fire_bolt": {
        "cost": 1,
        "range": FAR,
        "effect": "magic_damage",
        "amplitude": 1
    },
    "fire_blast": {
        "cost": 2,
        "range": FAR,
        "effect": "magic_damage",
        "amplitude": 2
    },
    "fire_beam": {
        "cost": 3,
        "range": FAR,
        "effect": "magic_damage",
        "amplitude": 3
    },

}
SPELLS = {
    **SPELLS_THAT_COUNTER_MAGIC,
    **SPELLS_THAT_COUNTER_DAMAGE,
    **SPELLS_THAT_DEAL_DAMAGE
}

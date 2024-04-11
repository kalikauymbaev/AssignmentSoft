class Character:
    def __init__(self, name, class_type, weapon, health, mana):
        self.name = name
        self.class_type = class_type
        self.weapon = weapon
        self.health = health
        self.mana = mana

class Weapon:
    def __init__(self, type, damage, speed, range):
        self.type = type
        self.damage = damage
        self.speed = speed
        self.range = range

import CharacterFactory
import Character

class WarriorFactory(CharacterFactory):
    def createCharacter(self, name):
        # Assuming predefined abilities, attributes, and equipment for simplicity
        abilities = [{"name": "Slash", "damage": 10}]
        equipment = [{"name": "Sword", "attack_bonus": 5}]
        attributes = {"strength": 10, "dexterity": 5}
        appearance = {"hair": "short", "armor": "heavy"}
        return Character(name, appearance, abilities, equipment, attributes)

class MageFactory(CharacterFactory):
    def createCharacter(self, name):
        abilities = [{"name": "Fireball", "damage": 15}]
        equipment = [{"name": "Magic Wand", "magic_bonus": 5}]
        attributes = {"intelligence": 10, "wisdom": 5}
        appearance = {"hair": "long", "robe": "enchanted"}
        return Character(name, appearance, abilities, equipment, attributes)

class ArcherFactory(CharacterFactory):
    def createCharacter(self, name):
        abilities = [{"name": "Arrow Shot", "damage": 12}]
        equipment = [{"name": "Bow", "range_bonus": 5}]
        attributes = {"dexterity": 10, "agility": 5}
        appearance = {"hair": "ponytail", "armor": "light"}
        return Character(name, appearance, abilities, equipment, attributes)

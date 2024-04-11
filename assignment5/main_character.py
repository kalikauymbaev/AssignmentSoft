import CharactersCreator
from ChFactories import WarriorSwordFactory
from ChFactories import MageStaffFactory

def main():
    character_creator = CharactersCreator()

    # Create a Warrior with a Sword
    character_creator.setFactory(WarriorSwordFactory())
    warrior = character_creator.createCharacter("Aragorn")
    print(f"Created {warrior.class_type} named {warrior.name} with a {warrior.weapon.type}")

    # Create a Mage with a Staff
    character_creator.setFactory(MageStaffFactory())
    mage = character_creator.createCharacter("Gandalf")
    print(f"Created {mage.class_type} named {mage.name} with a {mage.weapon.type}")

    # Similarly, create an Archer with a Bow

if __name__ == "__main__":
    main()
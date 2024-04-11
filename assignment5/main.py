import CharacterCreator
from Factory import WarriorFactory
from Factory import MageFactory
from Factory import ArcherFactory

def main():
    creator = CharacterCreator()
    
    # Create a warrior
    creator.setFactory(WarriorFactory())
    warrior = creator.createCharacter("Aragorn")
    print("Warrior created:", vars(warrior))
    
    # Create a mage
    creator.setFactory(MageFactory())
    mage = creator.createCharacter("Gandalf")
    print("Mage created:", vars(mage))
    
    # Create an archer
    creator.setFactory(ArcherFactory())
    archer = creator.createCharacter("Legolas")
    print("Archer created:", vars(archer))

if __name__ == "__main__":
    main()

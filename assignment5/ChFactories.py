from Characters import Character
from Characters import Weapon
import CharactersFactory

class WarriorSwordFactory(CharactersFactory):
    def createCharacter(self, name):
        return Character(name, "Warrior", self.createWeapon(), 100, 0)

    def createWeapon(self):
        return Weapon("Sword", 10, 5, 1)

class MageStaffFactory(CharactersFactory):
    def createCharacter(self, name):
        return Character(name, "Mage", self.createWeapon(), 70, 100)

    def createWeapon(self):
        return Weapon("Staff", 5, 3, 3)

class ArcherBowFactory(CharactersFactory):
    def createCharacter(self, name):
        return Character(name, "Archer", self.createWeapon(), 80, 50)

    def createWeapon(self):
        return Weapon("Bow", 8, 7, 5)

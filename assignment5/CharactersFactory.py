from abc import ABC, abstractmethod

class CharactersFactory(ABC):
    @abstractmethod
    def createCharacter(self, name):
        pass

    @abstractmethod
    def createWeapon(self):
        pass
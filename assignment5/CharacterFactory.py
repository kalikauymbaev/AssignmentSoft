from abc import ABC, abstractmethod

class CharacterFactory(ABC):
    @abstractmethod
    def createCharacter(self, name):
        pass

from abc import ABC, abstractmethod

class FurnitureFactory(ABC):
    @abstractmethod
    def createChair(self):
        pass

    @abstractmethod
    def createTable(self):
        pass

    @abstractmethod
    def createSofa(self):
        pass
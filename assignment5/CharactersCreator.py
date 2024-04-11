class CharactersCreator:
    def __init__(self, factory=None):
        self.factory = factory

    def setFactory(self, factory):
        self.factory = factory

    def createCharacter(self, name):
        if not self.factory:
            raise ValueError("Character factory not set")
        return self.factory.createCharacter(name)

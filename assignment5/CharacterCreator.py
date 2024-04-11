class CharacterCreator:
    def __init__(self):
        self.factory = None
    
    def setFactory(self, factory):
        self.factory = factory
    
    def createCharacter(self, name):
        if not self.factory:
            raise ValueError("No factory set for character creation")
        return self.factory.createCharacter(name)

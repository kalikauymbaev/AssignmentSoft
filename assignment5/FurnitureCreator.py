class FurnitureCreator:
    def __init__(self, factory):
        self.factory = factory
    
    def createChair(self):
        return self.factory.createChair()
    
    def createTable(self):
        return self.factory.createTable()
    
    def createSofa(self):
        return self.factory.createSofa()

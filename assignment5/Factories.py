import FurnitureFactory
import Furniture

class ModernWoodFactory(FurnitureFactory):
    def createChair(self):
        return Furniture("Modern Chair", "Modern", "Wood", 120.0)
    
    def createTable(self):
        return Furniture("Modern Table", "Modern", "Wood", 220.0)
    
    def createSofa(self):
        return Furniture("Modern Sofa", "Modern", "Wood", 320.0)

class TraditionalMetalFactory(FurnitureFactory):
    def createChair(self):
        return Furniture("Traditional Chair", "Traditional", "Metal", 150.0)
    
    def createTable(self):
        return Furniture("Traditional Table", "Traditional", "Metal", 250.0)
    
    def createSofa(self):
        return Furniture("Traditional Sofa", "Traditional", "Metal", 350.0)

# Additional factories like IndustrialGlassFactory can be defined similarly.

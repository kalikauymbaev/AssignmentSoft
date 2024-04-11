from Factories import ModernWoodFactory
import FurnitureCreator

def display_furniture(furniture):
    print(f"{furniture.name}: Style={furniture.style}, Material={furniture.material}, Price=${furniture.price}")

def main():
    # Create and display modern wood furniture
    modern_wood_factory = ModernWoodFactory()
    modern_wood_creator = FurnitureCreator(modern_wood_factory)
    
    chair = modern_wood_creator.createChair()
    table = modern_wood_creator.createTable()
    sofa = modern_wood_creator.createSofa()
    
    display_furniture(chair)
    display_furniture(table)
    display_furniture(sofa)

if __name__ == "__main__":
    main()

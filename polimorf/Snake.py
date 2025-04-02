# class Animal:
#     def __init__(self, species, diet):
#         self.species = species
#         self.diet = diet

#     def describe(self):
#         print(f"Rūšis: {self.species}, Mityba: {self.diet}")

# class Aquatic:
#     def __init__(self, can_swim=True):
#         self.can_swim = can_swim

#     def swim(self):
#         if self.can_swim:
#             print("Plaukimas vandenyje...")
#         else:
#             print("Nemoku plaukti.")

# class Terrestrial:
#     def __init__(self, can_walk=True):
#         self.can_walk = can_walk

#     def walk(self):
#         if self.can_walk:
#             print("Vaikštant žeme...")
#         else:
#             print("Negalima vaikščioti.")

# class ZooAnimal(Animal, Aquatic, Terrestrial):
#     def __init__(self, name, species, diet, can_swim=True, can_walk=True):
#         self.name = name

#         # Вызываем инициализацию каждого родительского класса
#         Animal.__init__(self, species, diet)
#         Aquatic.__init__(self, can_swim)
#         Terrestrial.__init__(self, can_walk)

#     def zoo_info(self):
#         print(f"Vardas: {self.name}")
#         self.describe()  # из Animal
#         print(f"Gali plaukti: {self.can_swim}")
#         print(f"Gali vaikščioti: {self.can_walk}")

# pingvinas = ZooAnimal(
#     name="Pingu", 
#     species="Penguin", 
#     diet="Carnivore", 
#     can_swim=True, 
#     can_walk=True
# )

# gyvate = ZooAnimal(
#     name="Sly", 
#     species="Snake", 
#     diet="Carnivore", 
#     can_swim=False, 
#     can_walk=False
# )

# print("\n--- Pingvino informacija ---")
# pingvinas.zoo_info()
# pingvinas.swim()
# pingvinas.walk()

# print("\n--- Gyvatės informacija ---")
# gyvate.zoo_info()
# gyvate.swim()
# gyvate.walk()

class Animal:
    def __init__(self, species, diet):
        self.species = species
        self.diet = diet

    def describe(self):
        print(f"Species: {self.species}, Diet: {self.diet}")


class Aquatic:
    def __init__(self, can_swim=True):
        self.can_swim = can_swim

    def swim(self):
        if self.can_swim:
            print("Swimming in the water...")
        else:
            print("Cannot swim.")


class Terrestrial:
    def __init__(self, can_walk=True):
        self.can_walk = can_walk

    def walk(self):
        if self.can_walk:
            print("Walking on land...")
        else:
            print("Cannot walk.")


class ZooAnimal(Animal, Aquatic, Terrestrial):
    def __init__(self, name, species, diet, can_swim=True, can_walk=True):
        Animal.__init__(self, species, diet)
        Aquatic.__init__(self, can_swim)
        Terrestrial.__init__(self, can_walk)
        self.name = name

    def zoo_info(self):
        print(f"Name: {self.name}")
        self.describe()
        print(f"Can Swim: {'Yes' if self.can_swim else 'No'}")
        print(f"Can Walk: {'Yes' if self.can_walk else 'No'}")


# Example Usage
penguin = ZooAnimal("Penny", "Penguin", "Carnivore", can_swim=True, can_walk=True)
snake = ZooAnimal("Slither", "Snake", "Carnivore", can_swim=False, can_walk=False)

# Demonstrate abilities of the penguin
penguin.zoo_info()
penguin.swim()
penguin.walk()

# Demonstrate abilities of the snake
snake.zoo_info()
snake.swim()
snake.walk()


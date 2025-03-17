class Animal:
    def __init__(self, name, species, habitat):
        self.name = name
        self.species = species
        self.habitat = habitat

    def speak(self):
        return "Some generic animal sound"

    def move(self):
        return "Moves in some way"

    def get_info(self):
        return f"Name: {self.name}, Species: {self.species}, Habitat: {self.habitat}"


class Mammal(Animal):
    def __init__(self, name, species, habitat, has_fur, warm_blooded, diet):
        super().__init__(name, species, habitat)
        self.has_fur = has_fur
        self.warm_blooded = warm_blooded
        self.diet = diet

    def give_birth(self):
        return "Gives birth to live young"

    def mammal_info(self):
        return f"Fur: {self.has_fur}, Warm-blooded: {self.warm_blooded}, Diet: {self.diet}"


class Dog(Mammal):
    def __init__(self, name, breed, habitat, has_fur, warm_blooded, diet, bark_sound):
        super().__init__(name, "Dog", habitat, has_fur, warm_blooded, diet)
        self.breed = breed
        self.bark_sound = bark_sound
        self.loyalty_level = "High"

    def speak(self):
        return self.bark_sound

    def dog_info(self):
        return f"Breed: {self.breed}, Bark sound: {self.bark_sound}, Loyalty: {self.loyalty_level}"


# Kuriame šunų klasės objektą
my_dog = Dog(
    name="Buddy",
    breed="Golden Retriever",
    habitat="Household",
    has_fur=True,
    warm_blooded=True,
    diet="Omnivore",
    bark_sound="Woof!"
)

# Informacijos apie objektą rodymas
print(my_dog.get_info())      # Informacija apie gyvūną
print(my_dog.mammal_info())   # Informacija apie žinduolį
print(my_dog.dog_info())      # Informacija apie šunį
print(my_dog.speak())         # Woof!
print(my_dog.give_birth())    # Gives birth to live young
print(my_dog.move())          # Moves in some way
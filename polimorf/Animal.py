# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_noise(self):
#         return f"{self.name} skleidžia garsą."  # "издаёт звук"
    
# class Mammal(Animal):
#     def __init__(self, name, warm_blooded):
#         super().__init__(name)              # вызываем конструктор родителя Animal
#         self.warm_blooded = warm_blooded

#     def give_birth(self):
#         return f"{self.name} gimdo jauniklius."  # "рождает детёнышей"
    
# class Primate(Mammal):
#     def __init__(self, name, warm_blooded, opposable_thumbs):
#         super().__init__(name, warm_blooded)
#         self.opposable_thumbs = opposable_thumbs

#     def swing(self):
#         return f"{self.name} supasi ant šakų!"  # "качаетcя на ветках"

# chimpanzee = Primate("Šimpanzė", warm_blooded=True, opposable_thumbs=True)

# print(chimpanzee.make_noise())     # метод из Animal
# print(chimpanzee.give_birth())     # метод из Mammal
# print(chimpanzee.swing())          # метод из Primate

# # Проверим его атрибуты
# print("Ar šiltakraujis:", chimpanzee.warm_blooded)
# print("Ar turi nykštį:", chimpanzee.opposable_thumbs)  
# 
class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_noise(self) -> None:
        print("Some generic animal noise")


class Mammal(Animal):
    def __init__(self, name: str, warm_blooded: bool):
        super().__init__(name)
        self.warm_blooded = warm_blooded

    def give_birth(self) -> None:
        print("Giving birth to a baby mammal")


class Primate(Mammal):
    def __init__(self, name: str, warm_blooded: bool, opposable_thumbs: bool):
        super().__init__(name, warm_blooded)
        self.opposable_thumbs = opposable_thumbs

    def swing(self) -> None:
        print("Swinging through the trees")


chimpanzee = Primate("Charlie", True, True)
print(chimpanzee.name)
print(chimpanzee.warm_blooded)
print(chimpanzee.opposable_thumbs)
chimpanzee.make_noise()
chimpanzee.give_birth()
chimpanzee.swing()  
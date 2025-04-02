# class Fighter:
#     def attack(self):
#         print("Puola kardu!")  # Атака мечом

# class Mage:
#     def cast_spell(self):
#         print("Casting fireball!")  # Заклинание — огненный шар

# class Battlemage(Fighter, Mage):
#     def battle(self):
#         self.attack()        # Метод из Fighter
#         self.cast_spell()    # Метод из Mage
#         print("Battlemage in action!")  # Боевой клич

# hero = Battlemage()

# hero.battle()

class Fighter:
    def attack(self):
        print("Attacking with sword!")


class Mage:
    def cast_spell(self):
        print("Casting fireball!")


class Battlemage(Fighter, Mage):
    def battle(self):
        print("Battlemage in action!")
        self.attack()
        self.cast_spell()


# Example Usage
hero = Battlemage()
hero.battle()
# Outputs:
# Battlemage in action!
# Attacking with sword!
# Casting fireball!
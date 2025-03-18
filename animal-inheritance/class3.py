class Vehicle:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def start(self):
        return f"{self.brand} {self.model} paleidžiamas."

    def stop(self):
        return f"{self.brand} {self.model} sustoja."

    def accelerate(self):
        return f"{self.brand} {self.model} pagreitina iki {self.speed} km/val."

# Poklasis (mašina)
class Car(Vehicle):
    def __init__(self, brand, model, speed, fuel_type, doors, transmission):
        super().__init__(brand, model, speed)
        self.fuel_type = fuel_type
        self.doors = doors
        self.transmission = transmission

    def honk(self):
        return f"{self.brand} {self.model} skambina: 'Bip-bip!'"

    def car_info(self):
        return f"Kuro tipas: {self.fuel_type}, Durys: {self.doors}, transmisija: {self.transmission}"

#Poklasis (elektrinė transporto priemonė)
class ElectricCar(Car):
    def __init__(self, brand, model, speed, doors, transmission, battery_capacity, charge_time):
        super().__init__(brand, model, speed, "Electric", doors, transmission)
        self.battery_capacity = battery_capacity
        self.charge_time = charge_time
        self.eco_friendly = True

    def charge(self):
        return f"{self.brand} {self.model} kraunasi {self.charge_time} valandų."

    def electric_info(self):
        return f"Baterijos talpa: {self.battery_capacity} kWh, Ekologiškas: {self.eco_friendly}, Įkrovimo laikas: {self.charge_time} h"



#Rodoma informacija apie automobilį
my_tesla = ElectricCar("Tesla", "Model S", 250, 4, "Automatinė", 100, 1.5)
print(my_tesla.start())      # Automobilis paleidžiamas
print(my_tesla.accelerate()) # Automobilis įsibėgėja
print(my_tesla.honk())       # Mašina garsiai skamba
print(my_tesla.car_info())   # Informacija apie automobilį
print(my_tesla.electric_info())  # Informacija apie elektromobilį
print(my_tesla.charge())     # Automobilis kraunasi



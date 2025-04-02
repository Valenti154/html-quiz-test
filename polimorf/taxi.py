# class Vehicle:
#     def __init__(self, name, brand, color, capacity, number):
#         self.name = name
#         self.brand = brand
#         self.color = color
#         self.capacity = capacity
#         self.number = number

#     def describe(self):
#         return f"{self.name} - {self.brand}, spalva: {self.color}, numeris: {self.number}"

#     def ticket_price(self):
#         return self.capacity * 100

#     def start(self):
#         return f"{self.name} pajudėjo!"

#     def stop(self):
#         return f"{self.name} sustojo."

#     def honk(self):
#         return f"{self.name} pypsi!"
    
# class Bus(Vehicle):
#     def ticket_price(self):
#         base_price = super().ticket_price()  # вызываем метод из Vehicle
#         maintenance_fee = base_price * 0.10  # 10%
#         return base_price + maintenance_fee
    
# class Taxi(Vehicle):
#     pass  # Просто используем поведение Vehicle 

# class Train(Vehicle):
#     pass

# bus = Bus("Autobusas", "Mercedes", "Geltonas", 50, "BUS-123")
# taxi = Taxi("Taksi", "Toyota", "Juodas", 4, "TAX-456")
# train = Train("Traukinys", "Siemens", "Pilkas", 200, "TRN-789")

# print(bus.describe())
# print("Kaina:", bus.ticket_price())  # ← будет с 10% наценкой
# print(bus.honk())
# print()

# print(taxi.describe())
# print("Kaina:", taxi.ticket_price())
# print(taxi.start())
# print()

# print(train.describe())
# print("Kaina:", train.ticket_price())
# print(train.stop())

class Vehicle:
    def __init__(self, make, model, year, capacity):
        self.make = make
        self.model = model
        self.year = year
        self.capacity = capacity

    def display_info(self):
        print(
            f"Vehicle Make: {self.make}, Model: {self.model}, Year: {self.year}, "
            f"Capacity: {self.capacity}"
        )

    def start_engine(self):
        print("The engine is starting.")

    def stop_engine(self):
        print("The engine is stopping.")

    def fare(self):
        return self.capacity * 100

    def maintenance_check(self):
        print("Conducting routine maintenance.")


class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10
        return base_fare + maintenance_charge

    def open_doors(self):
        print("Opening the bus doors.")

    def close_doors(self):
        print("Closing the bus doors.")


class Taxi(Vehicle):
    def fare(self):
        return super().fare()  # Assume no extra charge for Taxis

    def meter_on(self):
        print("Taxi meter is now on.")

    def meter_off(self):
        print("Taxi meter is now off.")


class Train(Vehicle):
    def fare(self):
        return super().fare()  # Assume no extra charge for Trains

    def start_announcement(self):
        print("Please mind the gap between the train and the platform.")

    def stop_announcement(self):
        print("This is the final station.")
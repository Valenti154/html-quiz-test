# class Vehicle:
#     def make_sound(self):
#         print("Nezinomas transporto garsas.")

# class Car(Vehicle):
#     def make_sound(self):
#         print("Vroom!")

# class Bike(Vehicle):
#     def make_sound(self):
#         print("Ring-ring!")

# v = Vehicle()
# c = Car()
# b = Bike()
# v.make_sound()
# c.make_sound()
# b.make_sound()
    
username = input("Įveskite slapyvardį: ")
password = input("Įveskite slaptažodį: ")

if username == "" or password == "":
    print("Negalite palikti tuščių laukų!")  # ❗ Проверка на пустые строки
elif username == "admin" and password == "slaptas":
    print("Prisijungta sėkmingai!")          # ✅ Всё правильно
else:
    print("Prisijungimas nepavyko.")  


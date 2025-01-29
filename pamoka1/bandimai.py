name = "Code Academy"
# print(name[5])
# print(name[-2])
# print(name[5:12])
# print(name[:4])
# print(name[5:12:1])
# print(name[5::2])
# print(name[::-1])
# print(name.upper())
# print(name.replace("o","e"))
# print(name.replace("Code","Muzik"))
# print(name[-1])
# print(name[-2])
# print(name[:4])
# print(name[5:12])
# print(name.upper())
# print(name.split())
# print(name.pop())
# num1 = int(input("Iveskit pirma skaiciu:"))
# num2 = int(input("Iveskit antra skaiciu:"))
# result = num1 + num2
# print( "Summa yra",result)

# farengeit = float(input("Įveskite temperatūrą pagal Farenheitą:"))
# celsius = (farengeit- 32) * 5 / 9
# print("Temperatūra pagal Celsijų:",celsius)

# word = input("Iveskite zodi:")
# reversed_word = word[::-1]
# print("Apverstas zodis:",reversed_word)

# first_name = input("iveskit savo varda:")
# last_name = input("iveskit savo pavarde:")
# formating_name = f"{first_name} {last_name}"
# print("Formatuotas vardas:",formating_name)

# P = float(input("Įveskite pradinę sumą:"))
# N = float(input("Įveskite palūkanų normą (%):"))
# L = float(input("Įveskite laiką (metais): "))
# PP = (P * N * L) / 100
# print("Paprastosios palukanos",PP)
# Įveskite savo pilną vardą: Jonas Jonaitis
# Labas, JONAS, sveiki atvykę!

# full_name = input("Įveskite savo pilną vardą: ")
# space_index = full_name.find(" ")
# first_name = full_name[:space_index]
# first_name_upper = first_name.upper()
# greeting = f"Labas, {first_name.upper()}, sveiki atvike!"
# print(greeting)

# split_word.py

# Слово, которое нужно разбить
# word = "Академия"

# Печатаем каждую букву на новой строке
# for letter in word:
#     print(letter)

# d = {"a": 10, "b": 20, "c": 30}
# for key, value in d.items():
#     print(key, value)

# dict_one = {"a": 10, "b": 20, "c": 30}
# dict_one.update(b=200, d=400)
# print(dict_one)

# dict_one = {"a": 10, "b": 20, "c": 30}
# dict_two = {"b": 200, "d": 400}
# dict_one.update(dict_two)
# print(dict_one)

# def my_function():

#     return 2 + 2

def my_function():

    return 2 + 2


my_val = my_function()

print(my_val)


def add_three_numbers(a, b, c):
    num_sum = a + b + c
    return num_sum * 52


my_val = add_three_numbers(2, 2, 2)
print(my_val)

my_val_sec = add_three_numbers(89, 52, 567)
print(my_val_sec)

# Write functions that:
# Makes basic math calculations,
# Converts Celsius from faranheit.
# Calculate average speed in meters/sec .Distance is given in Km and time in hours.
# Test all the functions. Prints should be clear and precise.
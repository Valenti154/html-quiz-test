# def calkulate_bmi(height, weight):
#     return  weight / (height**2)
# height = float(input("iveskite ugi metrais:"))
# weight = float(input("iveskit svori kilogramais:"))
# bmi = weight / (height **2)
# bmi = round(bmi, 2)
# print(f"KMI yra{bmi}.")

def calkulate_weight(bmi, height):
    return height**2*25
height = float(input("iveskite ugi metrais:"))
bmi = int(input("iveskit KMI:"))
weight = bmi * (height **2)
weight = round(weight, 2)
print(f"Svoris yra: {weight}.")




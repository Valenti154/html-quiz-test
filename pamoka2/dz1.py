# Базовые математические операции
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Конверсия температуры: из Фаренгейта в Цельсий
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Расчёт средней скорости (в метрах в секунду)
# Дистанция в километрах и время в часах
def average_speed(distance_km, time_hr):
    distance_m = distance_km * 1000 # переводим из км в м
    time_sec = time_hr * 3600 # переводим из часов в секунды
    if time_sec != 0:
        return distance_m / time_sec
    else:
        return "Error: Time cannot be zero"

# Тестирование всех функций
def test_functions():
    print("Basic mathematical operations:")
    print(f"6 + 3 = {add(6, 3)}")
    print(f"6 - 3 = {subtract(6, 3)}")
    print(f"6 * 3 = {multiply(6, 3)}")
    print(f"6 / 3 = {divide(6, 3)}")
    print(f"6 / 0 = {divide(6, 0)}")

    print("Temperature Conversion:")
    print(f"100°F in Celsius = {fahrenheit_to_celsius(100):.2f}°C")
    print(f"32°F in Celsius = {fahrenheit_to_celsius(32):.2f}°C")

    print("Calculating average speed:")
    print(f"Distance: 100 km, Time: 2 h, Average speed = {average_speed(100, 2):.2f} м/s")
    print(f"Distance: 50 km, Time: 1.5 h, Average speed = {average_speed(50, 1.5):.2f} м/s")
    print(f"Distance: 60 km, Time: 0 h, Average speed = {average_speed(60, 0)}")

# Запуск тестирования функций
if __name__ == "__main__":
    test_functions()
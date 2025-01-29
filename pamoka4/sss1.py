import random

# # Списки товаров, цен и количества
# items = ["toy", "book", "pen", "notebook", "bag", "laptop", "phone", "tablet", "headphones", "camera"]
# prices = [35, 50, 10, 25, 40, 1000, 700, 500, 150, 200]
# amounts = [56, 30, 100, 20, 15, 5, 8, 10, 25, 12]

# # Запрос количества корзин у пользователя
# num_baskets = int(input("Enter the number of baskets (min 5, max 10): "))
# while num_baskets < 5 or num_baskets > 10:
#     num_baskets = int(input("Please enter a number between 5 and 10: "))

# # Создание корзин
# baskets = []
# used_items = set()
# for _ in range(num_baskets):
#     item = random.choice([i for i in items if i not in used_items])
#     price = random.choice(prices)
#     amount = random.choice(amounts)
#     basket = {"item": item, "price": price, "amount": amount}
#     baskets.append(basket)
#     used_items.add(item)

# # Поиск индекса корзины с самым дорогим товаром
# most_expensive_index = max(range(len(baskets)), key=lambda i: baskets[i]["price"])

# # Поиск товара с самой низкой ценой
# lowest_price_item = min(baskets, key=lambda x: x["price"])["item"]

# # Поиск товара с наибольшей денежной стоимостью в магазине
# most_monetary_value_item = max(baskets, key=lambda x: x["price"] * x["amount"])["item"]

# # Вывод результатов
# print("Baskets:", baskets)
# print("Most expensive product basket index:", most_expensive_index)
# print("The product with the lowest price:", lowest_price_item)
# print("The item with the highest monetary value in the store:", most_monetary_value_item)

def analize_baskets(
    items: list[str],
    prices: list[float],
    amounts: list[int],
    num_baskets: int
) -> tuple[list[dict], int, str,str]:
    baskets = []
    used_items = set()
    for_in range(num_baskets):
    item = random.choice([i for i in items if i not in used_items])
        price = random.choice(prices)
        amount = random.choice(amounts)
        basket = {"item": item, "price": price, "amount": amount}
        baskets.append(basket)
        used_items.add(item)
    
    most_expensive_index = max(range(len(baskets)), key=lambda i: baskets[i]["price"])
    lowest_price_item = min(baskets, key=lambda x: x["price"])["item"]
    most_monetary_value_item = max(baskets, key=lambda x: x["price"] * x["amount"])["item"]
    
    return baskets, most_expensive_index, lowest_price_item, most_monetary_value_item

# Входные данные
items = ["toy", "book", "pen", "notebook", "bag", "laptop", "phone", "tablet", "headphones", "camera"]
prices = [35, 50, 10, 25, 40, 1000, 700, 500, 150, 200]
amounts = [56, 30, 100, 20, 15, 5, 8, 10, 25, 12]

# Ввод количества корзин
num_baskets = int(input("Enter the number of baskets (min 5, max 10): "))
while num_baskets < 5 or num_baskets > 10:
    num_baskets = int(input("Please enter a number between 5 and 10: "))

# Вызов функции
baskets, most_expensive_index, lowest_price_item, most_monetary_value_item = analyze_baskets(
    items=items,
    prices=prices,
    amounts=amounts,
    num_baskets=num_baskets
)

# Вывод результатов
print("Baskets:", baskets)
print("Most expensive product basket index:", most_expensive_index)
print("The product with the lowest price:", lowest_price_item)
print("The item with the highest monetary value in the store:", most_monetary_value_item)

    
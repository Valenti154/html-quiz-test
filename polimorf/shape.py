# class Shape:
#     def __init__(self, name, sides):
#         self.name = name        # Название фигуры (например: "Rectangle")
#         self.sides = sides      # Количество сторон (у прямоугольника — 4)

#     def area(self):
#         return 0  # Пока ничего не считаем, потому что у общей фигуры нет конкретной формулы
    
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         # Инициализируем width и height
#         self.width = width
#         self.height = height

#         # Naudojame super() kad iškviesti __init__ pirmines klases Shape
#         super().__init__("Rectangle", 4)  # Прямоугольник: имя и 4 стороны

#     def area(self):
#         return self.width * self.height  # Stačiakampio plotas = plotis * aukštis
    
# class Square(Rectangle):
#     def __init__(self, side_length):
#         self.side_length = side_length

#         # Kvadratas yra vienodo pločio ir aukščio, mes vadiname __init__ iš Rectangle
#         super().__init__(side_length, side_length)

#         # Pakeiskite figūros pavadinimą į "Square"
#         self.name = "Square"

# shape = Shape("Generic Shape", 0)
# print(shape.name)        # Generic Shape
# print(shape.area())      # 0

# rect = Rectangle(5, 10)
# print(rect.name)         # Rectangle
# print(rect.area())       # 50

# square = Square(7)
# print(square.name)       # Square
# print(square.area())     # 49


class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides

    def area(self) -> float:
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle", 4)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_length: float) -> None:
        super().__init__(side_length, side_length)
        self.side_length = side_length


square = Square(5)
print(square.name)  # prints "Rectangle"
print(square.sides)  # prints 4
print(square.area())  # prints 25
import math

class figure:
    def area(self):
        pass
    def perimeter(self):
        pass

class square(figure):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return self.side * 4

class rectangle(figure):
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght
    def area(self):
        return self.width * self.lenght
    def perimeter(self):
        return (self.width + self.lenght) * 2

class circle(figure):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

square = square(int(input("Введите сторону квадрата: ")))
rectangle = rectangle(int(input("Введите ширину прямоугольника: ")), int(input("Введите длину прямоугольника: ")))
circle = circle(int(input("Введите радиус окружности: ")))

print("Квадрат - ", "Площадь: ", square.area(), "Периметр: ", square.perimeter())
print("Прямоугольник - ", "Площадь: ", rectangle.area(), "Периметр: ", rectangle.perimeter())
print("Круг - ", "Площадь: ", circle.area(), "Длина окружности: ", circle.perimeter())
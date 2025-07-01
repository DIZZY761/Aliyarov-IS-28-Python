class Figure:
    def area(self):
        """Метод для расчета площади фигуры. Должен быть переопределен в подклассах."""
        raise NotImplementedError("Метод 'area' должен быть переопределен в подклассах.")

class Square(Figure):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        """Вычисляет площадь квадрата."""
        return self.side_length ** 2

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Вычисляет площадь прямоугольника."""
        return self.width * self.height

# Пример использования
if __name__ == "__main__":
    # Создаем экземпляры классов
    square = Square(4)
    rectangle = Rectangle(3, 5)

    # Выводим площади фигур
    print(f"Площадь квадрата со стороной {square.side_length}: {square.area()}")
    print(f"Площадь прямоугольника шириной {rectangle.width} и высотой {rectangle.height}: {rectangle.area()}")

import pickle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Вычисляет площадь круга."""
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """Вычисляет длину окружности."""
        return 2 * math.pi * self.radius

    def diameter(self):
        """Вычисляет диаметр круга."""
        return 2 * self.radius

def save_def(circles, filename):
    """Сохраняет список объектов Circle в файл."""
    with open(filename, 'wb') as file:
        pickle.dump(circles, file)

def load_def(filename):
    """Загружает список объектов Circle из файла."""
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Пример использования
if __name__ == "__main__":
    # Создаем три экземпляра класса Circle
    circle1 = Circle(5)
    circle2 = Circle(10)
    circle3 = Circle(15)

    # Сохраняем их в файл
    circles = [circle1, circle2, circle3]
    save_def(circles, 'circles.pkl')

    # Загружаем их обратно
    loaded_circles = load_def('circles.pkl')

    # Выводим информацию о загруженных кругах
    for i, circle in enumerate(loaded_circles, start=1):
        print(f"Круг {i}:")
        print(f"  Радиус: {circle.radius}")
        print(f"  Площадь: {circle.area():.2f}")
        print(f"  Длина окружности: {circle.circumference():.2f}")
        print(f"  Диаметр: {circle.diameter():.2f}")
        print()

#Дано: Известно, что X кг конфет стоит A рублей. Определить, сколько стоит 1 кг и Y кг этих же конфет.

#Переменные
x = (input("Введите вес конфет в кг: "))
a = (input("Введите стоимость конфет в рублях: "))
y = (input("Введите желаемый вес конфет в кг: "))
u = ("стоимость конфет")
g = ("цена за кг")

#Проверка
while type(x) != int: # обработка исключений
    try:
        x = int(x)
    except ValueError:
        print("Неправильно ввели!")
        x = input("Введите первое число: ")
#Проверка
while type(a) != int: # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")
#Проверка
while type(y) != int: # обработка исключений
    try:
        y = int(y)
    except ValueError:
        print("Неправильно ввели!")
        y = input("Введите первое число: ")

#Определяем цену за 1 кг конфет
g = a / x

#Определяем цену за Y кг конфет
u = y * g

#Вывод
print(f"1 кг конфет стоит {g} рублей")
print(f"y кг конфет стоят {u} рублей")

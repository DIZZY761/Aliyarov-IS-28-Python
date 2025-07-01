import random

def generate_numbers_file(filename, count):
    """Генерирует файл с заданным количеством случайных целых чисел."""
    with open(filename, 'w') as file:
        for _ in range(count):
            number = random.randint(-100, 100)  # Генерируем числа от -100 до 100
            file.write(f"{number}\n")

def process_numbers_file(input_filename, output_filename):
    """Обрабатывает файл с числами и записывает результаты в новый файл."""
    with open(input_filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    # Фильтруем отрицательные нечетные элементы
    negative_odd_numbers = [num for num in numbers if num < 0 and num % 2 != 0]

    # Подсчитываем необходимые значения
    count = len(numbers)
    sum_negative_odd = sum(negative_odd_numbers)
    average_negative_odd = sum_negative_odd / len(negative_odd_numbers) if negative_odd_numbers else 0

    # Записываем результаты в новый файл
    with open(output_filename, 'w') as file:
        file.write("Исходные данные:\n")
        file.write(" ".join(map(str, numbers)) + "\n")
        file.write(f"Количество элементов: {count}\n")
        file.write("Отрицательные нечетные элементы: " + " ".join(map(str, negative_odd_numbers)) + "\n")
        file.write(f"Сумма отрицательных нечетных элементов: {sum_negative_odd}\n")
        file.write(f"Среднее арифметическое отрицательных нечетных элементов: {average_negative_odd:.2f}\n")

# Пример использования
if __name__ == "__main__":
    input_file = "numbers.txt"
    output_file = "processed_numbers.txt"
    
    # Генерируем файл с числами
    generate_numbers_file(input_file, 20)  # Генерируем 20 случайных чисел

    # Обрабатываем файл и записываем результаты
    process_numbers_file(input_file, output_file)

    print(f"Обработка завершена. Результаты записаны в '{output_file}'.")

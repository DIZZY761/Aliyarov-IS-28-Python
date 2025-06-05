#Перенести в новый двумерный список Matr1 элементы, которые не находятся в первых и последних строках и столбцах матрицы Matr2 произвольного размера

def extract_inner_matrix(Matr2):
    if not Matr2 or len(Matr2) < 3 or len(Matr2[0]) < 3:
        return []  # Возвращаем пустой список, если матрица слишком мала
    
    Matr1 = []
    for i in range(1, len(Matr2) - 1):  # Пропускаем первую и последнюю строки
        row = []
        for j in range(1, len(Matr2[i]) - 1):  # Пропускаем первый и последний столбцы
            row.append(Matr2[i][j])
        Matr1.append(row)
    return Matr1

# Пример использования
Matr2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

Matr1 = extract_inner_matrix(Matr2)
print(Matr1)
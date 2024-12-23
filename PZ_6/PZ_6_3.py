#Дан список A размера N и целые числа K и L (1 < K < L < N). Переставить в обратном порядке элементы списка, расположенные между элементами AK и AL, не включая эти элементы.


def reverse_sublist(A, K, L):
    # Проверяем, что K и L находятся в допустимых пределах
    if K < 1 or L >= len(A) or K >= L:
        print("Ошибка: K и L должны удовлетворять условиям 1 < K < L < N.")
        return A

    # Переворачиваем подсписок между K и L
    A[K:L] = A[K:L][::-1]
    
    return A

#Переменные
N = int(input("Введите размер списка N: "))
A = []

# Заполнение списка
for i in range(N):
    element = int(input(f"Введите элемент {i + 1}: "))
    A.append(element)

K = int(input("Введите K (1 < K < N): ")) - 1  # Преобразуем в 0-индексацию
L = int(input("Введите L (K < L < N): ")) - 1  # Преобразуем в 0-индексацию

# Переставляем элементы и выводим результат
result = reverse_sublist(A, K, L)
print("Результат:", result)
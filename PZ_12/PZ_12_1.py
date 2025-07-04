# Создаем последовательность A
n = int(input("Введите количество элементов в последовательности A: "))
A = []
for i in range(n):
    num = int(input(f"Введите элемент {i+1}: "))
    A.append(num)

#Формируем последовательности B (четные) и C (нечетные)
B = [x for x in A if x % 2 == 0]
C = [x for x in A if x % 2 != 0]

print(f"Последовательность A: {A}")
print(f"Последовательность B (четные элементы): {B}")
print(f"Последовательность C (нечетные элементы): {C}")

#Суммирование соответствующих элементов B и C
length = min(len(B), len(C))
sum_sequence = [B[i] + C[i] for i in range(length)]

print(f"Суммирование соответствующих элементов последовательностей B и C: {sum_sequence}")

#Нахождение минимального элемента в суммированной последовательности
if sum_sequence:
    min_element = min(sum_sequence)
    print(f"Минимальный элемент полученной последовательности: {min_element}")
else:
    print("Суммированная последовательность пуста (нет соответствующих элементов для суммирования).")

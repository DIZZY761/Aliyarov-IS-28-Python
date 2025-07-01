import tkinter as tk
from tkinter import ttk, messagebox

def calculate_cost():
    try:
        # Получаем значения из полей ввода
        x = float(entry_x.get())  # Количество килограммов конфет
        a = float(entry_a.get())  # Стоимость конфет в рублях
        y = float(entry_y.get())  # Количество килограммов для расчета стоимости

        # Вычисляем стоимость 1 кг и Y кг конфет
        cost_per_kg = a / x
        total_cost_y = cost_per_kg * y

        # Отображаем результаты
        result_label.config(text=f"Стоимость 1 кг: {cost_per_kg:.2f} рублей\n"
                                  f"Стоимость {y} кг: {total_cost_y:.2f} рублей")
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные числовые значения.")

# Создание основного окна
root = tk.Tk()
root.title("Калькулятор стоимости конфет")
root.geometry("400x300")
root.configure(bg="#f2f2f2")

# Заголовок
header = tk.Label(root, text="Калькулятор стоимости конфет", font=("Helvetica", 16), bg="#f2f2f2")
header.pack(pady=10)

# Поля ввода
label_x = tk.Label(root, text="Введите количество кг конфет (X):", bg="#f2f2f2")
label_x.pack(pady=5)
entry_x = ttk.Entry(root)
entry_x.pack(pady=5)

label_a = tk.Label(root, text="Введите стоимость конфет (A) в рублях:", bg="#f2f2f2")
label_a.pack(pady=5)
entry_a = ttk.Entry(root)
entry_a.pack(pady=5)

label_y = tk.Label(root, text="Введите количество кг для расчета (Y):", bg="#f2f2f2")
label_y.pack(pady=5)
entry_y = ttk.Entry(root)
entry_y.pack(pady=5)

# Кнопка расчета
calculate_button = ttk.Button(root, text="Рассчитать", command=calculate_cost)
calculate_button.pack(pady=20)

# Метка для отображения результатов
result_label = tk.Label(root, text="", bg="#f2f2f2")
result_label.pack(pady=10)

# Запуск основного цикла
root.mainloop()

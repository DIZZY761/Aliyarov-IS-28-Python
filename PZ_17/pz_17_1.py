import tkinter as tk
from tkinter import ttk

# Функция для обработки нажатия кнопки
def submit_form():
    print("Форма отправлена!")

# Создание основного окна
root = tk.Tk()
root.title("Регистрация")
root.geometry("400x500")
root.configure(bg="#f2f2f2")

# Заголовок
header = tk.Label(root, text="Регистрация", font=("Helvetica", 20), bg="#f2f2f2")
header.pack(pady=20)

# Поля ввода
username_label = tk.Label(root, text="Имя пользователя", bg="#f2f2f2")
username_label.pack(pady=5)
username_entry = ttk.Entry(root)
username_entry.pack(pady=5)

email_label = tk.Label(root, text="Электронная почта", bg="#f2f2f2")
email_label.pack(pady=5)
email_entry = ttk.Entry(root)
email_entry.pack(pady=5)

password_label = tk.Label(root, text="Пароль", bg="#f2f2f2")
password_label.pack(pady=5)
password_entry = ttk.Entry(root, show="*")
password_entry.pack(pady=5)

# Кнопка отправки
submit_button = ttk.Button(root, text="Отправить", command=submit_form)
submit_button.pack(pady=20)

# Запуск основного цикла
root.mainloop()

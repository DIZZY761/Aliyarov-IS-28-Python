names = ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']

# Фильтруем список по длине слов
filtered_names = [name for name in names if len(name) <= 5]

print(filtered_names)

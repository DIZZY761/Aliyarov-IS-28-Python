# ФФункция для чтения фамилий писателей из файла
def read_writer_surnames(filename):
    surnames = []
    with open('C:/Users/Рустам/Documents/GitHub/Aliyarov-IS-28-Python/PZ_14/writer.txt', 'r', encoding='utf-8') as file:
        for line in file:
            surname = line.strip()  # Удаление пробелов и символов новой строки
            if surname:  # Проверяем, что строка не пустая
                surnames.append(surname)
    return surnames

# Функция для замены слова "роман" на "произведение"
def replace_word(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile:
        content = infile.read()
    
    # Замена слова
    modified_content = content.replace('роман', 'произведение')
    
    with open('C:/Users/Рустам/Documents/GitHub/Aliyarov-IS-28-Python/PZ_14/text_with_romans.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(modified_content)

# Основная часть программы
if __name__ == '__main__':
    # Чтение фамилий
    surnames = read_writer_surnames('writer.txt')
    print(f"Количество фамилий: {len(surnames)}")
    
    # Замена слов в файле
    replace_word('text_with_romans.txt', 'text_with_proizvedeniyami.txt')

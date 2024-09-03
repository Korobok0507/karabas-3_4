# Создание функции
def single_root_words(root_word, *other_words):
    # Приводим ключевое слово к нижнему регистру
    root_word_lower = root_word.lower()

    # Создаем пустой список для хранения слов,
    # которые содержат ключевое слово, либо сами содержатся в нём
    same_words = []

    # Перебираем все слова в other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()

        # Проверяем, содержится ли ключевое слово в текущем слове,
        # либо текущее слово содержится в ключевом
        if root_word_lower in word_lower or word_lower in root_word_lower:
            # Добавляем текущее слово в same_words при выполнении условия
            same_words.append(word)

    # Возвращаем список найденных слов
    return same_words


# Примеры использования функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результатов
print(result1)
print(result2)
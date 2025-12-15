# При розв'язанні задачі зверніть увагу на наступні моменти:
# У рядку можуть зустрічаються крапки та/або коми
# Рядок може починатися з літери або, наприклад, з пробілу або точки
# У слові може бути апостроф і він є частиною слова
# Весь текст може бути представлений лише одним словом та все
# Вхідні параметри: Рядок.
# Вихідні параметри: Рядок.
def first_word(text):
    """Пошук першого слова"""
    word = ""
    started = False

    for ch in text:
        if ch.isalpha() or ch == "'":
            word += ch
            started = True
        else:
            if started:
                break
    return word


assert first_word("Hello world") == "Hello", "Test1"
assert first_word("greetings, friends") == "greetings", "Test2"
assert first_word("don't touch it") == "don't", "Test3"
assert first_word(".., and so on ...") == "and", "Test4"
assert first_word("hi") == "hi", "Test5"
assert first_word("Hello.World") == "Hello", "Test6"
print("OK")

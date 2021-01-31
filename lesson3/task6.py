
# Эта программа включает функцию, которая берет строку и выводит с большой буквы все ее слова

def int_func(user_word):
    cut_word = ''
    for i in range(1, len(user_word)):
        cut_word = cut_word + user_word[i]
    if not (user_word.istitle() and cut_word.islower()):
        user_word = user_word.capitalize()
    return user_word

def latin_char_chek(user_word):
    latin_char = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    latin_char_list = list(latin_char)
    for i in range(len(user_word)):
        if user_word[i] not in latin_char_list:
            return False

def create_new_string(user_string):
    user_list = user_string.split(' ')
    user_new_string = ''
    for word in user_list:
        if latin_char_chek(word) == False:
            print(f"{word} не корректное слово")
        else:
            user_new_string += int_func(word) + " "
    return user_new_string

user_string = input("Введите строку слов латинскими буквами через пробел: ")
print(create_new_string(user_string))


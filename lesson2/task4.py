
# Эта программа выводит каждое слово строки в новой строке и нумерует слова

user_string = input("Введите строку из нескольких слов разделяя слова пробелами:")
user_list = user_string.split(' ')
for ind, el in enumerate(user_list):
    print(ind+1, el)

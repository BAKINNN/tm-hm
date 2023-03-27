# 4*
# Ввести строку (считаем, что в начале и в конце строки нет пробелов,
# все слова в строке разделены одним пробелом). Для введенной строки
# изменить порядок символов в каждом слове в предложении,
# сохраняя при этом пробелы и первоначальный порядок слов.
# Примеры:
# "Hello World!" -> "olleH !dlroW"
# "Let's see, how it works" -> "s'teL ,ees woh ti skrow"

str_ = input("Enter your sentence, plz>> ")
words = str_.split()
reversed_words = [word[::-1] for word in words]
print(" ".join(reversed_words))
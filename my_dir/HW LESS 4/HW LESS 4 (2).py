# 2
# Написать программу, используя функции input() и print().
# Программа запрашивает ввести произвольную строку.
# Затем необходимо создать 2 строковые переменные,
# первая из которых состоит только из чётных символов введённой строки,
# а вторая только из не чётных (сделать это двумя способами: через слайсы и через цикл).
# Вначале вывести введённую строку без начальных и завершающих пробелов
# в формате "Введена строка <введённая строка>”.
# Сделать 2 отступа (используя аргументы функции print)
# и затем обе переменные вывести одной функцией print, разделяя их между собой пятью
# пробелами и закончить вывод переводом строки и тремя восклицательными знаками.


# Через слайсы
# str_ = input("Enter your string, plz>> ")
# even_chars = str_[1::2]
# odd_chars = str_[::2]
#
# print(f"Введеная строка {str_}", end="\t\t")
# print(f"{even_chars}     {odd_chars}\n!!!")


str_ = input("Enter your string, plz>> ")
even_chars, odd_chars = "", ""

for idx in range(len(str_)):
    if idx == 0 or idx % 2:
        odd_chars += str_[idx]
    else:
        even_chars += str_[idx]

print(f"Введеная строка {str_}", end="\t\t")
print(f"{even_chars}     {odd_chars}\n!!!")

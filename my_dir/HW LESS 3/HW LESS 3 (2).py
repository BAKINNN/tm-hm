# 2*
# Пользователь вводит две строки. Нужно вывести True, если в обеих строках использовались одинаковые символы,
# и False иначе. Постараться решить, не используя циклы.
# Примеры работы:
# "abc" и "bca" -> True
# "aabc" и "abc" -> True
# "Abc" и "abc" -> False
# "abc" и "aaa" -> False



diff = set(input("Enter the first string>> ")) - set(input("Enter the second string>> "))
if diff:
    print(False)
else:
    print(True)
# Пусть у нас есть три переменные:
# a = 1
# b = 2
# c = 3
# Нужно, используя распаковку кортежа, поменять местами значения переменных a и b, а потом b и c.

a, b, c = (1, 2, 3)

a, b = b, a
b, c = c, b

print(a, b)

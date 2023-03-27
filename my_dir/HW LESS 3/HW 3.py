import math
x = float(input("Введите число x: "))
y = float(input("Введите число y: "))

module_1 = abs(x)
module_2 = abs(y)
module_3 = abs(x*y)

result = ((module_1 - module_2) / (1 + module_3))

print(result)
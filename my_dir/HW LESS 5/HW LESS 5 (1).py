# Написать функцию, которая проверяет является ли целое число четным.
# Функция возвращает True, если число четное, False если нет.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.
# Ввод и вывод результата производится вне функции проверки

def is_even(num):
    return num % 2 == 0


target_num = input("Enter your number>> ")


if not target_num.isdigit():
    print("You must enter a number!")
else:
    is_even_result = is_even(int(target_num))
    if is_even_result:
        print("You entered an even number")
    else:
        print("You entered an odd number")


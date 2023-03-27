# Написать функцию, которая принимает число n и выводит числа от 0 до n.
# Если число является четным, вывести квадрат числа, вместо числа.
# Для проверки на четность использовать функцию из задания 1.
# Если число делится на 7 и на 4 одновременно, процесс останавливается.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.

def is_even(num):
    return num % 2 == 0


target_num = input("Enter your number>> ")
if not target_num.isdigit():
    print("Enter a valid number!")
else:
    for num in range(int(target_num) + 1):
        if num % 7 == 0 and num % 4 == 0 and num != 0:
            break
        elif is_even(num):
            print(num ** 2)
        else:
            print(num)

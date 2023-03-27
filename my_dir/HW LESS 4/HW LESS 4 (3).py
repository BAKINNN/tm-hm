# 3*
# Сделать программу, в которой нужно будет угадывать число

import random

generated_num = random.randint(1, 100)

while True:
    user_num = int(input("Please, enter you number>> "))
    if user_num == generated_num:  # True
        print("Congratulations!!! You are lucky!")
        break
    else:
        if user_num > generated_num:
            print("Try numbers that less than your")
        else:
            print("Try numbers that greater than your")

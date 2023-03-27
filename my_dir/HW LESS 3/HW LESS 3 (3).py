# 3*
# Написать мини-игру «Камень ножницы бумага с ботом», в которой пользователь должен выбрать либо камень,
# либо ножницы, либо бумагу. Бот делает случайный выбор (случайное число).
# Вывести результат если, например, игрок выбрал бумагу, а бот ножницы:
# Бот выбрал ножницы, вы проиграли!
# Подсказка: я не показывала, как в Pyhon получить случайное число, попробуйте найти это сами
import random

choice_mapper = {
    1: "stone",
    2: "scissors",
    3: "paper"
}

bot_choice = choice_mapper.get(random.choice([1, 2, 3]))
your_choice = choice_mapper.get((int(input("Enter your choice, where 1 - stone, 2 - scissors, 3 - paper>> "))))

print(f"You have chosen {your_choice}")
print(f"Bot chose {bot_choice}")

if bot_choice == your_choice:
    print("Draw!")
elif bot_choice == "stone":
    if your_choice == "scissors":
        print("You loose!")
    elif your_choice == "paper":
        print("You win!")
elif bot_choice == "scissors":
    if your_choice == "paper":
        print("You loose!")
    elif your_choice == "stone":
        print("You win!")
elif bot_choice == "paper":
    if your_choice == "stone":
        print("You loose!")
    elif your_choice == "scissors":
        print("You win!")

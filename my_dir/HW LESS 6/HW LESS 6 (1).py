lambda_func = lambda number: "четное" if number % 2 == 0 else "нечетное"
print(lambda_func(12))
print(lambda_func(13))
print(list(map(lambda number: "четное" if number % 2 == 0 else "нечетное", [2, 3, 4, 5])))

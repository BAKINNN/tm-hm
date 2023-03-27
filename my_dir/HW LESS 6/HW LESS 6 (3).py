strings = ('oko', 'hello', 'ervre', 'by')
print(list(filter(lambda string: string == string[::-1], strings)))
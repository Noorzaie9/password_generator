import string, random

letters  = list(string.ascii_letters)
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
    ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~'
]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print('Welcome to password generator app')
print('----------------------------------')

letter_amount = int(input('How many letters you want in your password?\n'))
symbol_amount = int(input('How many symbols you want in your password?\n'))
number_amount = int(input('How many numbers you want in your password?\n'))

password_array = []

for i in range(0, letter_amount):
    letter = random.choice(letters)
    password_array.append(letter)

for i in range(0, symbol_amount):
    letter = random.choice(symbols)
    password_array.append(letter)

for i in range(0, number_amount):
    letter = random.choice(numbers)
    password_array.append(letter)

random.shuffle(password_array)

password = ''
for e in password_array:
    password += str(e)

print(password)
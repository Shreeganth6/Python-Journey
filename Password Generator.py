import random
print("Welcome to PyPassword Generator")
pass_letters = int(input("How many letters do you like in your password? "))
pass_symbols = int(input("How many symbols do you like in your password? "))
pass_numbers = int(input("How many numbers do you like in your password? "))
alphabets = "abcdefghiklmnopqrstuvwxyz"
symbols = "!@#$%^&*"
numbers = "1234567890"
easy_password = ""
for i in range(pass_letters):
    easy_password.append(random.choice(alphabets))
    easy_password.append(random.choice(symbols))
    easy_password.append(random.choice(numbers))

easy_password = str(easy_password)
print("the Easy Password is: ", easy_password)

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase_alphabets = [letter.upper() for letter in alphabets]
alphabets = alphabets + uppercase_alphabets

tough_password = []
mixture = [uppercase_alphabets,symbols,numbers]

for i in range(pass_letters):
    tough_password.append(random.choice(mixture))

print("the Tough Password is: ", tough_password)



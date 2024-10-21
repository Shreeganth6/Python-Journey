import random
print("Welcome to PyPassword Generator")
pass_letters = int(input("How many letters do you like in your password? "))
pass_symbols = int(input("How many symbols do you like in your password? "))
pass_numbers = int(input("How many numbers do you like in your password? "))
alphabets = "abcdefghiklmnopqrstuvwxyz"
symbols = "!@#$%^&*"
numbers = "1234567890"
easy_password = []
for i in range(pass_letters):
    easy_password.append(random.choice(alphabets))
    easy_password.append(random.choice(symbols))
    easy_password.append(random.choice(numbers))

easy_password1 = ""
for i in easy_password:
    easy_password1 += i

print("the Easy Password is: ", easy_password1)

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

tough_password = []
mixture = [alphabets,symbols,numbers]

for i in range(pass_letters):
    tough_password.append(random.choice(mixture))

easy_password1 = ""

for i in tough_password:
    easy_password1 += i

print("the Tough Password is: ", easy_password1)



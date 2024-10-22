import random
import string

print("Welcome to PyPassword Generator")

pass_letters = int(input("How many letters do you like in your password? "))
pass_symbols = int(input("How many symbols do you like in your password? "))
pass_numbers = int(input("How many numbers do you like in your password? "))

la = list(string.ascii_lowercase)
ua = list(string.ascii_uppercase)


alphabets = la + ua

number = ['1','2','3','4','5','6','7','8','9','0']

symbols = ['!','@','#','$','%','^','&','*','(',')','_',]

#password

password =[]

for character in range(0,pass_letters):
    password.append(random.choice(alphabets))
for character in range(0,pass_numbers):    
    password.append(random.choice(number))
for character in range(0,pass_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
password = password[:pass_letters]
print(password)
str_password = ""

for letter in range(0,len(password)):
    str_password = str_password + password[letter]

print(f"The password is {str_password}")
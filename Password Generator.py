import random
import string

alphabets = list(string.ascii_letters) #[a-z and A-Z]
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')']

pass_len = int(input('Enter Password Length: '))
pass_num = int(input('how many number would you like to generate in this password: : '))
pass_sym = int(input('how many symbols would you like to generate in this password: : '))

password = "" #empty string to store the password value
password_list = []

for i in range(pass_len):
    password_list.append(random.choice(alphabets))
for i in range(pass_num):
    password_list.append(random.choice(numbers))
for i in range(pass_sym):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password_list = password_list[:pass_len]

for i in password_list:
    password = password + i

print(f"The Password is {password}")





import random
lower_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['@','#','$','&','_','-','+','(',')','?','!',':','/','*']
print("Welcome to my Password Generator")
no_upper_letters=int(input("Enter number of upper case letters you want in a password   "))
no_lower_letters=int(input("Enter number of lower case letters you want in a password   "))
no_numbers=int(input("Enter number of numbers you want in a password  "))
no_symbol=int(input("Enter number of symbols you want in a password  "))
password_list=[]
password=''
for i in range(no_upper_letters):
    password_list.append(random.choice(upper_letters))
for i in range(no_lower_letters):
    password_list.append(random.choice(lower_letters))
for i in range(no_numbers):
    password_list.append(random.choice(numbers))
for i in range(no_symbol):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
for i in password_list:
    password+=i
print(password)
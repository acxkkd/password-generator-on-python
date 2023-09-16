import random

user_password=""
password_length=14
password_els="1234567890AbcdEfghiOPqjLySxZv"
user_data=input("Please,enter your name:")
print(user_data)
start_com=input("To start the program enter 'start':")
print(start_com)
if start_com=='start':
    for el in range(password_length):
        user_password=user_password+random.choice(password_els)

print("Hello,",user_data,"Your password is:",user_password)
exit_prog=input("To exit from program please enter 'exit':")
if exit_prog=='exit':
    exit()

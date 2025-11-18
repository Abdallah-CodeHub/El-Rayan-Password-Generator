import string, secrets, random, sys

print("Welcome to El Rayan Password Generator\n")
print("Tip: Strong passwords are typically 16 characters or longer.\n")

# function to get int from the user
def get_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Please enter a valid whole number.")

#user input
letters = get_int("How many letters would you like in your password?\n")
numbers = get_int("How many digits would you like to include?\n")
symbols = get_int("How many symbols would you like to include?\n")


password_list = []

# 1 of each guaranteer
if letters >= 1:
    password_list.append(secrets.choice(string.ascii_uppercase))
    letters -= 1
if letters >= 1:
    password_list.append(secrets.choice(string.ascii_lowercase))
    letters -= 1
if numbers >= 1:
    password_list.append(secrets.choice(string.digits))
    numbers -= 1
if symbols >= 1:
    password_list.append(secrets.choice(string.punctuation))
    symbols -= 1

# password generator
for _ in range(letters):
    if secrets.choice([True, False]):
        password_list.append(secrets.choice(string.ascii_uppercase))
    else:
        password_list.append(secrets.choice(string.ascii_lowercase))
for _ in range(numbers):
    password_list.append(secrets.choice(string.digits))
for _ in range(symbols):
    password_list.append(secrets.choice(string.punctuation))

# guard clause
if letters == 0 and numbers == 0 and symbols == 0:
    print("You requested a password length of zero, so the program will now exit.")
    sys.exit(0)

# secure shuffle and join
random.SystemRandom().shuffle(password_list)
password = ''.join(password_list)
print(f"Your new password is: {password}\n")

# important notes for the user
print("Please note: Strong passwords are not meant to be memorized.")
print("Please store your new password in a secure and private location.")











import random # Used for random selector codes below is creating a bank of needed variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Josh's Password Generator") # Title

letter_s = int(input("How many letters would you like in your password?:")) # Get user input values ""
special_character_s = int(input("How many special characters would you like in your password?:"))
number_s = int(input("How many numbers would you like in your password?:"))

password_list = [] # To ensure code matches request
for char in range(1, letter_s + 1):
    password_list += random.choice(letters)

for char in range(1,special_character_s + 1):
    password_list += random.choice(special_characters)

for char in range(1, number_s + 1):
    password_list += random.choice(numbers)

# Shuffle and Print
random.shuffle(password_list)
password = " "
for char in password_list:
    password += char

print(f"Your password is: {password}")
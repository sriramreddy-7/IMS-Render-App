import csv
import random
import string

def generate_random_password():
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    password = random.choice(uppercase_letters) + random.choice(lowercase_letters) + random.choice(digits) + random.choice(special_characters)
    remaining_length = 8 - len(password)
    password += ''.join(random.choices(uppercase_letters + lowercase_letters + digits + special_characters, k=remaining_length))
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

with open("password.csv", mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Passwords"])
    for i in range(10):
        random_password = generate_random_password()
        writer.writerow([random_password])

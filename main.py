import random
import pyperclip

def generate_password(length):
    if length.isdigit():
        length = int(length)

        lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        special = ['@', '#', '$', '%', '&', '*']
        all_chars = lower + upper + num + special
        password = "".join(random.sample(all_chars, length))
        
        print('Your password:', password)
        pyperclip.copy(password)
    else:
        print('Please enter a valid integer for password length.')

length_str = input('Enter password length: ')
generate_password(length_str)

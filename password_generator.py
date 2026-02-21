import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter desired password length (default is 8): "))
    except ValueError:
        length = 8
        print("Invalid input! Using default length of 12.")
    
    password = generate_password(length)
    print(f"Generated Password: {password}")
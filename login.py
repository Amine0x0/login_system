from encrypt_data import generate_key, encrypt_data, decrypt_data
from cryptography.fernet import InvalidToken

# Your color codes as defined before
red = '\033[31m'
blue = '\033[34m'
yellow = '\033[33m'
reset = '\033[0m'
green = '\033[32m'

# Load encrypted user data
def load_user_data():
    try:
        with open("user_data.txt", "rb") as file:
            encrypted_data = file.read()
            decrypted_data = decrypt_data(encryption_key, encrypted_data)
            decrypted_lines = decrypted_data.splitlines()
            for line in decrypted_lines:
                login, password = line.strip().split(":")
                user_data[login] = password
    except (FileNotFoundError, InvalidToken):
        pass

# Save encrypted user data
def save_user_data():
    data_to_encrypt = "\n".join([f"{login}:{password}" for login, password in user_data.items()])
    encrypted_data = encrypt_data(encryption_key, data_to_encrypt)
    with open("user_data.txt", "wb") as file:
        file.write(encrypted_data)

# Load encryption key/generate a new one
try:
    with open("encryption_key.txt", "rb") as key_file:
        encryption_key = key_file.read()
except FileNotFoundError:
    encryption_key = generate_key()
    with open("encryption_key.txt", "wb") as key_file:
        key_file.write(encryption_key)

user_data = {}
load_user_data()

class Credentials:
    def create_account(self):
        login = self.enter_login()
        password = self.enter_password()
        
        if login in user_data:
            print(red + "Username already exists" + reset)
        else:
            user_data[login] = password
            print(green + "Account created Successfully " + reset)
        
    def login(self):
        login = self.enter_login()
        password = self.enter_password()
        
        while True:
            if login in user_data and user_data[login] == password:
                print(green + "Login Successful!" + reset)
                break
            elif login not in user_data or user_data[login] != password:
                print(red + "Wrong Username or Password" + reset)
                break
            else:
                print(red + "Something went wrong ..." + reset)

    def enter_login(self):
        temp_log = input(yellow + "Enter your Login: " + reset)
        return temp_log

    def enter_password(self):
        while True:
            temp_pass = input(yellow + "Enter your Password: " + reset)
            if len(temp_pass) >= 8:
                return temp_pass
            else:
                print(red + "The password must be at least 8 characters long." + reset)

def main():
    while True:
        user_input = input(yellow + "1) Login / 2) Create Account / 3) Exit: " + reset)
        if user_input == '1':
            Credentials().login()
        elif user_input == '2':
            Credentials().create_account()
            save_user_data()  # Save User
        elif user_input == '3':
            print(yellow + "Saving user data..." + reset)
            save_user_data()
            print(red + "Exiting Program..." + reset)
            exit()
        else:
            print(red + "Something Went Wrong" + reset)

if __name__ == "__main__":
    main()


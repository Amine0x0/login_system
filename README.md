# User Account Management Program
This Python program is a command-line application designed to manage user accounts, demonstrating fundamental Object-Oriented Programming (OOP) concepts, cryptography, and Python syntax. Please note that this project is intended for educational purposes and learning experience.

## Features
Login: Users can enter their login credentials to log in. The program verifies the username and password and provides a successful login message upon success.

Create Account: New users can create accounts by entering their desired username and password. The program checks for existing usernames and ensures that the password is at least 8 characters long.

Data Persistence: User account data is saved to a text file named user_data.txt. The data is encrypted using the cryptography library to enhance security. The encryption key is automatically generated and stored in encryption_key.txt. The encrypted data can be accessed and decrypted when the program is restarted.

ANSI Colors: The program uses ANSI color codes for colored console output. Messages are displayed in colors such as red for warnings, green for success messages, and yellow for prompts.

### Getting Started
Clone the repository to your local machine.
Make sure you have Python installed (version 3.x).
Install the cryptography library using pip install cryptography.
Run the program by executing the main script using python main_script.py.
Usage
Choose options from the menu to log in, create an account, or exit the program.
For account creation, enter a new username and password when prompted.
User account data will be saved in encrypted form in user_data.txt.

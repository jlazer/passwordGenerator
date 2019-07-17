# Justin Lazarski 2019
import random
import os
# The list of available characters for the password generator
chars = 'abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_-=+[]\;,./{}|:"<>?"ABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''

# This makes the user specify the desired length of the password
length = int(input("Input password length: "))

# For loop to append a character to the password variable for the length specified
for c in range(length):
	password += random.choice(chars)

print(password)
# This copies the generated password to the clipboard and notifies the user
os.system("echo '%s' | pbcopy" %password)
print("Password has been copied to the clipboard")






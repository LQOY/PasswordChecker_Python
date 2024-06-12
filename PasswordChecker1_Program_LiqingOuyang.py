# Liqing Ouyang
# Date:29/05/2024
# assignment PasswordChecker1

"""
This program will request the user to enter a password and will calculate the length of the password and validate the length of the password to ensure it contains the minimum number of characters 6 and a maximum of 10 characters. Continue to input the password and calculate the length of the password until a valid length password has been entered.

Once the length is valid, the program will output the length of the password and determine if the password is weak or strong. If the password only contains letters output a message stating “password weak – only contains letters” or if the password only contains numbers output a message stating “password weak – only contains numbers” otherwise output a message stating the password is strong, that is, it contains a combination of letters/numbers or other characters.

"""

# pseudocode
# Program PasswordChecker1 developed by: Liqing Ouyang
#   MIN_PASSWORD_LENGTH = 6
#   MAX_PASSWORD_LENGTH = 10

#   INPUT password

#   Validate length of password
#   while MIN_PASSWORD_LENGTH > password_length or password_length > MAX_PASSWORD_LENGTH
#       message='please enter 6-10 characters'
#       OUTPUT password_length and message
#       INPUT password again
#       END WHILE

#   Determine if the password is weak or strong
#       if password only contains numbers
#           message = "password weak – only contains numbers"

#       else if password only contains letters
#           message = "password weak – only contains letters"

#       else password is strong
#           message = "password is strong!"
#
#       OUTPUT message

# END

print('PasswordChecker1 program developed by: “Liqing Ouyang”')
# constance
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 10

# input variable
password: str = ""

# output variable
password_length: int = 0
message: str = ''

# program
password = input('Please enter password: ')
password_length = len(password)

# Validate the password length:
# when MIN_PASSWORD_LENGTH > password_length or password_length > MAX_PASSWORD_LENGTH, the while loop starts executing
while MIN_PASSWORD_LENGTH > password_length or password_length > MAX_PASSWORD_LENGTH:
    message = "please enter 6-10 characters"
    # OUTPUT password_length and message
    print("Password length is {}, {}".format(password_length, message))
    # INPUT password again
    password = input('Please enter password: ')
    password_length = len(password)
#   END WHILE

# Determine if the password is weak or strong:
# Determine if password only contains numbers
if password.isnumeric():
    message = "password weak – only contains numbers"

# Determine if password only contains letters
elif password.isalpha():
    message = "password weak – only contains letters"

# else password is strong
else:
    message = "password is strong!"

# OUTPUT password_length and message
print("Password length is {}, {}".format(password_length, message))

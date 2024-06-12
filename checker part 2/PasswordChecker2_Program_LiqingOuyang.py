# Liqing Ouyang
# Date:09/06/2024
# assignment PasswordChecker2

# pseudocode
# Program PasswordChecker2 developed by: Liqing Ouyang
#   MIN_PASSWORD_LENGTH = 6
#   MAX_PASSWORD_LENGTH = 10


# INPUT password and calculate the password_length
# password = input()
# password_length = len(password)

# Create a function: for every invalid password entered, write the date/time and reason the password is invalid to the password log file.
# add_to_log() function:
# open the log file
# input_file = open("password_log_Liqing_Ouyang.txt", "a")
# get the current date and time
# datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')
# when password length <MIN_PASSWORD_LENGTH
# reason= password<6
# when password length > MAX_PASSWORD_LENGTH
# reason= password>10
# Add current date and time + reason to log file
# Now close the file

# Validate the password_length must be a minimum of 6 and a maximum of 10 characters.
# while MIN_PASSWORD_LENGTH > password_length or password_length > MAX_PASSWORD_LENGTH:
# OUTPUT password_length and message
# For every invalid password entered, write the date/time and reason the password is invalid to the password log file.
# call function add_to_log()
# Input password again, until length is valid
#   END WHILE

# Once the password length is valid, output the password_length and a message indicating if the password is weak or strong.
# Determine if password only contains numbers:
# if password.isnumeric()
# Determine if password only contains letters:
# elif password.isalpha()
# else password is strong
# OUTPUT password_length and message

# Once the password is valid, output each line of the password log file to the screen.
# OUTPUT each line in "password_log_Liqing_Ouyang.txt"


def main():
    import datetime

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
    #   INPUT password and calculate the password_length
    password = input('Please enter password: ')
    password_length = len(password)

    def add_to_log():
        reason_password_invalid: str = ''
        # open the log file
        input_file = open("password_log_Liqing_Ouyang.txt", "a")
        # get the current date and time
        current_date_and_time = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')

        # when password length <MIN_PASSWORD_LENGTH
        if MIN_PASSWORD_LENGTH > password_length:
            # reason = "password < 6"
            reason_password_invalid = "password < 6"
        # when password length > MAX_PASSWORD_LENGTH
        elif password_length > MAX_PASSWORD_LENGTH:
            # reason = "password > 10"
            reason_password_invalid = "password > 10"

        # add current date and time + reason to log file
        input_file.write(current_date_and_time + "," + reason_password_invalid)
        input_file.write("\n")
        # Now close the file
        input_file.close()

    # Validate the password length:
    # when MIN_PASSWORD_LENGTH > password_length or password_length > MAX_PASSWORD_LENGTH, the while loop starts executing

    while MIN_PASSWORD_LENGTH > password_length or password_length > MAX_PASSWORD_LENGTH:
        message = "please enter 6-10 characters"
        # OUTPUT password_length and message
        print("Password length is {}, {}".format(password_length, message))
        # For every invalid password entered, write the date/time and reason the password is invalid to the password log file.
        add_to_log()
        # Input password again
        password = input("enter your password again:")
        password_length = len(password)
    #   END WHILE

    # Once the password length is valid, output the password_length and a message indicating if the password is weak or strong.
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

    # Once the password is valid, output each line of the password log file to the screen.
    output_file = open("password_log_Liqing_Ouyang.txt", "r")
    for line in output_file:
        print(line, end='')
    output_file.close()


main()

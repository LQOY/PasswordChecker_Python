# Liqing Ouyang
# Date:11/06/2024
# assignment PasswordChecker3

# Pseudocode
# log_file = "ITWorks_password_log.txt"
# count_pw_too_small = 0
# count_pw_too_large = 0
# error_list[]
#
# OPEN  "ITWorks_password_log.txt" FOR INPUT
# FOR line IN log_file
#       APPEND line TO error_list[]
# ENDFOR
#   CLOSE log_file
#
#   FOR EACH line IN error_list
#       OUTPUT line
#       IF line contains "password < 6" THEN
#           count_pw_too_small = count_pw_too_small + 1
#       ELIF line contains "password > 10" THEN
#           count_pw_too_large = count_pw_too_large + 1
#       ENDIF
#   ENDFOR
#
#   OUTPUT count_pw_too_small, count_pw_too_large
#
# END

def main():
    print('PasswordChecker3 program developed by: “Liqing Ouyang”')

    # Output variables
    count_pw_too_small = 0
    count_pw_too_large = 0
    # Create an empty list to store data from log file
    error_list = []

    # Use open() function to open the log file for reading
    log_file = open("ITWorks_password_log.txt", "r")
    # Use for loop to add items from log file into the error_list
    for line in log_file:
        error_list.append(line)
    # ENDFOR
    # CLOSE log_file
    log_file.close()

    #   FOR EACH line IN error_list
    for item in error_list:
        # output each line
        print(item)
        # Count the number of passwords below the minimum length
        if 'password < 6' in item:
            count_pw_too_small += 1

        # Count the number of passwords above the maximum length
        elif 'password > 10' in item:
            count_pw_too_large += 1

    # Display both counts to the screen
    print(f"Count of passwords below the minimum length: {count_pw_too_small}")
    print(f"Count of passwords below the minimum length: {count_pw_too_large}")


main()

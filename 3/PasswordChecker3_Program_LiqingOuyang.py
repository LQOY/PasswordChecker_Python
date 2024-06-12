# Liqing Ouyang
# Date:11/06/2024
# assignment PasswordChecker3

# pseudocode
# Create an empty list to store data from log file:
# error_list = []

# Read the errors from log file and add into the error_list:
# Use open() function to open the log file for reading: open("ITWorks_password_log.txt", "r")
# Use for loop to add items from log file into the error_list
# close the log file

# Use the list to output each line:
# for loop to print each item error_list

# Count the number of passwords below the minimum length:
# if ' < 6' found in item, count_pw_too_small += 1
# Count the number of passwords above the maximum length:
# if  ' > 10' found in item, count_pw_too_large += 1

# Display both counts to the screen：
# print both counts

def main():
    print('PasswordChecker3 program developed by: “Liqing Ouyang”')

    # Output variables
    count_pw_too_small = int(0)
    count_pw_too_large = int(0)

    # Create an empty list to store data from log file
    error_list = []

    # Use open() function to open the log file for reading
    output_file = open("ITWorks_password_log.txt", "r")
    # Use for loop to add items from log file into the error_list
    for line in output_file:
        error_list.append(line)

    # close the log file
    output_file.close()

    for item in error_list:
        # Use the list to output each line
        print(item)
        # Count the number of passwords below the minimum length
        if ' < 6' in item:
            count_pw_too_small += 1

        # Count the number of passwords above the maximum length
        if ' > 10' in item:
            count_pw_too_large += 1

    # Display both counts to the screen
    print(f"Count of passwords below the minimum length: {count_pw_too_small}")
    print(f"Count of passwords below the minimum length: {count_pw_too_large}")


main()

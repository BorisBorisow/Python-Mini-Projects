# Python Simple Command Line Calculator

# This is calculation function
def calculation(button, first_num, second_num):
    my_list = []
    if button == "1":
        my_list.append("+")
        my_list.append(first_num + second_num)

    elif button == "2":
        my_list.append("-")
        my_list.append(first_num - second_num)

    elif button == "3":
        my_list.append("*")
        my_list.append(first_num * second_num)

    elif button == "4":
        my_list.append("/")
        my_list.append(first_num / second_num)

    return my_list

print()
print("Python Calculator")
print()
print("Select Operation")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print()


while True:
    # Take the user input
    print()
    operation = input("Enter Operation(1/2/3/4): ")

    if operation in ("1", "2", "3", "4"):
        num_1 = float(input("Enter your first number: "))
        num_2 = float(input("Enter your second number: "))

        result = calculation(operation, num_1, num_2)

        print(num_1, result[0], num_2, " = ", result[1])

        # Check if user wants to do another calculation
        # Break the Loop if answer is "n"
        next_cal = input("Let's do next calculation? (y/n): ")
        if next_cal.upper() == "N":
            break



    else:
        print("")
        print("Invalid user input")














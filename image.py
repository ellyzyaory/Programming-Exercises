def calc_new_height():
    current_width = int(input("Enter the current width: "))
    current_height = int(input("Enter the current height: "))
    desired_width = int(input("Enter the desired width: "))
    print("The corresponding height is: ", desired_width / current_width * current_height)
    return desired_width / current_width * current_height

print(calc_new_height())

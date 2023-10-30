# Klipper Rotation Calculator Mini App

import os

def get_float_input(prompt):
    while True:
        user_input = input(prompt)
        user_input = user_input.replace(',', '.')  # Change ',' to '.' 
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("This is not a valid number. Please try again.")

os.system('cls')
old_value = get_float_input("Enter OLD Rotation Value: ")
is_value = get_float_input("Enter ACTUAL Value: ")
target_value = get_float_input("Enter TARGET Value: ")

def rotation_calculations():
    calc_cache = is_value / target_value
    new_value = old_value * calc_cache
    print("The new Rotation Value is: " + str(new_value))

rotation_calculations()

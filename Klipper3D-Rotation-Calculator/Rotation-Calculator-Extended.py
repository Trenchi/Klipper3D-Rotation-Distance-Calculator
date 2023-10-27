# Klipper Rotation Calculator Mini App

import os

def get_float_input(prompt):
    while True:
        user_input = input(prompt)
        user_input = user_input.replace(',', '.')  # Ersetze ',' durch '.'
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Das ist keine gültige Zahl. Bitte versuchen Sie es erneut.")

os.system('cls')
old_value = get_float_input("ALTEN Rotationswert eingeben: ")
is_value = get_float_input("Bitte IST Wert eingeben: ")
target_value = get_float_input("Bitte SOLL Wert eingeben: ")

def rotation_calculations():
    calc_cache = is_value / target_value
    new_value = old_value * calc_cache
    print("Der neue Rotationswert lautet: " + str(new_value))

rotation_calculations()

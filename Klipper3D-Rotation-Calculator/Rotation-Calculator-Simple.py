# Klipper Rotation Calculator Mini App

import os
os.system('cls')

old_value       = float(input("ALTEN Rotationswert eingeben: ").replace(',','.'))
is_value        = float(input("Bitte IST Wert eingeben: ").replace(',','.'))
target_value    = float(input("Bitte SOLL Wert eingeben: ").replace(',','.'))
new_value       = 0
new_value       = float(new_value)

def rotation_calculations():
    calc_cache = is_value / target_value
    new_value = old_value * calc_cache
    print("Der neue Rotationswert lautet: " + str(new_value))

rotation_calculations()
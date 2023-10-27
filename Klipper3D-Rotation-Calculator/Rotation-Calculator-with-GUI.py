# Klipper Rotation Calculator Mini App

# Imports
from tkinter import *

# Checks if the input is only numbers
def get_float_input(entry):
    while True:
        user_input = entry.get()
        user_input = user_input.replace(',', '.')
        try:
            number = float(user_input)
            return number
        except ValueError:
            return None

# Calculates and outputs the rotation
def calculate_rotation():
    old_value = get_float_input(input_field_old_value)
    is_value = get_float_input(input_field_is_value)
    target_value = get_float_input(input_field_target_value)
    
    if old_value is not None and is_value is not None and target_value is not None:
        calc_cache = is_value / target_value
        new_value = old_value * calc_cache
        result_label.config(text=f"The new Rotation Value is:  {new_value}")
    else:
        result_label.config(text="Invalid Input.\n Please enter valid numbers.")

# Create Main Window
WINDOW = Tk()
WINDOW.title("Klipper Rotation Distance Calculator V1.0 Alpha")
WINDOW.geometry("450x325")
WINDOW.resizable(False, False)
WINDOW.iconbitmap(r"C:\Users\Maik\Desktop\Klipper Rotation Calculator\icons\gears-colored.ico")

# Create Widgets (Labels and Input Fields and Button)
Label(WINDOW, text="Please Enter the Values to\n calculate your Rotation Distance.", font=('Comfortaa 12 bold')).pack()
Label(WINDOW, text="OLD Value", font=('Comfortaa 10')).pack()
input_field_old_value = Entry(WINDOW, justify='center', font=('Comfortaa 10'))
input_field_old_value.pack()
Label(WINDOW, text="IS Value", font=('Comfortaa 10')).pack()
input_field_is_value = Entry(WINDOW, justify='center', font=('Comfortaa 10'))
input_field_is_value.pack()
Label(WINDOW, text="TARGET Value", font=('Comfortaa 10')).pack()
input_field_target_value = Entry(WINDOW, justify='center', font=('Comfortaa 10'))
input_field_target_value.pack()

calculate_button = Button(WINDOW, text="Calculate", font=('Comfortaa 8 bold'), command=calculate_rotation)
calculate_button.pack()

result_label = Label(WINDOW, text="", font=('Comfortaa 12 bold'))
result_label.pack(pady=20)

WINDOW.mainloop()
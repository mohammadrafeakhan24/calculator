import tkinter as tk


# The window
root = tk.Tk()
root.wm_title('Calculator app')
root.resizable(False, False)


# The GUI widgets.
num_1_entry = tk.Entry(master=root)
num_2_entry = tk.Entry(master=root)
num_1_entry.pack(side=tk.TOP)
num_2_entry.pack(side=tk.TOP)
def get_numbers():
    result = []
    num_1_entry_value = num_1_entry.get()
    num_2_entry_value = num_2_entry.get()
    if num_1_entry_value:
        try:
            result.append(float(num_1_entry_value))
        except ValueError:
            pass
    if num_2_entry_value:
        try:
            result.append(float(num_2_entry_value))
        except ValueError:
            pass
    return result

option_selector = tk.Listbox(master=root)
option_selector.pack(side=tk.TOP)
for element in ['Add', 'Subtract', 'Multiply', 'Divide', 'Exponent']:
    option_selector.insert(0, element)
current_option_selector_element = None
def on_option_selector_element_switch(event):
    global current_option_selector_element
    curselection = event.widget.curselection()
    if curselection:
        curselection = int(curselection[0])
    else:
        curselection = 0
    current_option_selector_element = event.widget.get(curselection)
option_selector.bind('<<ListboxSelect>>', on_option_selector_element_switch)

calculate_button = tk.Button(
    master=root,
    text='Calculate!',
    bg='snow',
    fg='black'
)
calculate_button.pack(side=tk.TOP)
def set_calculate_button_command(command):
    calculate_button.configure(command=command)

output_label = tk.Label(
    master=root,
    text='',
    bg='green',
    fg='snow'
)
output_label.pack(side=tk.BOTTOM)
def output(text: str, bg='green'):
    output_label['text'] = text
    output_label['bg'] = bg


# Calculating functions
def add(num1: float, num2: float):
    return f'{num1} + {num2} = {num1 + num2}'
def subtract(num1: float, num2: float):
    if num1 == num2:
        return f'{num1} - {num2} = 0'
    else:
        return f'{num1} - {num2} = {num1-num2}\n{num2} - {num1} = {num2-num1}'
def multiply(num1: float, num2: float):
    return f'{num1} X {num2} = {num1*num2}'
def divide(num1: float, num2: float):
    try:
        if num1 == num2:
            return f'{num1} / {num2} = 1'
        else:
            return f'{num1} / {num2} = {num1/num2}\n{num2} / {num1} = {num2/num1}'
    except ZeroDivisionError:
        return 'Don\'t use 0'
def exponent(num1: float, num2: float):
    if num1 == num2:
        return f'{num1} ^ {num2} = {num1**num2}'
    else:
        return f'{num1} ^ {num2} = {num1**num2}\n{num2} ^ {num1} = {num2**num1}'


# GUI functionalities
def calculate():
    numbers = get_numbers()
    try:
        if current_option_selector_element == 'Add':
            output(add(numbers[0], numbers[1]))
        elif current_option_selector_element == 'Subtract':
            output(subtract(numbers[0], numbers[1]))
        elif current_option_selector_element == 'Multiply':
            output(multiply(numbers[0], numbers[1]))
        elif current_option_selector_element == 'Divide':
            output(divide(numbers[0], numbers[1]))
        elif current_option_selector_element == 'Exponent':
            output(exponent(numbers[0], numbers[1]))
        else:
            output(text='ERROR: Select Addition, Subtraction, Multiplication or Division')
    except IndexError:
        output(text='ERROR: Make sure that both values are filled!', bg='red')
set_calculate_button_command(calculate)


root.mainloop()  # window mainloop.

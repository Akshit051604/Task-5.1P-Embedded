import tkinter as tk
from gpiozero import LED

# Initialize LEDs
led1 = LED(27)
led2 = LED(22)
led3 = LED(2)

def reset_led():
    led1.off()
    led2.off()
    led3.off()

def turn_on_led(led):
    reset_led()
    if led == 1:
        led1.on()
    elif led == 2:
        led2.on()
    elif led == 3:
        led3.on()

#Function to handle radio button selection
def led_select():
    selected_led = led_var.get()
    turn_on_led(selected_led)

def quit_app():
    reset_led()
    root.quit()

# Create the GUI window
root = tk.Tk()
root.title("LED Control")
heading = tk.Label(root, text="Lights", font=("Helvetica", 24))
heading.pack()

# Create radio buttons
led_var = tk.IntVar()  # Use IntVar for integer values
red_button = tk.Radiobutton(root, text="Red", value=1, variable=led_var, command=led_select)
white_button = tk.Radiobutton(root, text="White", value=2, variable=led_var, command=led_select)
green_button = tk.Radiobutton(root, text="Green", value=3, variable=led_var, command=led_select)

#Reset Button
reset_button = tk.Button(root, text="Reset", command= reset_led)
reset_button.pack()

# Create exit button
exit_button = tk.Button(root, text="Exit", command=quit_app)

# Place the buttons on the window
red_button.pack()
white_button.pack()
green_button.pack()
exit_button.pack()

# Start the GUI event loop
root.mainloop()

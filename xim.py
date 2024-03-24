import pyvjoy
import time

# Set up a virtual joystick
joystick = pyvjoy.VJoyDevice(1)

# Define the functions to mimic controller inputs
def press_button(button):
    joystick.set_button(button, 1)
    time.sleep(0.1)
    joystick.set_button(button, 0)
    time.sleep(0.1)

def move_axis(axis, value):
    value = int(value * 32767)  # Scale the value to match joystick input range
    joystick.set_axis(axis, value)

# Trick the Xbox into thinking mouse movement is joystick movement
def move_mouse_as_joystick():
    # Simulate moving the mouse as joystick movement
    sensitivity = 0.5  # You can adjust this value to control sensitivity
    x_movement = sensitivity * 0.1  # Replace 0.1 with actual mouse x-axis movement
    y_movement = sensitivity * 0.1  # Replace 0.1 with actual mouse y-axis movement

    move_axis(pyvjoy.HID_USAGE_X, x_movement)
    move_axis(pyvjoy.HID_USAGE_Y, y_movement)

# Trick the Xbox into thinking keyboard keys are controller buttons
def press_keys_as_buttons():
    # Simulate pressing keyboard keys as controller buttons
    BUTTON_A = 1
    BUTTON_B = 2
    BUTTON_X = 3
    BUTTON_Y = 4

    # Replace these with the actual keys you want to map
    press_button(BUTTON_A)
    press_button(BUTTON_B)
    press_button(BUTTON_X)
    press_button(BUTTON_Y)

# Main function to run the script
if __name__ == "__main__":
    while True:
        move_mouse_as_joystick()
        press_keys_as_buttons()
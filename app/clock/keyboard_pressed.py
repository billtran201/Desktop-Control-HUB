import keyboard

print("Press any key to exit the program.")

# Infinite loop to check for key press
while True:
    if keyboard.read_event():
        print("A key was pressed!")
        break
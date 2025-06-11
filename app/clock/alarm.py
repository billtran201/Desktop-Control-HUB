import time
import datetime
import pygame
import threading
import keyboard
import os

# Function to play the alarm sound
def play_alarm(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

# Function to set the alarm
def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "app/clock/alarm_sound/zilly-pop-17767.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Alarm triggered!")

            # Start the alarm sound in a new thread
            alarm_thread = threading.Thread(target=play_alarm, args=(sound_file,))
            alarm_thread.start()

            # Start waiting for user input in the main thread
            while True:
                if keyboard.read_event():
                    # Stop the sound once user input is received
                    pygame.mixer.music.stop()
                    print("Alarm stopped.")
                    is_running = False  # Break the loop to stop checking time
                    break
    os.system('cls')

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
    

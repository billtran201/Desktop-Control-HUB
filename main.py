# TODO: Break up the script and re-organize for better readability

import subprocess
import os

def run_subprocess(script_path):
    subprocess.Popen(['python', script_path])

if __name__ == "__main__":
    os.system('cls')
    # Get the directory where the script is located
    base_directory = os.path.dirname(os.path.abspath(__file__))

    # Run local Python scripts
    run_subprocess(os.path.join(base_directory, 'localhost.py'))
    # run_subprocess(os.path.join(base_directory, 'system.py'))
    #TODO: Work on Application.py
    # run_subprocess(os.path.join(base_directory, 'application.py'))

    # Change to the Electron app directory and run npm start
    electron_app_directory = os.path.join(base_directory, 'client', 'desktop')
    original_directory = os.getcwd()
    os.chdir(electron_app_directory)
    electron_command = "npm start"
    subprocess.Popen(electron_command, shell=True, stderr=subprocess.DEVNULL)
    os.chdir(original_directory)

    # Run mobile Python script
    run_subprocess(os.path.join(base_directory, 'client', 'mobile', 'mobile.py'))

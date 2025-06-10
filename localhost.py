from flask import Flask, render_template, request
import subprocess
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    return execute_command('shutdown')

@app.route('/restart', methods=['POST'])
def restart():
    return execute_command('restart')

@app.route('/sleep', methods=['POST'])
def sleep():
    return execute_command('sleep')

def execute_command(action):
    if platform.system() == 'Windows':
        commands = {
            'shutdown': 'shutdown /s /t 1',
            'restart': 'shutdown /r /t 1',
            'sleep': 'rundll32.exe powrprof.dll,SetSuspendState 0,1,0'
        }
    elif platform.system() == 'Linux' or platform.system() == 'Darwin':
        commands = {
            'shutdown': 'sudo shutdown -h now',
            'restart': 'sudo shutdown -r now',
            'sleep': 'sudo pm-suspend'  # This may vary depending on the Linux distribution and configuration
        }
    else:
        return 'Unsupported OS', 400

    command = commands.get(action)
    if not command:
        return 'Invalid action', 400

    try:
        subprocess.run(command, shell=True, check=True)
        return f'{action.capitalize()} command executed', 200
    except Exception as e:
        print(f"Error executing {action}: {e}")
        return f'Failed to execute {action} command', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

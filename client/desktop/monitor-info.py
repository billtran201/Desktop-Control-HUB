# Python Flask example

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/monitors')
def get_monitors():
    # Example monitor data (replace with actual monitor data)
    monitors = [
        {"width": 1920, "height": 1080},
        {"width": 1280, "height": 720},
        # Add more monitor data as needed
    ]
    return jsonify(monitors)

if __name__ == '__main__':
    app.run(debug=True)

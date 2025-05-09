from flask import Flask, render_template
from flask_socketio import SocketIO
import csv
import time

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    socketio.emit('update', get_recent_stats())

@socketio.on('request_data')
def handle_request():
    socketio.emit('update', get_recent_stats())


def get_recent_stats():
    try:
        with open('packet_stats.csv') as f:
            rows = list(csv.reader(f))[-50:]
    except FileNotFoundError:
        rows = []
    # structure as list of dicts
    data = [{'time': r[0], 'ip': r[1], 'count': int(r[2])} for r in rows]
    return {'data': data}

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)


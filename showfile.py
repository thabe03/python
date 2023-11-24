from flask import Flask, send_from_directory
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/ffmpeg-core.js')
def send_ffmpeg_core():
    return send_from_directory('./', 'ffmpeg-core.js')

if __name__ == '__main__':
    app.run()
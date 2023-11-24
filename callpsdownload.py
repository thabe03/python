from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video = request.files['video']
        audio = request.files['audio']
        video.save('video.mp4')
        audio.save('audio.mp3')
        
        output_file = 'merged.mp4'
        os.system(f'ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 {output_file}')
        
        return send_file(output_file, as_attachment=True)
    
    return '''
        <html>
            <body>
                <h1>Merge Video and Audio using FFmpeg</h1>
                <form method="post" enctype="multipart/form-data">
                    <input type="file" name="video" accept="video/*" /><br /><br />
                    <input type="file" name="audio" accept="audio/*" /><br /><br />
                    <input type="submit" value="Merge" />
                </form>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

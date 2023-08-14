from flask import Flask, render_template
from service.load_credentials_google_drive import search_videos_in_drive
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
FOLDER_ID = '10fOVDLm9Bcp4tGv3EaSBpkmrGyBL5mfB'

@app.route('/')
def home():
    file = search_videos_in_drive(FOLDER_ID)
    print(file[0]['id'])
    return render_template('home.html', folder_id=file[0]['id'])



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

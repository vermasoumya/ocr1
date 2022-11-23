from flask import Flask
from flask_dropzone import Dropzone
from flask_session import Session
import os

app = Flask (__name__)
app.config['SECRET_KEY'] = '45647f48b766fa2428b9a78b47b258041a7d0cd7d2ba27c92f3c1b352c30'

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

dir_path=os.path.dirname(os.path.realpath(__file__))

app.config.update(
    UPLOADED_PATH = os.path.join(dir_path, "static/uploaded_files/"),
    DROPZONE_ALLOWED_FILE_TYPE = "image",
    DROPZONE_MAX_FILE_SIZE = 20,
    DROPZONE_MAX_FILES = 1,
)

app.config['DROPZONE_REDIRECT_VIEW'] = 'decoded'

dropzone = Dropzone(app)

from application import routes
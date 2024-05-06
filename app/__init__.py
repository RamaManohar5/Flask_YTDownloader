from pytube import YouTube
from flask import Flask, render_template
from wtforms import TextAreaField, SubmitField

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
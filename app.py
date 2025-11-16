from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Flask sucht automatisch im 'templates'-Ordner
    return render_template('index.html')

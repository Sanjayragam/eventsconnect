from flask import Flask, render_template
app = Flask(__name__)


@app.route('/routee')
def root():
    return render_template('index.html')
  
from flask import Flask, render_template
from werkzeug.utils import append_slash_redirect

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/analyze')
def analyze():
    return render_template('analyze.html')

@app.route('/search')
def search():
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True)
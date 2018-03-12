from flask import Flask, redirect, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello Flask"


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/search')
def search():
    return render_template('search.html')


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def _app():
    return render_template('index.html')


@app.route('/calculate', methods=["POST"])
def calculate():
    return 'Hello there!'


if __name__ == '__main__':
    app.run()

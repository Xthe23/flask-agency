from flask import Flask, render_template
import time

app = Flask(__name__)


@app.route('/')
def index():
    version = int(time.time())
    return render_template('homepage.html', version=version)

if __name__ == '__main__':
    app.run(debug=True)

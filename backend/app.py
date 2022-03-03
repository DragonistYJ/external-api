from flask import Flask, render_template

import virustotal

app = Flask(__name__)
app.register_blueprint(virustotal.vt)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()

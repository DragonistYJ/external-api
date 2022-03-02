from flask import Flask
import virustotal

app = Flask(__name__)
app.register_blueprint(virustotal.vt)

if __name__ == '__main__':
    app.run()

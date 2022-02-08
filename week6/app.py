from flask import Flask
from login.login import logIn

app = Flask(__name__)
app.secret_key="any string but secret" 

app.register_blueprint(logIn, url_prefix='')

if __name__ == "__main__":
    app.run(debug=True, port=3000)
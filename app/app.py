from flask import Flask
from dotenv import load_dotenv
import os
from routes import app as route_blueprint

load_dotenv()

app = Flask(__name__)
app.secret_key = 'secret123'
app.register_blueprint(route_blueprint)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

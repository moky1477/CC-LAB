import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

# Configure FLASK_DEBUG from environment variable
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
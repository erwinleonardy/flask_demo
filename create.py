import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# let this code to be run independently, wto having to run the flask app
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    # allow us to interact with Flask through the command line, instead of the GUI
    with app.app_context():
        main()

from flask_app.controllers import controller_gamers
# from flask import render_template, request, redirect
from flask_app import app
# from gamers import Gamers

# LAUNCH
if __name__ == "__main__":  # This black need to be last in file
    app.run(host="localhost", port=5002, debug=True)
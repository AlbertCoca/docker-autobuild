# -*- coding: utf-8 -*-

# ==== IMPORTS SECTION ========================================================
import flask
# ==== CONSTANTS DEFINITIONS ==================================================

# ==== CLASS DEFINITION =======================================================
app = flask.Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True, port=80)

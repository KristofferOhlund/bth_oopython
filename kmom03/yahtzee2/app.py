#!/usr/bin/env python3
"""
My second Flask app
"""
# Importera relevanta moduler
import traceback
from flask import Flask, render_template
from src.hand import Hand


app = Flask(__name__)

@app.route("/")
def main():
    """ Main route """
    my_hand = Hand()

    return render_template("index.html", hand=my_hand)
@app.route("/about")
def about():
    """ About route """

    my_name_r = "Rubi Jansson"
    my_name_k = "Kristoffer Öhlund"
    my_akr_r = "rure24"
    my_akr_k = "kroh24"

    return render_template("about.html", name=my_name_r, name_k=my_name_k,
                                                akronym=my_akr_r, akronym_k=my_akr_k)
@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run(debug=True)

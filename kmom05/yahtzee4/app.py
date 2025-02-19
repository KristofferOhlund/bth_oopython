#!/usr/bin/env python3
"""
My second Flask app
"""
# Importera relevanta moduler
import os
import re
import traceback
from flask import (Flask, render_template, request,
                   redirect, url_for, session, flash)
from src.hand import Hand
from src.scoreboard import Scoreboard


app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))


@app.route("/")
def main():
    """ Main route """
    if "hand" not in session:
        my_hand = Hand()
        scoreboard = Scoreboard()
        print("No session was found, creating one..")
        session["hand"] = my_hand.to_list()
        session["score"] = scoreboard.game_data
        session["rolls"] = 0
    else:
        my_hand = Hand(session["hand"])
        scoreboard = Scoreboard(session["score"])
        session["rolls"] = session["rolls"]
    return render_template("index.html", hand=my_hand, score=scoreboard)


@app.route("/roll", methods=["POST"])
def roll():
    """ Roll dices with int from checkbox """

    session["rolls"] = session["rolls"] + 1

    if session["rolls"] <= 2:
        # Gör request values till int
        reroll_index = request.form.getlist("checkbox")
        for index, string in enumerate(reroll_index):
            reroll_index[index] = int(string)

        # Skapa nytt hand objekt baserat på befintliga tärningar
        hand = Hand(session["hand"])
        hand.roll(reroll_index)  # rerolla valda tärningar

        # spara hand.to_list i session
        session["hand"] = hand.to_list()
    else:
        flash("Du har kastat 2 gånger, välj en regel!", "info")
    return redirect(url_for("main"))


@app.route("/addpoints", methods=["POST"])
def addpoints():
    """ Apply points to rule """
    # get rule name attribute value from form
    rule = request.form.get("radio")

    if rule:
        try:
            hand = Hand(session["hand"])
            scoreboard = Scoreboard(session["score"])
            scoreboard.add_points(rule, hand)
            session["score"] = scoreboard.game_data
            session["hand"] = hand.to_list()
            # reset number of rolls
            session["rolls"] = 0
        except ValueError as _:
            flash("Regel har redan blivit använd!")
    else:
        flash("Du har inte valt en regel!")

    return redirect(url_for("randomhand"))
    # return redirect(url_for("main"))


@app.route("/randomhand")
def randomhand():
    """Creates a new random hand after a rule has been chosen."""
    session["hand"] = Hand().to_list()
    return redirect(url_for("main"))


@app.route("/about")
def about():
    """ About route """

    my_name_r = "Rubi Jansson"
    my_name_k = "Kristoffer Öhlund"
    my_akr_r = "rure24"
    my_akr_k = "kroh24"

    return render_template("about.html", name=my_name_r, name_k=my_name_k,
                           akronym=my_akr_r, akronym_k=my_akr_k)


@app.route("/reset")
def reset():
    """ Reset current session """
    for key in list(session.keys()):
        session.pop(key)
    # _ = [session.pop(key) for key in list(session.keys())]
    return redirect(url_for("main"))


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    # pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    # pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run(debug=True)

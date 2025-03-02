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
from src.leaderboard import Leaderboard
from src.queue import Queue


app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))


@app.route("/setup")
def setup():
    """ Setup number of players. """
    return render_template("forms/setup.html")

@app.route("/add_players", methods=["POST"])
def add_players():
    """ Add number of players to the session """
    number = int(request.form.get("players"))
    queue = Queue()

    # add players to queue list
    hands = []
    scoreboards = []
    rolls = []
    for player in range(number):
        hands.append(Hand().to_list())
        scoreboards.append(Scoreboard().game_data)
        rolls.append(0)
        queue.enqueue(player)

    session["hands"] = hands
    session["scoreboards"] = scoreboards
    session["rolls"] = rolls
    session["queue"] = queue.to_list()
    return redirect(url_for("main"))



@app.route("/")
def main():
    """ Main route """
    if "hands" not in session:
        return redirect(url_for("setup"))
    queue_index = Queue.from_session(session["queue"]).peek()
    hand = Hand(session['hands'][queue_index])
    print(f"hand i main: {session['hands']}")
    score = Scoreboard(session["scoreboards"][queue_index])
    return render_template("index.html", player=queue_index, hand=hand, score=score)


@app.route("/roll", methods=["POST"])
def roll():
    """ Roll dices with int from checkbox """

    player_index = get_player_queue()
    session["rolls"][player_index] = session["rolls"][player_index] +1

    if session["rolls"][player_index] <= 2:
        # Gör request values till int
        reroll_index = request.form.getlist("checkbox")
        for index, string in enumerate(reroll_index):
            reroll_index[index] = int(string)

        # Skapa nytt hand objekt baserat på befintliga tärningar
        hand = Hand(session["hands"][player_index])
        hand.roll(reroll_index)
        # flask märker inte att vi ändrar i en inbäddad struktur (lista)
        session.modified = True
        # spara hand.to_list i session
        session["hands"][player_index] = hand.to_list()
    else:
        flash("Du har kastat 2 gånger, välj en regel!", "info")
    return redirect(url_for("main"))


def get_player_queue():
    """ metod for returning the current queue index """
    return Queue.from_session(session["queue"]).peek()


@app.route("/addpoints", methods=["POST"])
def addpoints():
    """ Apply points to rule """
    # get rule name attribute value from form
    rule = request.form.get("radio")
    player = get_player_queue()

    if rule:
        try:
            hand = Hand(session["hands"][player])
            scoreboard = Scoreboard(session["scoreboards"][player])
            scoreboard.add_points(rule, hand)
            session["score"] = scoreboard.game_data
            session["hands"][player] = hand.to_list()
            # reset number of rolls
            session["rolls"][player] = 0
            session.modified = True
        except ValueError as _:
            flash("Regel har redan blivit använd!")
    else:
        flash("Du har inte valt en regel!")

    return next_player()


def next_player():
    """ Update queue """
    print("next summoned")
    current_queue = get_player_queue()
    queue = Queue(session["queue"])
    queue.dequeue()
    queue.enqueue(current_queue)

    return redirect(url_for("main"))
# @app.route("/addpoints", methods=["POST"])
# def addpoints():
#     """ Apply points to rule """
#     # get rule name attribute value from form
#     rule = request.form.get("radio")

#     if rule:
#         try:
#             hand = Hand(session["hand"])
#             scoreboard = Scoreboard(session["score"])
#             scoreboard.add_points(rule, hand)
#             session["score"] = scoreboard.game_data
#             session["hand"] = hand.to_list()
#             # reset number of rolls
#             session["rolls"] = 0
#         except ValueError as _:
#             flash("Regel har redan blivit använd!")
#     else:
#         flash("Du har inte valt en regel!")

#     return redirect(url_for("randomhand"))


@app.route("/randomhand")
def randomhand():
    """Creates a new random hand after a rule has been chosen."""
    player = get_player_queue()
    session["hands"][player] = Hand().to_list()
    session.modified = True
    return redirect(url_for("main"))


@app.route("/highscore")
def highscore():
    """Show current highscore"""
    lb = Leaderboard().load()
    return render_template("tables/leaderboard.html", leaderboard=lb)


@app.route("/add_highscore", methods=["POST"])
def add_highscore():
    """Add points to leaderboard"""
    name = request.form.get("namn")
    points = int(request.form.get("points"))

    lb = Leaderboard().load()
    lb.add_entry(name, points)
    lb.save()

    return redirect(url_for("highscore"))


@app.route("/remove_entry", methods=["POST"])
def remove_entry():
    """Remove entry form leaderboard"""

    index = int(request.form.get("radio"))
    print(f"Jag skickades i form {index}")
    lb = Leaderboard().load()
    lb.remove_entry(index)
    lb.save()

    return redirect(url_for("reset"))


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

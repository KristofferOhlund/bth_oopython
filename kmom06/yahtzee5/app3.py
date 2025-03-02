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

# Skapar en dictionary för varje spelare
# varje dictionary läggs i Queue klassen.
# logik för att vinna ligger i flask


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
    for player in range(number):
        queue.enqueue({
            "player": player,
            "hand": Hand().to_list(),
            "scoreboard": Scoreboard().game_data,
            "rolls": 0
        })
    session["queue"] = queue.to_list()
    print(session["queue"])
    return redirect(url_for("main"))


@app.route("/")
def main():
    """ Main route """
    if "queue" not in session:
         return redirect(url_for("setup"))
    
    queue_obj = get_queue_object().peek()
    hand = Hand(queue_obj["hand"])
    scoreboard = Scoreboard().from_dict(queue_obj["scoreboard"])
    spelare = queue_obj["player"]

    return render_template("index.html", spelare=spelare, hand=hand, score=scoreboard)


@app.route("/roll", methods=["POST"])
def roll():
    """ Roll dices with int from checkbox """

    queue = get_queue_object()
    current_queue_obj = queue.peek()
    print(current_queue_obj)
    # create hand from session
    hand = Hand(current_queue_obj["hand"])
    print(hand.to_list())
    rolls = current_queue_obj["rolls"]

    if rolls < 2:
        # Gör request values till int
        reroll_index = request.form.getlist("checkbox")
        for index, string in enumerate(reroll_index):
            reroll_index[index] = int(string)
        # kasta tärningar
        hand.roll(reroll_index)
        
        # spara nya hand objektet och rolls i queue object
        current_queue_obj["hand"] = Hand().to_list()
        current_queue_obj["rolls"] = current_queue_obj["rolls"] + 1
        session.modified = True
    else:
        flash("Du har kastat 2 gånger, välj en regel!", "info")
    return redirect(url_for("main"))


def get_queue_object():
    """ method for returning Queue as object"""
    return Queue.from_session(session["queue"])


@app.route("/addpoints", methods=["POST"])
def addpoints():
    """ Apply points to rule """
    # get rule name attribute value from form
    rule = request.form.get("radio")
    current_queue_obj = get_queue_object().peek()

    if rule:
        try:
            hand = Hand(current_queue_obj["hand"])
            scoreboard = Scoreboard(current_queue_obj["scoreboard"])
            scoreboard.add_points(rule, hand)
            current_queue_obj["scoreboard"] = scoreboard.game_data
            current_queue_obj["hand"] = Hand().to_list()
            current_queue_obj["rolls"] = 0
            # update session
            session.modified = True
        except ValueError as _:
            flash(str(_))
            return redirect(url_for("main"))
    else:
        flash("Du har inte valt en regel!")
    return next_player()


def next_player():
    """ Check if there is a winner, else
     queue the next player """
    if not game_finished():
        queue = get_queue_object() 
        current_queue = queue.peek()  # nuvarande spelare
        queue.dequeue()
        queue.enqueue(current_queue)
        session["queue"] = queue.to_list()
        return redirect(url_for("main"))


def game_finished():
    """ check if all players have used all rules, return winner """
    winner_index = 0
    max_points = 0
    for idx, obj in enumerate(get_queue_object().to_list()):
        scoreboard = Scoreboard().from_dict(obj["scoreboard"])
        if scoreboard.finished():
            if scoreboard.get_total_points() > max_points:
                hand = Hand(obj["hand"]).to_list()
                winner_index = idx
        return False
    return render_template("index.html", spelare=winner_index, hand=hand, score=scoreboard)


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

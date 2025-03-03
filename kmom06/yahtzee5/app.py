#!/usr/bin/env python3
"""
My first Flask app
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
from src.manager import Manager
from src.sort import recursive_insertion

# MANAGER KLASS
# Varje spelare är en dictionary enligt
# { "player": player,
# "hand": Hand().to_list(),
# "scoreboard": Scoreboard().game_data,
# "rolls": 0 }


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

    # list of player objects
    manager_objects = []

    # add players to queue list
    for player in range(number):
        manager_objects.append({
            "player": player,
            "hand": Hand().to_list(),
            "scoreboard": Scoreboard().game_data,
            "rolls": 0
        })
        queue.enqueue(player)

    # add manager as a list of objects
    session["manager"] = Manager(manager_objects).to_list()

    session["queue"] = queue.to_list()
    return redirect(url_for("main"))


@app.route("/")
def main():
    """ Main route """
    if "manager" not in session:
        return redirect(url_for("setup"))

    manager = Manager.from_data(session["manager"]).to_list()
    queue_index = get_player_queue().peek()

    # show players hand and scoreboard
    hand = Hand(manager[queue_index]["hand"])
    scoreboard = Scoreboard().from_dict(manager[queue_index]["scoreboard"])
    spelare = manager[queue_index]["player"]

    return render_template("index.html", spelare=spelare, hand=hand, score=scoreboard)


@app.route("/roll", methods=["POST"])
def roll():
    """ Roll dices with int from checkbox """

    player_index = get_player_queue().peek()
    manager = Manager.from_data(session["manager"])
    player_object = manager.get_player(player_index)

    # create hand from session
    hand = Hand(player_object["hand"])
    rolls = player_object["rolls"]


    if rolls < 2:
        # Gör request values till int
        reroll_index = request.form.getlist("checkbox")
        for index, string in enumerate(reroll_index):
            reroll_index[index] = int(string)
        # kasta tärningar och uppdatera rolls
        hand.roll(reroll_index)
        player_object["rolls"] = player_object["rolls"] +1

        # updatera manager och spara i session
        manager.update_key_on_index(player_index, "hand", hand.to_list())
        session["manager"] = manager.to_list()
        session.modified = True
    else:
        flash("Du har kastat 2 gånger, välj en regel!", "info")
    return redirect(url_for("main"))


def get_player_queue():
    """ metod for returning the Queue object """
    return Queue.from_session(session["queue"])


@app.route("/addpoints", methods=["POST"])
def addpoints():
    """ Apply points to rule """
    # get rule name attribute value from form
    rule = request.form.get("radio")

    player_index = get_player_queue().peek()
    manager = Manager.from_data(session["manager"])
    player_object = manager.get_player(player_index)

    # create hand from session
    hand = Hand(player_object["hand"])
    scoreboard = Scoreboard().from_dict(player_object["scoreboard"])
    rolls = player_object["rolls"]

    if rule:
        try:
            scoreboard.add_points(rule, hand)
            new_obj = {
                "player": player_index,
                "hand": Hand().to_list(),
                "scoreboard": scoreboard.game_data,
                "rolls": rolls +1 
            }
            manager.replace_obj_at_index(player_index, new_obj)
            # update session
            session["manager"] = manager.to_list()
            session.modified = True
        except ValueError as e:
            flash(str(e))
            return redirect(url_for("main"))
    else:
        flash("Du har inte valt en regel!")
        return redirect(url_for("main"))

    return next_player()


def next_player():
    """ Check if there is a winner, else
     queue the next player """
    manager = Manager.from_data(session["manager"])
    all_done = manager.all_done()
    if not all_done:
        current_queue = get_player_queue().peek()
        queue = Queue(session["queue"])
        queue.dequeue()
        queue.enqueue(current_queue)
        return redirect(url_for("main"))

    # få spelare med mest poäng
    winner = manager.get_winner()
    spelare = winner["player"]
    hand = Hand(winner["hand"])
    scoreboard = Scoreboard.from_dict(winner["scoreboard"])

    return render_template("index.html", spelare=spelare, hand=hand, score=scoreboard)


@app.route("/highscore")
def highscore():
    """Show current highscore"""

    lb = Leaderboard().load()

    # Sortera med recursive_insertion
    recursive_insertion(lb.entries, lb.entries.size())

    return render_template("tables/leaderboard.html", leaderboard=lb)


@app.route("/add_highscore", methods=["POST"])
def add_highscore():
    """Add points to leaderboard"""
    name = request.form.get("namn")
    points = int(request.form.get("points"))

    lb = Leaderboard().load()
    lb.add_entry(points, name)
    lb.save()

    return redirect(url_for("highscore"))


@app.route("/remove_entry", methods=["POST"])
def remove_entry():
    """Remove entry form leaderboard"""

    index = int(request.form.get("radio"))
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

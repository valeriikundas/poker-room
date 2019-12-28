from flask_cors import CORS, cross_origin
import simplejson as json
import mongoengine as me
from mongoengine import connect
import simplejson

# import socketio
from flask import Flask, escape, current_app, request, session, url_for, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.secret_key = "123"

connect("poker", host="mongodb")

# sio = socketio.Client()

CORS(app)

STARTING_CHIP_COUNT = 10000


class Player(me.Document):
    username = me.StringField(required=True)
    chip_count = me.IntField(default=0)

    def __str__(self):
        return self.username


class Table(me.Document):
    name = me.StringField(required=True)
    players = me.ListField(me.ReferenceField(Player), default=list)


def init():
    Player.objects.delete()
    Table.objects.delete()

    player1 = Player(username="John", chip_count=3000).save()
    player2 = Player(username="Will", chip_count=2000).save()
    player3 = Player(username="Robert", chip_count=3500).save()
    Table(name="default", players=[player1, player2, player3]).save()


@app.route("/tables/")
@cross_origin()
def tables():
    return {
        "tables": list(
            map(
                lambda i: {"table_id": str(i.id), "players_count": len(i.players)},
                Table.objects.all(),
            )
        )
    }


@app.route("/users/")
def users():
    return Player.objects.to_json()


@app.route("/login/", methods=["POST"])
@cross_origin()
def login():
    try:
        username = request.json.get("username", None)
        if not username:
            return {
                "status": "error",
                "error": "request body does not contain username",
            }
        session["username"] = username
        player = Player.objects(username=username).first()
        if player is None:
            player = Player(username=username, chip_count=STARTING_CHIP_COUNT).save()
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


@app.route("/logout/")
def logout():
    if "username" in session:
        del session["username"]
    return {"status": "logged out"}


@app.route("/tables/join/<string:table_id>/", methods=["GET"])
def join_table(table_id):
    if "username" not in session:
        return {"status": "error", "error": "login first", "session": str(session)}
    table = Table.objects(id=table_id).first()
    username = session.get("username")
    player = Player.objects(username=username).first()
    if player is None:
        player = Player(username=username, chip_count=STARTING_CHIP_COUNT).save()
    table["players"].append(player)
    table.save()
    return {"status": "joined"}


@app.route("/tables/leave/")
def leave_table():
    # FIXME: this will not work for multitabling
    if "username" not in session:
        return {"status": "login first"}
    username = session.get("username")
    player = Player.objects.get(username=username)
    table = Table.objects.filter(players__contains=player)
    return {"status": "left table"}


@app.route("/table/<string:table_id>/")
def table(table_id):
    table = Table.objects.get(id=table_id)
    pot = 0
    players = [
        {"username": i.username, "chip_count": i.chip_count} for i in table.players
    ]
    return {"status": "game", "pot": pot, "players": players}


@app.route("/inform/<string:table_id>/<string:username>/", methods=["POST"])
def inform(table_id, message):
    message_json = request.get_json()

    # TODO: send to one player, not to all
    # sio.emit(message_json)


@app.route("/request_action/<string:table_id>/<string:username>/", methods=["POST"])
def request_action(table_id, username):
    message_json = request.get_json()

    # TODO: send to one player, not to all


#     sio.emit(message_json)


# @sio.event
# def connect():
#     print('connection established')


# @sio.event
# def response_callback(data):
#     print('message received with ', data)
#     data_json = simplejson.loads(data)

#     # TODO:
#     # rabbitmq_publish(data_json)


# @sio.event
# def disconnect():
#     print('disconnected from server')


# sio.connect('http://localhost:5000')
# sio.wait()


if __name__ == "__main__":
    app.run(debug=True)

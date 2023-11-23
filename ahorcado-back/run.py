from flask import Flask, request
from utils import add_game,get_current_games,get_current_games_by_ip, update_game
import uuid
from datetime import datetime,timedelta
from ahorcado import Ahorcado
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/new_game", methods=["POST"])
def new_game():

    ip = request.headers.get('X-Forwarded-For')
    if not ip:
        ip = request.remote_addr

    instance = Ahorcado('hola')

    new_game_obj = {
        'expiresIn': (datetime.now() + timedelta(minutes=5)).isoformat(),
        'instance': instance.__dict__,
        'ip': ip,
    }

    session_id = str(uuid.uuid1().hex) 

    add_game(session_id, new_game_obj)

    return session_id, 200


@app.route("/current_games")
def current_games():

    ip = request.headers.get('X-Forwarded-For')
    if not ip:
        ip = request.remote_addr

    filtered_games = get_current_games_by_ip(ip)
    return list(filtered_games.keys()),200


@app.route("/current_game/<game_id>", methods=["GET", "POST"])
def current_game(game_id):

    if request.method == "GET":
        current_games = get_current_games()
        if not game_id in current_games:
            return "NOT FOUND", 404
        
        current_game = current_games[game_id]
        
        del current_game["instance"]["palabra"]
        del current_game["ip"]
        
        return current_game
    
    else:
        data =  request.get_json()
        if not "key" in data:
            return {"error": "You must specify valid key. Example: {'key': 'a'}"}, 400
        if len(data["key"]) != 1:
               return {"error": "key must be a string of length 1"},400
        
        key = data["key"]
        
        obj = get_current_games()[game_id]
        instance = Ahorcado.from_dict(obj["instance"])
    
        if instance.letra_pertenece(key):
            instance.reemplazar_letra(key)
        else:
            instance.restar_vidas()

        instance.actualizar_estado_juego()

        obj["instance"] = instance.__dict__
        update_game(game_id, obj)
    
        if instance.partida_en_juego():
            del obj["instance"]["palabra"]
            del obj["ip"]

        elif instance.estado == instance.ESTADOS["DERROTA"]:
            obj["instance"]["defeat_reason"] = "no_lifes"

        return obj,200

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=4000)
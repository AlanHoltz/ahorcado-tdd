from flask import Flask, request
from utils import add_game,get_current_games,get_current_games_by_ip, update_game, get_ip
import uuid
from datetime import datetime,timedelta
from ahorcado import Ahorcado
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/new_game", methods=["POST"])
def new_game():

    ip = get_ip(request)

    ip_sessions = get_current_games_by_ip(ip)
    ip_sessions = list(ip_sessions.keys())
    
    if len(ip_sessions) != 0:
        return {"error": "You can't have more than one running session"},403

    instance = Ahorcado('hola')

    new_game_obj = {
        'expiresIn': (datetime.now() + timedelta(seconds=20)).isoformat(),
        'instance': instance.__dict__,
        'ip': ip,
    }

    session_id = str(uuid.uuid1().hex) 

    add_game(session_id, new_game_obj)

    return session_id, 200


@app.route("/leave_game/<game_id>", methods = ["DELETE"])
def leave_game(game_id):
    pass    

@app.route("/current_games")
def current_games():

    ip = request.headers.get('X-Forwarded-For')
    if not ip:
        ip = request.remote_addr

    filtered_games = get_current_games_by_ip(ip)
    return list(filtered_games.keys()),200


@app.route("/current_game/<game_id>", methods=["GET", "POST"])
def current_game(game_id):

    ip = get_ip(request)
    current_games = get_current_games()
    if not game_id in current_games:
        return "NOT FOUND", 404
    if current_games[game_id]["ip"] != ip:
        return {"error": "You can't access other players games"},403

    current_game = current_games[game_id]
    instance = Ahorcado.from_dict(current_game["instance"])

    game_expires_in = datetime.fromisoformat(current_game["expiresIn"])
    current_datetime = datetime.now()

    #Compruebo si el juego ha expirado
    if current_datetime > game_expires_in and instance.partida_en_juego():
        instance.estado = instance.ESTADOS["DERROTA"]
        current_game["instance"]["estado"] = instance.ESTADOS["DERROTA"]
        update_game(game_id, current_game)

    if request.method == "GET":
            
        if instance.estado == instance.ESTADOS["DERROTA"]:
            defeat_reason = "no_lifes" if instance.vidas == 0 else "no_time" 
            current_game["instance"]["defeat_reason"] = defeat_reason
        elif instance.partida_en_juego():
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
        
        if not instance.partida_en_juego():
            return {"error": "Game has ended"}, 403
    
        if instance.letra_pertenece(key):
            instance.reemplazar_letra(key)
        else:
            instance.restar_vidas()

        instance.actualizar_estado_juego()

        current_game["instance"] = instance.__dict__
        update_game(game_id, current_game)

        del current_game["instance"]["palabra"]
        del current_game["ip"]

        return current_game,200

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=4000)
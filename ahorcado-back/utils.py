import json

def get_current_games():
    with open('games.json', 'r') as gameFile:
        return json.load(gameFile)
    
def get_current_games_by_ip(ip):
    with open('games.json', 'r') as gameFile:
        games_dict = json.load(gameFile)
        filtered_games = {sess_id: obj for sess_id, obj in games_dict.items() if obj["ip"] == ip}
        return filtered_games
    
def add_game(id:str, obj:dict):
    current_games = get_current_games()
    with open('games.json', 'w') as gameFile:
        current_games[id] = obj
        json.dump(current_games, gameFile)

def update_game(id:str,obj:dict):
    add_game(id, obj)

def delete_game(id:str):
    current_games = get_current_games()
    if not id in current_games:
        return False
    del current_games[id]
    return True

def get_ip(request):
    ip = request.headers.get('X-Forwarded-For')
    if not ip:
        ip = request.remote_addr
    return ip
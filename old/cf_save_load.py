import os
import json
import jsonpickle
from json import JSONEncoder


def save_player_file(player_num, player):
    '''This Function uses Jsonpickle to change the complex class to a json
    useable format then saves it to disk as to the human readable
    cd_data.txt file'''
    cf_char_json = jsonpickle.encode(player, unpicklable=False)
    with open(f'cf_data-{player_num}.txt', 'w') as outfile:
        json.dump(cf_char_json, outfile, indent=4)
    print('Character dumped to Json')
    print('Character Saved to cd_data.txt')
    return (f'cf_data-{player_num}.txt')

def load_player_file(filename):
    '''This Function attempts to load the formerly saved cf_data.txt (json) file
    it returns a 'player' DICTIONARY Object'''
    print('attempting to open file!')
    with open(str(filename)) as json_file:
        cf_data = json.load(json_file)
        player = jsonpickle.decode(cf_data)
    print(type(player))
    print(dir(player))
    print(player)
    return player

def load_player1_file():
    '''This Function attempts to load the formerly saved cf_data.txt (json) file
    it returns a 'player' DICTIONARY Object'''
    print('attempting to open file!')
    with open(str('cf_data_p1.txt')) as json_file:
        cf_data = json.load(json_file)
        player1 = jsonpickle.decode(cf_data)
    print('player 1 loaded')
    return player1

def load_player2_file():
    '''This Function attempts to load the formerly saved cf_data.txt (json) file
    it returns a 'player' DICTIONARY Object'''
    print('attempting to open file!')
    with open(str('cf_data_p2.txt')) as json_file:
        cf_data = json.load(json_file)
        player2 = jsonpickle.decode(cf_data)
    print('player 2 loaded')
    return player2

load_player1_file()

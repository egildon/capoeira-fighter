#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
#
#       cf_character_creator.py
#
#       Copyright 2020 earnest gildon <egildon@gmail.com>


import os
import json
import jsonpickle
from json import JSONEncoder
import random
import time
import cf_base_class

print("The Capoeira Fighter Creation module")

#TODO: Add Load and save methods for character creation process
#TODO: Create method to allow user to utilize experience points and buildpoints
#TODO: generte random number to use as uuid combining email and random number and combine the 2



# def save_player_file(player, player_num):
#     '''This Function uses Jsonpickle to change the complex class to a json
#     useable format then saves it to disk as to the human readable
#     cd_data.txt file'''
#     cf_char_json = jsonpickle.encode(player, unpicklable=False)
#     with open(f'cf_data{player_num}.txt', 'w') as outfile:
#         json.dump(cf_char_json, outfile, indent=4)
#     print('Character dumped to Json')
#     print(f'Character Saved to cf_data{player_num}.txt')


# def load_player_files():
#     '''This Function attempts to load the formerly saved cf_data.txt (json) file
#     it returns a 'player' DICTIONARY Object'''
#     print('attempting to reopen file!')
#     with open('cf_data.txt') as json_file:
#         cf_data = json.load(json_file)
#         player = jsonpickle.decode(cf_data)
#     print(type(player))
#     print(dir(player))
#     print(player)
#     return player

# def get_player_info(player):
#     pname = input("What is your characters name?")
#     if pname == "":
#         print ('Name cannot be blank!')
#         print ("Assging name")
#         pname = ("The Stranger")
#     playerx.set_name(pname)# is this broken?
#     print ("Your Characters name is: ")
#     print((player1.get_name()))

#     time.sleep(timex)

#     userid = input("What is your e-mail address? (userId)")
#     player1.set_userid(userid)
#     print ("Your UserID/Email is: ")
#     print((player1.get_userid()))

#     time.sleep(timex)

if __name__ == '__main__':
    print('hello')
    #seriallize_player_info()
    save_player_file(uuid_maker('Earnest', 'Bailarino'), '_p1')
    save_player_file(uuid_maker('Henry', 'Samurai'), '_p2')
    #load_player_files()

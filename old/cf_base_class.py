#!/usr/bin/env/python3.7
# -*- coding: utf-8 -*-
#
#       cf_base_class.py

import time

#from dataclasses import dataclass

'''This is the base class for Capoeira Fighter'''
#@dataclass
class CFCharacter():
    def __init__(self, user_name, char_name):
        '''This is the base class for all cahrazcters in Capoeira Fighter'''
        char_name = 'The Stranger'
        user_name = 'Person-X'
        self.user_info = {'uuid': None, 'user_name': user_name}
        self.char_status = {'in_roda': True, 'is_conscious': True, 'is_alive': True, 'xy_pos':[0,0]}
        self.char_stats = {'char_name': char_name, 'exp_total': 1, 'exp_current': 0,
                           'gender': None, 'size_cm': 78,
                           'mestre': None, 'capoeira_school': None,
                           'corda':  1, 'predction_ponts': 1,
                           'malicia': 1, 'spirit': 10, 'swag': 5,
                           'intelegence': 5, 'strength': 5, 'agility': 10,
                           'perception': 1, 'health': 10, 'reflexes': 5,
                           'accuracy': 1, 'mestre_levels': 1,
                           'prediction_points': 0}
        self.equipment = {'shirt': 0, 'pants': 0, 'shoes': 0, 'cord': None,
                          'necklace': 0, 'bracelet': 0, 'anklet': 0,
                          'hand_weapon': 0, 'foot_weapon': 0}

        #Technique {key : [0,1,2,3,4]
        #/[0]- a - attack,  b - banda, d - disloca, e - esquiva, f - feinta,
        #      g - ginga, r - rastera, t - tesoura, A - Acrobacia, F - Florieo
        #/[1]- Movement advance or retreat +- 0-3 meters
        #//[2]- Technique Level (can perform level number and below) (X * str) and (x * speed)
        #///[3]- Player Height level 3=high, 2=mid, 1=low
        #////[4]- Attack @ Level  level 3=high, 2=mid, 1=low
        #////[5]- Uuid
        self.technicas = {'ginga': ['g',0, 2, 1], 'esquiva_na_ginga':  ['e',0, 2, 2], 'deceda_basica': ['e',0, 2, 1], 'escalada':['a',1, 2, 3], 'meialua_de_frente': ['a', 1, 2, 2], 'martello': ['a', 1, 2, 3], 'banda':['b', 1, 1, 3]}

    def cfleveler():
        '''use this class to update strength and agility on the technices as well
        as add new technuques'''
        #TODO: Make this work!
        pass

    def uuid_maker(user_name, char_name):
        '''This function creates a unique player ID by combining epoc time and user name'''
        player = cf_base_class.CFCharacter(user_name, char_name)
        etime = time.time()
        temp = (player.user_info['user_name']), (str(int(etime)))
        unique_id = ":".join(temp)
        player.user_info['uuid'] = unique_id
        print(unique_id)
        print(player.user_info['uuid'])
        return player


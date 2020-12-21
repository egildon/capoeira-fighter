#!/usr/bin/env/python3
# -*- coding : utf-8 -*-
#
#       CFCharacter.py
#

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import List

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import mapper
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
# class PDFCharactor :
#     '''This is the base class for all cahracters in Capoeira Fighter'''
#     def __init__(self, userid, name) :

#         self.userid = userid
#         self.name = name
#         is_in_roda = True
#         is_conscious = True
#         is_alive = True





#         self.char_stats = {'char_name' : name, 'exp_total' :0, 'exp_current' :0, 'sex' :None, 'size' :0, 'mestre' :None,
#                     'capoeira_school' :None, 'corda' :0, 'predction_ponts' :0,
#                     'malicia' :0, 'spirit' :0, 'swag' :0,
#                     'intelegence' :0, 'strength' :0, 'agility' :0,
#                     'perception' :0, 'health' :10, 'reflexes' : 0, 'accuracy' :0,
#                       'mestre_levels' :0, 'prediction_points' :0}

#         self.equipment = {'shirt' :0, 'pants' :0, 'shoes' :0, 'cord' :None,
#                     'necklace' :0, 'bracelet' :0, 'anklet' :0,
#                     'hand_weapon' :0, 'foot_weapon' :0}

#         self.techniques_level = {'ginga' :1, 'meialua_de_frente' :1, 'esquiva_na_ginga' :1, 'deceda_basica' :1}
@dataclass
class UserInfo :
    user_id : str = field(init=False)
    character_id :int = field(default=None)
    fullname :str = field(default=None)
    nickname :str = field(default=None)
    email :str = field(default=None)

@dataclass
class CharacterInfo :    
    user_id :str = field(init=False)
    character_id :int = field(init=False)

    is_in_roda :bool = field(default=False) 
    is_conscious  :bool = field(default=True)  
    is_alive  :bool = field(default=True)

    char_name  :str=field(default=None)   
    exp_total  : int = field(default=0)   
    exp_current  : int = field(default=0)   
    gender_ident :str=field(default=None)   
    size_cm  : int = field(default=20)  
    mestre  :str=field(default=None) 
    capoeira_school  :str=field(default=None)
    corda  :str=field(default=None) 
    predction_ponts  : int = field(default=0) 
    malicia  : int = field(default=0)  
    spirit  : int = field(default=0)   
    swag  : int = field(default=0) 
                 
    intelegence : int = field(default=5) 
    strength  : int = field(default=5)  
    agility  : int = field(default="5") 
    perception  : int = field(default="5")   
    health  : int = field(default="5")   
    reflexes :int = field(default="5")   
    accuracy :int = field(default="5")
    mestre_levels :int = field(default="0")
    prediction_points :int = field(default="0")

    shirt_id :int = field(default="0")   
    pants_id :int = field(default="0")   
    shoes_id :int = field(default="0")  
    corda :str=field(default=None) 
    necklace_id :int = field(default="0")   
    bracelet_id :int = field(default="0")   
    anklet_id :int = field(default="0")
    hand_weapon_id :int = field(default="0")   
    foot_weapon_id :int = field(default="0")

    ginga :int = field(default="1")
    meialua_de_frente :int = field(default="1")
    esquiva_na_ginga :int = field(default="1") 
    deceda_basica :int = field(default="1")


    def pool_balanca(char_stats)  :
        pool_balanca = (char_stats['agility'] *  char_stats['perception'] +  char_stats['reflexes'])
        return pool_balanca

    def pool_health(char_stats) :
        pool_health = (char_stats['health'] *  char_stats['spirit'] +  char_stats['strength'])
        return pool_health

    def pool_stamina(char_stats) :
        pool_stamina = (char_stats['agility'] *  char_stats['spirit'] +  CharacterInfo.pool_health)
        return pool_stamina

    def pool_axe(char_stats) :
        pool_axe = (char_stats['spirit'] * char_stats['malicia'] + char_stats['swag'])
        print('axe :', pool_axe)
        return pool_axe

    def combat_strike(char_stats, pools,techniques_level) :
        #TODO Make Esquiva a function in combat
        accuracy = (char_stats['intelegence'] + pools.pool_balanca - pools.pool_stamina)
        return accuracy


    def combat_esquiva(char_stats, pools,techniques_level) :
        #TODO Make Esquiva a function in combat
        esquiva = (char_stats['intelgence'] *  char_stats['malicia'] +  char_stats['agility'] +  char_stats['perception'] - pools.pool_stamina)
        return esquiva

metadata = MetaData()
userinfo = Table(
    'userinfo',
    metadata,
    Column('user_id', String, primary_key=True),
    Column('character_id',Integer, ForeignKey('character_id')),
    Column('fullname', String(50)),
    Column('nickname', String(16)),
    Column('email', String(50)),
)

characterinfo = Table(
    'characterinfo',
    metadata,
    Column('user_id', String, ForeignKey('user_id')),
    Column('character_id',Integer, primary_key=True),
    Column('is_in_roda', Boolean(1)),
    Column('is_conscious', Boolean(1)),
    Column('is_alive', Boolean(1)),
    Column('char_name', String(25)),
    Column('exp_total', Integer(7)),
    Column('exp_current ', Integer(7)),
    Column('gender_ident', String(15)),
    Column('size_c', Integer(3)),
    Column('mestre', String(25)),
    Column('capoeira_school', String(25)),
    Column('corda', Integer(2)),
    Column('predction_ponts', Integer(3)),
    Column('malicia', Integer(3)),
    Column('spirit', Integer(3)),
    Column('swag', Integer(3)),
               
    Column('intelegence', Integer(3)),
    Column('strength', Integer(3)),
    Column('agility', Integer(3)),
    Column('perception', Integer(3)), 
    Column('health', Integer(3)),
    Column('reflexes', Integer(3)),
    Column('accuracy', Integer(3)),
    Column('mestre_levels', Integer(3)),
    Column('prediction_points', Integer(3)), 
    Column('shirt_id', Integer(5)),
    Column('pants_id', Integer(5)),
    Column('shoes_id', Integer(5)),
    Column('corda', String(15)),
    Column('necklace_id', Integer(5)),
    Column('bracelet_id', Integer(5)),
    Column('anklet_id', Integer(5)),
    Column('hand_weapon_id', Integer(5)),
    Column('foot_weapon_id', Integer(5)),

    Column('ginga', Integer(2)),
    Column('meialua_de_frente', Integer(2)), 
    Column('esquiva_na_ginga', Integer(2)),
    Column('deceda_basica', Integer(2))
    )

x = CharacterInfo
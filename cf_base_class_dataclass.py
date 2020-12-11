#!/usr/bin/env/python3.7
# -*- coding: utf-8 -*-
#
#       cf_base_class.py


from dataclasses import dataclass


@dataclass
class CFCharacterInfo:
    '''This is the base class for all cahracters in Capoeira Fighter'''
    char_name: str = 'The Stranger'
    user_name: str = 'Person X'
    char_stats: dict = {}
    uuid: str = None
    char_name: str = None
    exp_total: int = 0
    exp_current: int = 0
@dataclass
class CFCharacterStats:
    sex: str = None
    size_cm: int = 0
    mestre: str = None
    capoeira_school: str = None
    corda: int = 0
    predction_ponts: int = 0
    malicia: int = 0
    spirit: int = 0
    swag: int = 0
    intelegence: int = 0
    strength: int = 0
    agility: int = 0
    perception: int = 0
    health: int = 10
    reflexes: int = 0
    accuracy: int = 0
    mestre_levels: int = 0
    prediction_points: int = 0
    is_in_roda: bool = True
    is_conscious: bool = True
    is_alive: bool = True

class CFCharacterSkills(self):
    skills_levels = {'ginga':1, 'meialua_de_frente':1, 'esquiva_na_ginga':1, 'deceda_basica':1}

class CFCharacterEqupment(selfi, moo):
    self.moo = 10
    equipment = {'shirt':0, 'pants':0, 'shoes':0, 'cord':None,
                'necklace':0, 'bracelet':0, 'anklet':0,
                'hand_weapon':0, 'foot_weapon':0}







p1 = CFCharacter


##print(p1.name)
#print('character Name: ', p1.char_stats['char_name'])
#print('Technique: ',p1.techniques_level['ginga'])
#print('Balance Pool: ',pool_balanca(p1.char_stats))

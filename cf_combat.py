import cf_save_load
import cf_pools
import time
from math import sqrt

#standin for imported data
    #Technique {key : [0,1,2,3,4]
    #/[0]- a - attack,  b - banda, d - disloca, e - esquiva, f - feinta,
    #      g - ginga, r - rastera, t - tesoura, A - Acrobacia, F - Florieo
    #/[1]- Movement advance or retreat +- 0-3 meters
    #//[2]- Technique Level (can perform level number and below) (X * str) and (x * speed)
    #///[3]- Player Height level 3=high, 2=mid, 1=low
    #////[4]- Attack @ Level  level 3=high, 2=mid, 1=low
    #////[5]- Uuid

    #actions/techniqos {key : [0,1,2,3,4]
player1_jogo = [['g', 0, 2, 1, 0, None], ['e', 0, 2, 2, 0, None], ['a', 1, 2, 3, 2, None], ['g', 0, 2, 1, 0, None], [], []]
player2_jogo = [['g', 0, 2, 1, 0, None], ['a', 1, 2, 3, 3, None], ['g', 0, 2, 1, 0, None], ['e', 0, 2, 2, 0, None], [], []]
player2_jogo_dict = {'1':['g', 0, 2, 1, 0, None], '2':['a', 1, 2, 3, 3, None], '3':['g', 0, 2, 1, 0, None], '4':['e', 0, 2, 2, 0, None], '5':[],}

#combat round
def combat_loop():

    in_game = True
    conscious = True
    combat_turn = []

    #TODO: Make this work
    #TODO: Call loadfighters()
    #TODO: Load save with uuid is not working
    #cf_save_load.save_player_file(uuid_maker('Earnest', 'Bailarino'), '_p1')
    #cf_save_load.save_player_file(uuid_maker('Henry', 'Samurai'), '_p2')

    player1 = cf_save_load.load_player1_file()
    player2 = cf_save_load.load_player2_file()



    while in_game:

        if conscious:
            player1_action = player1_jogo.pop(0)
            player1_action[4] = player1['user_info']['uuid']#insert uuid into each attack/defense

            player2_action = player2_jogo.pop(0)
            player2_action[4] = player2['user_info']['uuid']#insert uuid into each attack/defense

            print(player2_action)

            # hits and misses
            if player1_action[3] > player2_action[3]:
                defender = player2_action
                attacker = player1_action

            elif player1_action[3] < player2_action[3]:
                defender = player1_action
                attacker = player2_action

            else:
                attacker = player1_action
                attacker = player2_action

            time.sleep(1)
            break
        break
    print('outer looop!')
    #TODO: Call inititive()
    #TODO: Call distance()
    #TODO: call damage()
    #TODO: call resolve()

def distance_combat(**player1_xy):#
    '''calculates strike distance between players dis > 1 is a miss'''
    dist = sqrt(sum([(a-b)**2 for a, b in zip(player1_xy, player2_xy)]))
    print(dist)
    return dist

def distance_roda(**player_xy):# the center is a constant, the player_xy is a dict obj
    '''calculates distance between player and the center of the roda dis > 5 is  not allowed'''
    roda_center = 0, 0
    dist = sqrt(sum([(a-b)**2 for a, b in zip(player_xy, roda_center)]))
    print(dist)
    if dist > 5:
        print("You back is against the wall. you cant move any more.")
    return dist

def inititive_calc(**action):#pass this a dict instead of list
    '''calculates bonuses for all actions'''
    #/[0]- a - attack,  b - banda, d - disloca, e - esquiva, f - feinta,
    #g - ginga, r - rastera, t - tesoura, A - acrobacia, F - florieo
    if action[0] == 'a':
        pass
    elif action[0] == 'b':
        pass
    elif action[0] == 'd':
        pass
    elif action[0] == 'e':
        # if action is 'esquiva' increment inititive by action level
        player1_inititive += action[2]

    elif action[0] == 'f':
        # if action is 'feinta' increment inititive by action level
        player1_inititive += action[2]

    elif action[0] == 'g':
        # if action is 'ginga' increment inititive by action level
        player1_inititive += action[2]

    elif action[0] == 'r':
        pass
    elif action[0] == 't':
        pass
    elif action[0] == 'A':
        pass
    elif action[0] == 'F':
        pass

def combat(**kwargs1):
    pass

combat()

import cf_save_load
import cf_pools
import time
from math import sqrt



#combat round
def combat():

    in_game = True
    conscious = True
    combat_turn = []

    #TODO: Make this work
    #TODO: Call loadfighters()

    player1 = cf_save_load.load_player1_file()
    player2 = cf_save_load.load_player2_file()


    #Technique {key : [0,1,2,3,4]
    #/[0]- a - attack,  b - banda, d - disloca, e - esquiva, f - feinta,
    #      g - ginga, r - rastera, t - tesoura, A - Acrobacia, F - Florieo
    #/[1]- advance or retreat +- 0-3 meters
    #//[2]- Power: technique level (can perform level number and below) (X * str)
    #//[3]- Speed: technique level (can perform level number and below) speed = (X * speed) ,
    #///[4]- attack height level 3=high, 2=mid, 1=low, ]}

    #actions/techniqos {key : [0,1,2,3,4]
    player1_jogo = [['g', 0, 2, 1, 1], ['e', 0, 2, 2, 3], ['a', 1, 2, 3, 3], ['g', 0, 2, 1, 1], [], []]
    player2_jogo = [['g', 0, 2, 1, 1], ['a', 1, 2, 3, 3], ['g', 0, 2, 1, 1], ['e', 0, 2, 2, 2], [], []]
    player3_jogo = ['g', 0, 2, 1, 1], ['a', 1, 2, 3, 3], ['g', 0, 2, 1, 1], ['e', 0, 2, 2, 2], [], []]


    player1_inititive = 0
    player2_inititive = 0
    while in_game:
        if conscious:
            player1_action = player1_jogo.pop(0)
            player2_action = player2_jogo.pop(0)

            if player1_action[3] > player2_action[3]:
                defender = player2_action
                attacker = player1_action
            elif player1_action[3] < player2_action[3]:
                defender = player1_action
                attacker = player2_action
            else:
                attacker = player1_action
                attacker = player2_action

        break
    break
    #TODO: Call inititive()
    #TODO: Call distance()
    #TODO: call damage()
    #TODO: call resolve()
            time.sleep(1)





def distance_combat(attacker, defender):
    '''calculates strike distance between players dis > 1 is a miss'''
    dist = sqrt(sum([(a-b)**2 for a, b in zip(attacker, defender)]))
    print(dist)
    return dist

def distance_roda(player, roda_center):
    '''calculates distance between player and the center of the roda dis > 5 is  not allowed'''
    roda_center = 0, 0
    dist = sqrt(sum([(a-b)**2 for a, b in zip(player, roda_center)]))
    print(dist)
    if dist > 5:
        print("You back is against the wall. you cant move any more.")
    return dist

def inititive_calc(action):
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












def pool_balanca(char_stats):
    pool_balanca = (char_stats['agility'] *  char_stats['perception'] +  char_stats['reflexes'])
    return pool_balanca

def pool_health(char_stats):
    pool_health = (char_stats['health'] *  char_stats['spirit'] +  char_stats['strength'])
    return pool_health

def pool_stamina(char_stats):
    pool_stamina = (char_stats['agility'] *  char_stats['spirit'] +  pool_health)
    return pool_stamina

def pool_axe(char_stats):
    pool_axe = (char_stats['spirit'] * char_stats['malicia'] + char_stats['swag'])
    print('axe:', pool_axe)
    return pool_axe 

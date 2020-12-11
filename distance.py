from math import sqrt



p1 = 1,1

p2 = -1,2

def distance():
    dist = sqrt(sum([(a-b)**2 for a, b in zip(p1, p2)]))
    print(dist)
distance()

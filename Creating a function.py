
fire = 0
water = 0


def simple(fire, water):
    if water == 0:
        fire += 1
    elif water < 0:
        fire += 3
    elif water > 0:
        fire = fire - water

    
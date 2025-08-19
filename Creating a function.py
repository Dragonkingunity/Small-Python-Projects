
fire = 0
water = 0


def simple(fire, water):
    if fire <= 0:
        print("No water is needed!")
    elif fire > 0:
        if water == 0:
            fire += 1
            print(fire)
        elif water < 0:
            fire += 3
            print(fire)
        elif water > 0:
            fire = fire - water
            print(fire)

simple(3,6)




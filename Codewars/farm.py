import math


def get_length(coords):
    return int(math.sqrt((coords[2] - coords[0]) ** 2 + (coords[3] - coords[1]) ** 2))


def fit_biggest_circle(coords):

    sides = []
    sides.append(get_length([coords[0],coords[1],coords[2],coords[3]]))
    sides.append(get_length([coords[2],coords[3],coords[4],coords[5]]))
    sides.append(get_length([coords[4],coords[5],coords[6],coords[7]]))
    sides.append(get_length([coords[6],coords[7],coords[0],coords[1]]))
    print(sides)
    radius = 0
    if sides[0] == sides[1] == sides[2] == sides[3]: #square
        radius = sides[0]/2
    elif (sides[0] == sides[1] and sides[2] == sides[3]) or (sides[0] == sides[3] and sides[1] == sides[2]):#kint
        radius = math.sqrt(sides[0]+sides[1] + sides[2] + sides[3]) - 2
    else:#trapezoid
        if sides[0] == sides[2]:
            radius = (math.sqrt(sides[1]*sides[3]))/2

    # center position (first two values) are not tested at present
    posx, posy = 0, 0
    return [posx, posy, radius]

print(fit_biggest_circle([-1, 0, 0, 1, 1, 0, 0, -1]))
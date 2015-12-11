def drop_floors(floor, height=100):
    floors = []
    jump = floor
    while floor < height and jump > 1:
        floors.append(floor)
        jump -= 1
        floor += jump
    return floors

def minimum_drops(height):
    out = []
    for floor in range(2, height):
        floors = drop_floors(floor, height)
        last_run = (height-1) - floors[-1]
        if last_run + len(floors) > floor:
            out.append(len(floors) + last_run)
        else:
            out.append(floor)
    return min(out)

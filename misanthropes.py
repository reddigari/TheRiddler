import numpy as np

N = 1000

houses = np.zeros(N)
free = np.arange(N)

def find_free(houses):
    free = []
    if not np.any(houses[0:2]):
        free.append(0)
    for h in range(1,len(houses)):
            if not (np.any(houses[h-1:h+2])):
                free.append(h)
    return np.array(free)

while free.size > 0:
    choice = np.random.choice(free)
    houses[choice] += 1
    free = find_free(houses)

print houses.mean()

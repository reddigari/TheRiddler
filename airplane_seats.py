import random
import numpy as np

def simulate(n_seats=100, morons=1):
    # make list of available seats and assigned seats
    seats = range(n_seats)
    assigned = list(np.random.choice(seats, n_seats, replace=False))
    # first guy sits in random seat, making it unavailable
    for moron in range(morons):
        seats.pop(random.randint(0, len(seats)-1))
    # for passengers 2-98: if assigned seat available, sit; else, make random seat unavailable
    for passenger in range(morons,n_seats-1):
        seat = assigned[passenger]
        if seat in seats:
            seats.pop(seats.index(seat))
        else:
            seats.pop(random.randint(0, len(seats)-1))
    # check if last remaining seat is assigned to last passenger
    return seats[0]==assigned[-1]

def test(n_sims, n_seats=100, morons=1):
    outcomes = np.empty(n_sims, dtype=bool)
    for i in range(n_sims):
        outcomes[i] = simulate(n_seats, morons)
    return outcomes.mean()

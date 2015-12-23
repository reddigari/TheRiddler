import numpy as np

def simulation():
    times = np.random.randint(1,6,2)
    while times[0] != times[1]:
        times[times.argmin()] += np.random.randint(1,6)
    return times[0]

outcomes = np.array([simulation() for _ in range(10000)])
print "On average, you eat after %f minutes." %outcomes.mean()

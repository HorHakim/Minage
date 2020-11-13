import matplotlib.pyplot as plt

difficulty = [1, 2, 3, 4, 5, 6, 7]
times = [1.14*10**(-4), 1.71*10**(-3), 2.47*10**(-2), 0.29, 3.72, 86.06, 2564]
plt.plot(difficulty, times)
plt.title('Average time required to mine according to difficulty')
plt.xlabel('difficulty')
plt.ylabel('time')
plt.show()
from scipy.signal import chirp, sawtooth
from matplotlib import pyplot as plt
from numpy import linspace, pi

# Chirp
t = linspace(0, 10, 1500)
w = chirp(t, f0=6, f1=1, t1=10, method='linear')
plt.plot(t, w)
plt.title("Linear Chirp, f(0)=6, f(10)=1")
plt.xlabel('t (sec)')


# Sawtooth
# t = linspace(0, 1, 500)
# plt.plot(t, sawtooth(2 * pi * 5 * t))
# plt.title("Linear Chirp, f(0)=6, f(10)=1")
# plt.xlabel('t (sec)')


plt.grid()
plt.show()

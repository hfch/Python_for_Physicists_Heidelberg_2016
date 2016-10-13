import matplotlib.pyplot as plt
import numpy as np

# matplotlib plots numpy-arrays:
x = np.linspace(-np.pi, np.pi, 50)
c = np.cos(x)
s = np.sin(x)

plt.plot(x, c)
plt.plot(x, s)

# within a script it is explicitely necessary to
# 'show' the plot
plt.show()

# or to save it:
#plt.savefig('test.png')

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.3)
y = x ** 2
plt.plot(x, y, 'ro', markersize=2, label='f(x)')
plt.title('График функции y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, alpha=1)
plt.legend()
plt.show()
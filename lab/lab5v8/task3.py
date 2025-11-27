from scipy.integrate import quad
import numpy as np

def integrand(x):
    return np.cos(x) * np.exp(x)

I = quad(integrand, 1, 4)
print(I)
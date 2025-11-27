# 2x - 3y + z = 2
# 3x + y + 2z = 7
# x + 2y + 3z = 3
import numpy as np
from scipy import linalg

A = np.array([
    [2, -3, 1],
    [3, 1, 2],
    [1, 2, 3]
])
B = np.array([2, 7, 3])
v = linalg.solve(A, B)
print("Система уравнений:")
print("2x - 3y + z = 2")
print("3x + y + 2z = 7")
print("x + 2y + 3z = 3")
print("\nРешение системы уравнений:")
print(v)
import math

def f(x):
    return math.sin(x) + math.sin(x**2)**2 + math.sin(x**3)**3

for i in range(0, 13):
    x = i / 10.0
    s = f(x)
    print(f"При x={x} функция f(x)={s}")
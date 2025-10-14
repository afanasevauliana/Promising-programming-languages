import math

for i in range(-5, 13):
    x = i / 10.0
    if x < 0.3:
        r = math.sin(math.pi/8+abs(x))
    else:
        r = math.sin((x**2 * math.pi)/2)
    print(f"При x={x} функция f(x)={r}")

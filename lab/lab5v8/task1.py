import numpy as np
import matplotlib.pyplot as plt

z = np.random.random((6, 6))
print("Матрица 6х6, содержащая случайные числа:\n",z)
z *=10
print("Матрица, умноженная на 10:\n", z)
z = z.astype(np.int32)
print("Матрица после преобразования к типу int:\n", z)
sumz = np.trace(z) + np.trace(np.fliplr(z))
print("Сумма элементов главной и побочной диагоналей:\n", sumz)

Z = np.zeros((5,5), dtype=int)
for i in range(5):
    for j in range(5):
        if (i + j) % 2 == 0:
            Z[i, j] = 8
        else:
            Z[i, j] = 3
print("Матрицу 5х5, содержащая расположенные в шахматном порядке цифры 8 и 3:\n", Z)
sumZ = np.trace(Z) + np.trace(np.fliplr(Z))
print("Сумма элементов главной и побочной диагоналей:\n", sumZ)
x = ["Матрица 6х6", "Матрица 5х5"]
z1 = [sumz, sumZ]
fig = plt.figure()
plt.bar(x, z1)
plt.title('Значения первой и второй зарезервированных переменных')
plt.grid(True) # линии вспомогательной сетки
plt.show()
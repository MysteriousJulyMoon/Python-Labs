import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Создаем фигуру для графика
plt.figure()
plt.title('Полиномы Лежандра')

x = np.linspace(-1, 1, 400)  # Определяем диапазон значений x

# Строим графики для полиномов Лежандра степеней от 1 до 7
for n in range(1, 8):
    y = legendre(n)(x)  # Вычисляем значения полинома Лежандра степени n в точках x
    plt.plot(x, y, label=f'n = {n}')  # Строим график и добавляем легенду

plt.legend(loc='upper right')  # Размещаем легенду в правом верхнем углу графика
plt.xlabel('x')
plt.ylabel('Pn(x)')
plt.grid(True)
plt.show()
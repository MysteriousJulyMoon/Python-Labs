import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создание данных
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z1 = X + Y  # Функция для первого графика
Z2 = np.log10(X + Y)  # Функция для второго графика в логарифмическом масштабе

# Построение первого трехмерного графика
fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis')
ax1.set_title('График функции MSE')

# Построение второго трехмерного графика с логарифмическим масштабом по оси z
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='plasma')
ax2.set_title('График функции MSE в логарифмическом масштабе по оси z')

plt.show()
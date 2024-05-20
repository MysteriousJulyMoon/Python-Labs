import numpy as np
import matplotlib.pyplot as plt

# Создаем фигуру для графиков
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Задаем параметры для каждой фигуры Лиссажу (соотношение частот)
ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]

# Отрисовываем каждую фигуру по очереди
for i, ratio in enumerate(ratios):
    ax = axs[i // 2, i % 2]  # Выбираем нужную область для графика
    t = np.linspace(0, 2*np.pi, 1000)
    x = np.sin(ratio[0] * t)
    y = np.sin(ratio[1] * t)
    ax.plot(x, y)
    ax.set_aspect('equal')  # Устанавливаем одинаковый масштаб по осям x и y
    ax.set_title(f'Соотношение частот: {ratio[0]}:{ratio[1]}')

plt.tight_layout()
plt.show()


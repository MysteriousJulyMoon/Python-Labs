import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    t = np.linspace(0, 2 * np.pi, 1000)
    freq_ratio = frame / 100  # Изменение соотношения частот от 0 до 1
    x = np.sin((3 + 2 * freq_ratio) * t)
    y = np.sin((2 + 2 * freq_ratio) * t)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

plt.title('Анимация вращения фигуры Лисажу')
plt.show()
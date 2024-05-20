import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Создание фигуры и осей
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Исходные данные волн
x = np.linspace(0, 2 * np.pi, 1000)
frequency1 = 1.0
amplitude1 = 1.0
frequency2 = 2.0
amplitude2 = 1.0

# Функции для волн
def wave1(x, frequency, amplitude):
    return amplitude * np.sin(frequency * x)

def wave2(x, frequency, amplitude):
    return amplitude * np.cos(frequency * x)

# Инициализация графиков
line1, = ax.plot(x, wave1(x, frequency1, amplitude1), label='Волна 1')
line2, = ax.plot(x, wave2(x, frequency2, amplitude2), label='Волна 2')
line_sum, = ax.plot(x, wave1(x, frequency1, amplitude1) + wave2(x, frequency2, amplitude2), label='Сложение')

ax.legend()

# Создание слайдеров
axamp1 = plt.axes([0.1, 0.1, 0.65, 0.03])
axfreq1 = plt.axes([0.1, 0.15, 0.65, 0.03])
axamp2 = plt.axes([0.1, 0.2, 0.65, 0.03])
axfreq2 = plt.axes([0.1, 0.25, 0.65, 0.03])

samp1 = Slider(axamp1, 'Амплитуда 1', 0.1, 10.0, valinit=amplitude1)
sfreq1 = Slider(axfreq1, 'Частота 1', 0.1, 10.0, valinit=frequency1)
samp2 = Slider(axamp2, 'Амплитуда 2', 0.1, 10.0, valinit=amplitude2)
sfreq2 = Slider(axfreq2, 'Частота 2', 0.1, 10.0, valinit=frequency2)

# Функция обновления графика
def update(val):
    amplitude1 = samp1.val
    frequency1 = sfreq1.val
    amplitude2 = samp2.val
    frequency2 = sfreq2.val

    line1.set_ydata(wave1(x, frequency1, amplitude1))
    line2.set_ydata(wave2(x, frequency2, amplitude2))
    line_sum.set_ydata(wave1(x, frequency1, amplitude1) + wave2(x, frequency2, amplitude2))
    fig.canvas.draw_idle()

# Привязка обновления к слайдерам
samp1.on_changed(update)
sfreq1.on_changed(update)
samp2.on_changed(update)
sfreq2.on_changed(update)

plt.show()
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
FileName = input()
Data = np.loadtxt(FileName)
fig, ax = plt.subplots()
X = [Data[i] for i in range(len(Data)) if not (i % 2)]
Y = [Data[i] for i in range(len(Data)) if (i % 2)]
#  Создаем функцию, генерирующую картинки
#  для последующей "склейки":


def animate(i):
    ax.clear()
    ax.set(xlim=(min(map(min, X)), max(map(max, X))), ylim=(min(map(min, Y)), max(map(max, Y))))
    ax.set_title("For Dataset %d" % i)
    ax.grid(True)
    line = ax.plot(X[i], Y[i])
    return line


sin_animation = animation.FuncAnimation(fig, animate, frames=6, interval=10, repeat=False)

sin_animation.save('моя анимация.gif', writer='imagemagick', fps=6)

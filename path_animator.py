import matplotlib.pyplot as plt
import matplotlib.animation as animation


def show_path_plot(*paths):
    for path in paths:
        x = [a[0] for a in path]
        y = [a[1] for a in path]
        plt.plot(x, y)
        print(1)
    plt.show()


def animate_2d_path(path, duration=10, fps=30):
    particle_amount = len(path[0]) // 4
    x_arrays = []
    y_arrays = []
    for i in range(particle_amount):
        x_arrays.append([a[2 * i + 1] for a in path])
        y_arrays.append([a[2 * i + 2] for a in path])
    n = len(x_arrays[0])
    frames = duration * fps
    d = int(n / frames)
    x_max, x_min = max([max(a) for a in x_arrays]), min([min(a) for a in x_arrays])
    y_max, y_min = max([max(a) for a in y_arrays]), min([min(a) for a in y_arrays])

    fig = plt.figure()
    ax = plt.axes(xlim=(x_min, x_max), ylim=(y_min, y_max))
    lines = []
    for i in range(particle_amount):
        line, = ax.plot([], [], lw=2)
        lines.append(line)

    # def init():
    #     line.set_data([], [])
    #     return line,

    x_data, y_data = [], []
    for i in range(particle_amount):
        x_data.append([])
        y_data.append([])

    def animate(frame_index):
        for i in range(particle_amount):
            x_data[i].append(x_arrays[i][frame_index * d:(frame_index + 1) * d])
            y_data[i].append(y_arrays[i][frame_index * d:(frame_index + 1) * d])
            lines[i].set_data(x_data[i], y_data[i])
        return lines

    anim = animation.FuncAnimation(fig, animate, frames=frames, interval=int(1000 / fps), blit=True)
    anim.save('C:/Users/eugen_000/Desktop/anim.gif', writer='imagemagick')


if __name__ == '__main__':
    f = open('cmake-build-debug/path.txt')
    path = []
    for line in f.readlines():
        state = tuple(map(float, line.split()))
        path.append(state)
    animate_2d_path(path)

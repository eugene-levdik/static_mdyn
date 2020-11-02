import random as r


if __name__ == '__main__':
    n = 10
    dim = 2
    max_mass = 1e27
    max_coord = 1e10
    max_speed = 1e5

    m = [(r.random() + 0.5) * max_mass for _ in range(n)]
    pos_init = [r.random() * max_coord for _ in range(dim * n)]
    vel_init = [r.random() * max_speed for _ in range(dim * n)]

    print(m)
    print()
    print(pos_init + vel_init)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

tau = 1e-4

nodes = np.linspace(-10, 10, 101)
h = nodes[1] - nodes[0]
CFL = tau / h
gamma = 5 / 3

v_start = [[0., 0., 0.]] * 101
w_start = [[0., 0., 0.]] * 101
v = [[]]
w = [[]]

for i in range(101):
    if i <= 50:
        v_start[i] = [13., 0., 10 * 10 ** 5 / (13 * (gamma - 1))]
        w_start[i] = [13., 0., 10 * 10 ** 5 / (gamma - 1)]
    else:
        v_start[i] = [1.3, 0., 10 ** 5 / (1.3 * (gamma - 1))]
        w_start[i] = [1.3, 0., 10 ** 5 / (gamma - 1)]

v[0] = v_start
w[0] = w_start

time = 0
while time <= 0.02:
    tmp = v[-1]
    tmp_w = w[-1]
    solution_w = [[0., 0., 0.]] * 101
    solution_v = [[0., 0., 0.]] * 101
    for j in range(1, 100):
        omega_t = np.empty((3, 3), dtype=np.float64)
        omega_t[0, 0] = -tmp[j][1] * np.sqrt(gamma * (gamma - 1) * tmp[j][2])
        omega_t[1, 0] = -gamma * (gamma - 1) * tmp[j][2]
        omega_t[2, 0] = tmp[j][1] * np.sqrt(gamma * (gamma - 1) * tmp[j][2])
        omega_t[0, 1] = np.sqrt(gamma * (gamma - 1) * tmp[j][2])
        omega_t[1, 1] = 0
        omega_t[2, 1] = -np.sqrt(gamma * (gamma - 1) * tmp[j][2])
        omega_t[0, 2] = gamma - 1
        omega_t[1, 2] = gamma - 1
        omega_t[2, 2] = gamma - 1
        omega_t_rev = np.linalg.inv(omega_t)
        l_diag = np.diag(
            [tmp[j][1] + np.sqrt(gamma * (gamma - 1) * tmp[j][2]), tmp[j][1],
             tmp[j][1] - np.sqrt(gamma * (gamma - 1) * tmp[j][2])])
        l_diag_ab = [abs(tmp[j][1] + np.sqrt(gamma * (gamma - 1) * tmp[j][2])), abs(tmp[j][1]),
                     abs(tmp[j][1] - np.sqrt(gamma * (gamma - 1) * tmp[j][2]))]
        l_diag_abs = np.diag(l_diag_ab)
        A = omega_t_rev @ l_diag @ omega_t

        if tau * max(l_diag_ab) / h > 1:
            tau = h / max(l_diag_ab)

        solution_w[j] = np.array(tmp_w[j]) - (tau / (2 * h)) * A @ (tmp_w[j + 1] - np.array(tmp_w[j - 1])) + (
                tau / (2 * h)) * (
                                omega_t_rev @ l_diag_abs @ omega_t) @ np.array(
            np.array(tmp_w[j + 1]) - 2 * np.array(tmp_w[j]) + np.array(tmp_w[j - 1]))
        solution_v[j][0] = solution_w[j][0]
        solution_v[j][1] = solution_w[j][1] / solution_w[j][0]
        solution_v[j][2] = solution_w[j][2] / solution_w[j][0]

    solution_v[0] = solution_v[1]
    solution_v[100] = solution_v[99]
    w.append(solution_w)
    v.append(solution_v)
    time += tau

fig = plt.figure()
ax = plt.axes(xlim=(-10, 10), ylim=(0, 5))
line, = ax.plot([], [], lw=3)

rho = np.zeros((len(v), 101))
for i in range(len(v)):
    for j in range(101):
        rho[i, j] = v[i][j][0]


def init():
    line.set_data([], [])
    return line,


def animate(i):
    x_data = nodes
    y_data = rho[i]
    line.set_data(x_data, y_data)
    return line,


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=len(v), interval=100, blit=True)
plt.show()
plt.close()

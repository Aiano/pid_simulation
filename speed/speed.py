import numpy as np
from matplotlib import pyplot as plt


class PidSimulation:
    def __init__(self, p, i, d):
        self.p = p
        self.i = i
        self.d = d

    def change_parameter(self, p, i, d):
        self.p = p
        self.i = i
        self.d = d

    def show(self, initial_speed, target_speed, drag_acceleration, time_range, unit_time=1, show_target_line=False):
        x = np.arange(1, time_range + 1, unit_time, dtype=np.float)
        now_speed = initial_speed
        previous_speed = initial_speed
        y = x.copy()
        accumulated_error = 0

        for index in range(0, len(x)):
            a = 0
            a += (target_speed - now_speed) * self.p  # p

            accumulated_error += (target_speed - now_speed) * unit_time  # i
            a += accumulated_error * self.i

            k = now_speed - previous_speed
            if k:
                k /= unit_time
            a += k * self.d

            a -= drag_acceleration  # subtract frictional acceleration

            y[index] = now_speed + a * unit_time
            now_speed = y[index]

        if show_target_line:
            target_line = np.ones(len(x)) * target_speed
            plt.plot(x, target_line, 'g')

        plt.title("PID P:" + str(self.p) + " I:" + str(self.i) + " D:" + str(self.d))
        plt.xlabel("Time")
        plt.ylabel("Velocity")
        plt.plot(x, y, 'b')
        plt.show()


if __name__ == '__main__':
    PID = PidSimulation(1, 0.09, 0)
    PID.show(0, 10, 1, 20, 0.1, True)

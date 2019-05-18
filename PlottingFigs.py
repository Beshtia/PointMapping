import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

location = "Test2\\"

write_files = ["test2 128 1000 Write", "test2 128 2000 Write", "test2 256 1000 Write", "test2 256 2000 Write"]
read_files = ["test2 128 1000 Read", "test2 128 2000 Read", "test2 256 1000 Read", "test2 256 2000 Read"]

for rfile in write_files + read_files:
    df = pd.read_excel(location + "Points.xlsx", sheet_name=rfile)
    x = (df['X-axis'] - df['X-axis'][0]).values
    y = (df['Y-axis'] - df['Y-axis'][0]).values

    plt.figure(figsize=(7.5, 5.5))
    plt.scatter(x, y, s=0.5)
    plt.grid()
    plt.title("Plotting x vs. y")
    plt.xlabel("X-axis[mm(rev.)]")
    plt.ylabel("Y-axis[mm(rev.)]")
    plt.savefig(location + "Plots\\" + rfile + " X vs. Y.png")
    print("Plotting X vs. Y for file: ", rfile)
    plt.close()

    plt.figure(figsize=(7.5, 5.5))
    dt = int(rfile[6:9]) / 8000  # Delta_t between two points((128 samples)/(8000Hz))
    dx = (x[1:] - x[:-1]) / (dt * 4000)  # 4000 encoder counts
    dx = dx[np.abs(dx) < 2 * np.std(dx)]
    t = dt * np.arange(dx.shape[0])  # Time between rapid movements is ignored
    plt.plot(t, dx)
    plt.title("Velocity of x_axis with filtered rapid move transitions")
    plt.xlabel("Time [s]")
    plt.ylabel(r"Velocity [$\frac{mm}{s}(\frac{rev.}{s})$]")
    plt.grid()
    plt.savefig(location + "Plots\\" + rfile + " Vel X.png")
    print("Plotting Velocity X for file: ", rfile)
    plt.close()

    plt.figure(figsize=(7.5, 5.5))
    ddx = (dx[1:] - dx[:-1]) / dt
    # dx = dx[np.abs(dx) <2*np.std(dx)]
    plt.plot(t[:-1], ddx)
    plt.title("Acceleration of x_axis with filtered rapid move transitions")
    plt.xlabel("Time [s]")
    plt.ylabel(r"Acceleration [$\frac{mm}{s^2}(\frac{rev.}{s^2})$]")
    plt.grid()
    plt.savefig(location + "Plots\\" + rfile + " Acc X.png")
    print("Plotting Acceleration X for file: ", rfile)
    plt.close()

    plt.figure(figsize=(7.5, 5.5))
    dy = (y[1:] - y[:-1]) / (dt * 4000)  # 4000 encoder counts
    dy = dy[np.abs(dy) < 2 * np.std(dy)]
    plt.plot(t, dy)
    plt.title("Velocity of y_axis with filtered rapid move transitions")
    plt.xlabel("Time [s]")
    plt.ylabel(r"Velocity [$\frac{mm}{s}(\frac{rev.}{s})$]")
    plt.grid()
    plt.savefig(location + "Plots\\" + rfile + " Vel Y.png")
    print("Plotting Velocity Y for file: ", rfile)
    plt.close()

    plt.figure(figsize=(7.5, 5.5))
    ddy = (dy[1:] - dy[:-1]) / dt
    # dx = dx[np.abs(dx) <2*np.std(dx)]
    plt.plot(t[:-1], ddy)
    plt.title("Acceleration of y_axis with filtered rapid move transitions")
    plt.xlabel("Time [s]")
    plt.ylabel(r"Acceleration [$\frac{mm}{s^2}(\frac{rev.}{s^2})$]")
    plt.grid()
    plt.savefig(location + "Plots\\" + rfile + " Acc Y.png")
    print("Plotting Acceleration Y for file: ", rfile)
    plt.close()

print("Saving figs complete!")

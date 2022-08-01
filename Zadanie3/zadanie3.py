import math
import matplotlib.pyplot as plt
n = int(input("Podaj stopień pierwiastka: "))

wartoscix = []
wartosciy = []
for i in range(0, n):
    x = math.cos((2 * i * math.pi) / n)
    y = math.sin((2 * i * math.pi) / n)
    wartoscix.append(x)
    wartosciy.append(y)
fig, ax = plt.subplots(figsize=(9, 6))
plt.xlim([-2, 2])
plt.ylim([-2, 2])
ax.axhline(linewidth=0.7, color="k")
ax.axvline(linewidth=0.7, color="k")
circle = plt.Circle((0, 0), 1, linestyle="dotted", facecolor="w", edgecolor="k", linewidth=1)
ax.add_patch(circle)
if n > 2:
    plt.scatter(wartoscix, wartosciy, c="#8C1E9F", s=50)
    plt.plot(wartoscix, wartosciy, "#8C1E9F")
    plt.plot([wartoscix[0], wartoscix[n-1]], [wartosciy[0], wartosciy[n-1]], "#8C1E9F")
    plt.fill_between(wartoscix, wartosciy, color="#E6A2F2")
    plt.fill_between([wartoscix[0], wartoscix[n-1]], [wartosciy[0], wartosciy[n-1]], color="#E6A2F2")
    plt.grid()
    plt.show()


elif n >= 0 and n <= 2:
    plt.scatter(wartoscix, wartosciy, c="#8C1E9F", s=50)
    plt.plot(wartoscix, wartosciy, "#8C1E9F")
    plt.grid()
    plt.show()

else:
    print("Podałeś złą liczbę.")

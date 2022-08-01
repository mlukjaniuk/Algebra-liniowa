
# Wartości modułu i kąta są zaokrąglone do dwóch miejsc miejsc po przecinku

import matplotlib.pyplot as plt
import math
import numpy as np
rez = int(input("Podaj część rzeczywistą liczby zespolonej: "))
imz = int(input("Podaj część urojoną liczby zespolonej: "))
modul = round(math.sqrt(rez*rez + imz*imz), 2)
kat = round(np.arctan2(imz, rez)*(180/3.14), 2)
fig, ax = plt.subplots(figsize=(10, 6))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.scatter([0, rez], [0, imz])
plt.plot([0, rez], [0, imz])
plt.plot([], [], ' ', label="Wartość modułu:")
plt.plot([], [], ' ', label=modul)
plt.plot([], [], ' ', label="Wartość kąta w stopniach:")
plt.plot([], [], ' ', label=kat)
plt.grid()
plt.legend()
ax.set_xlabel('ReZ')
ax.set_ylabel('ImZ')
plt.xlim([(-math.fabs(rez))*1.5-1, (math.fabs(rez)+1)*1.5+1])
plt.ylim([(-math.fabs(imz))*1.5-1, (math.fabs(imz)+1)*1.5+1])
ax.axhline(linewidth=1, color="k")
ax.axvline(linewidth=1, color="k")
plt.show()

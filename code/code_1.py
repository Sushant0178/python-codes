import matplotlib.pyplot as plt
import numpy as np
# import pyautogui
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
print(mylabels)
plt.pie(y, labels=mylabels)
plt.legend(title="Four Fruits:")
plt.show()

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()


# numpy_hello_world.py
# By: Aidan
# Date: 13/9/2022

import numpy as np
from matplotlib import pyplot as plt

data = np.random.randint(0, 100, 10)
data2 = np.random.randint(0, 100, 10)

plt.plot(data)
plt.plot(data2)
plt.ylabel("Random Values")

plt.show()







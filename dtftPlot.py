#%%
import numpy as np
import matplotlib.pyplot as plt
import math as m

def f(x):
    return abs(4*np.cos(x)/m.sqrt(5+(4*np.cos(x))))

f2 = np.vectorize(f)
x = np.arange(-10, 10, 0.1)
plt.plot(x, f2(x))
plt.grid()
plt.show()



# %%

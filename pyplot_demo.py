import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = range(-10, 11)
y = np.power(x, 3)
plt.plot(x, y, 'g')
plt.title('Third power of x')
y2 = 13 * np.power(x, 2) - y - 1000
plt.plot(x, y2, 'r')
# plt.savefig('demo.png')

plt.figure()
df = pd.read_csv('./data/water.csv')
plt.plot(df['height'])

plt.show()
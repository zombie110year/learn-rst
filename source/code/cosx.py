import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 1000)
y = np.cos(x)
plt.plot(x, y)
plt.title("cos(x)")
# 最后必须要调用 show 方法, 才能显示
plt.show()

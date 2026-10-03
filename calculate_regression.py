import numpy as np
import matplotlib.pyplot as plt

x = np.array([i for i in range(1, 6)])
y = np.array([10.0, 10.5, 11.0, 12.0, 12.5])

x_sum = sum(x)
x_mean = x.mean()
y_sum = sum(y)
y_mean = y.mean()

b = sum((x - x_mean) * (y - y_mean)) / (sum((x - x_mean) ** 2))
a = y_mean - b * x_mean
regr = a + b * 6
print("Regression for 6th year: ", regr)
print()

# calculate polyfit
coefs = np.polyfit(x, y, 1)
p = np.poly1d(coefs)
print("Полифит = ", p)

# drawing
plt.figure(figsize=(7, 5))
plt.scatter(x, y, color='red', s=80, label='Data')
plt.plot(x, a + b * x, color='blue', label='Trend')
plt.scatter(6, regr, color='orange', label='Regression')
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.legend()
plt.grid(alpha=0.5)
plt.show()

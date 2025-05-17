import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)

y1 = x**2            
y2 = np.sin(x)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x, y1, color='blue')
plt.title("Graph of y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x, y2, color='green')
plt.title("Graph of y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.tight_layout()
plt.show()

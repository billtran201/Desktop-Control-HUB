import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points
x = np.linspace(-8, 8, 20)
y = np.linspace(-8, 8, 20)
X, Y = np.meshgrid(x, y)

# Gradient field is constant: F = <4, 3>
U = np.full_like(X, 4)
V = np.full_like(Y, 3)

# Compute the potential function phi = 4x + 3y for level curves
phi = 4 * X + 3 * Y

# Plot setup
plt.figure(figsize=(8, 8))
plt.title("Gradient Field F = ∇φ and Level Curves of φ(x, y) = 4x + 3y")
plt.xlabel("x")
plt.ylabel("y")

# Plot a few level curves
contour_levels = np.arange(-48, 49, 12)  # evenly spaced values
contours = plt.contour(X, Y, phi, levels=contour_levels, colors='blue')
plt.clabel(contours, inline=True, fontsize=10)

# Plot the constant gradient field
plt.quiver(X, Y, U, V, color='red')

# Formatting
plt.grid(True)
plt.axis('equal')
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.show()

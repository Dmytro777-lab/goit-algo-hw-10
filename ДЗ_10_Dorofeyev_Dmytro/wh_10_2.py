import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Define the function to integrate


def f(x):
    return x ** 2


# Integration limits
a = 0  # Lower limit
b = 2  # Upper limit

# Monte Carlo method for integration


def monte_carlo_integrate(f, a, b, num_samples=10000):
    x_samples = np.random.uniform(
        a, b, num_samples)  # Generate random x values
    y_samples = f(x_samples)  # Evaluate function at sampled points
    integral_approx = (b - a) * np.mean(y_samples)  # Approximate integral
    return integral_approx


# Compute integral using Monte Carlo method
monte_carlo_result = monte_carlo_integrate(f, a, b)

# Compute integral using SciPy's quad function
quad_result, error = spi.quad(f, a, b)

# Print results
print(f"Monte Carlo Integration Result: {monte_carlo_result}")
print(f"SciPy Quad Integration Result: {
      quad_result} (Error Estimate: {error})")

# Visualization
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Integration of f(x) = x^2 from {a} to {b}')
plt.grid()
plt.show()

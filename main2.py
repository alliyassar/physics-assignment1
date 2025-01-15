# Required libraries
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.673 * 10**-11  # Gravitational constant (Nm^2/kg^2)
R = 10**5            # Distance between the two masses (m)

# Task 1: Calculate the gravitational force between two masses
M1 = 5 * 10**4        # First mass (kg)
M2 = 25 * 10**4       # Second mass (kg)

# Gravitational force calculation using eval()
force_expression = "G * M1 * M2 / R**2"
F = eval(force_expression)
print(f"Gravitational Force (F): {F} N")

# Task 2: Calculate the gravitational force for varying first mass and plot the relationship
# Define a range of values for the first mass
M1_values = np.linspace(1e4, 1.5e5, 100)  # Between 10,000 kg and 150,000 kg
M2 = 2.5e4                                # Second mass remains constant (kg)

# Gravitational force calculation for each value of M1 using eval()
force_values_expression = "G * M1_values * M2 / R**2"
F_values = eval(force_values_expression)

# Create a plot
plt.figure(figsize=(8, 6))
plt.plot(M1_values, F_values, label='Force vs Mass 1', linewidth=2)
plt.title('Gravitational Force vs First Mass', fontsize=14)
plt.xlabel('Mass 1 (kg)', fontsize=12)
plt.ylabel('Gravitational Force (N)', fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()

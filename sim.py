import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import hbar

# Determine the parameters for the infinite square well
n = 5
L = 10
electron_mass = 9.10938356e-31  # Mass of an electron in kg

# Time-independent schrodinger for infinite square well
def psi(x, n, L):
    """Wavefunction for the infinite square well."""
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

# Quantized energy level
def energy(n, L, m):
    """Energy levels for the infinite square well."""
    return (n**2 * np.pi**2 * hbar**2) / (2 * electron_mass * L**2)

# Determine coordinate system in term of wave function (psi) and position (x) within the domain of the infinite square well
x = np.linspace(0, L, 1000) 
y = psi(x, n, L)

# Plot the wavefunction
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f'Wavefunction n={n}', color='blue')
plt.title('Wavefunction for Infinite Square Well')
plt.xlabel('Position (x)')
plt.ylabel('Wavefunction (ψ)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.axvline(L, color='black', lw=0.5, ls='--')
plt.xlim(0, L)
plt.ylim(-1.5, 1.5)
plt.legend()
plt.grid()
plt.show()
print(f"Energy level for n={n}: {energy(n, L, electron_mass)} J")


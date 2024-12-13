import numpy as np


n = 4
omega = 4.53

poles = []
for i in range(1, 2 * n + 1):
    theta = np.pi / 2 + (2 * i - 1) * np.pi / (2 * n)
    pole = omega * (np.cos(theta) + 1j * np.sin(theta))
    poles.append(pole)

for idx, pole in enumerate(poles, start=1):
    print(f"Pole {idx}: {pole.real:.4f} {pole.imag:.4f}j")
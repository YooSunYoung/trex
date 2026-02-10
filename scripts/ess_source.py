import matplotlib.pyplot as plt
import numpy as np
import tof

source = tof.Source(facility="ess", neutrons=1_000_000)
print(source.data)

x = source.data.coords["birth_time"].values[0]
y = source.data.coords["wavelength"].values[0]
xedges = np.linspace(0, 5000, 100)
yedges = np.linspace(0, 5, 100)
H, xedges, yedges = np.histogram2d(x, y, bins=(xedges, yedges))

fig, ax = plt.subplots()
ax.pcolormesh(xedges, yedges, H.T, cmap="jet")
ax.set_xlabel(f'Birth time [{source.data.coords["birth_time"].unit}]')
ax.set_ylabel(f'Wavelength [{source.data.coords["wavelength"].unit}]')
ax.set_title("ESS Source Neutron Birth Time vs Wavelength")
ax.grid(alpha=0.6)
plt.show()

import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
import numpy as np

# Creamos una figura y un eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Creamos los datos para el eje X (fechas de lanzamiento) y el eje Y (energía necesaria)
launch_dates = np.arange(0, 365, 30)
energies = np.arange(1000, 10000, 1000)
X, Y = np.meshgrid(launch_dates, energies)

# Calculamos el coste en dólares de la misión en función de la fecha de lanzamiento y la energía necesaria
cost = X + Y

# Graficamos el coste en un eje Z
ax.plot_surface(X, Y, cost, cmap=cm.coolwarm, alpha=0.5)

# Añadimos etiquetas a los ejes
ax.set_xlabel("Fecha de lanzamiento (días)")
ax.set_ylabel("Energía necesaria (kJ)")
ax.set_zlabel("Coste de la misión (dólares)")

# Mostramos el gráfico
plt.show()
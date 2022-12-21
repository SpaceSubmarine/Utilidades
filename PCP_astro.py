import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Datos de la órbita de la Tierra y Marte
earth_orbit = {
    "semi_major_axis": 1.0,  # UA
    "eccentricity": 0.0167,
    "inclination": 0.0,  # Grados
    "longitude_of_ascending_node": 0.0,  # Grados
    "argument_of_periapsis": 0.0,  # Grados
    "mean_anomaly": 0.0  # Grados
}

mars_orbit = {
    "semi_major_axis": 1.524,  # UA
    "eccentricity": 0.0934,
    "inclination": 1.850,  # Grados
    "longitude_of_ascending_node": 49.578,  # Grados
    "argument_of_periapsis": 286.502,  # Grados
    "mean_anomaly": 19.441  # Grados
}

# Creamos el gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generamos una malla de puntos para representar la energía necesaria para trasladarnos entre la Tierra y Marte
energies = []
time_of_flights = []
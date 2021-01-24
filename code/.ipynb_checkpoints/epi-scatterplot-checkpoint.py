import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = np.genfromtxt("epi-data.csv", delimiter=";", skip_header=1)
         
nb_points = 4003

data_x = np.array(data[:, 3], dtype=int)
data_y = np.array(data[:, 2], dtype=int)

# np.set_printoptions(threshold=sys.maxsize)
data = np.column_stack((data_x, data_y))
plt.ylabel("Surface Carrez (m²)")
plt.xlabel("Valeur (millions d'euros)")
plt.plot(data[:, 0], data[:, 1], "o", markersize=1)
plt.savefig("scatter plot.pdf")

nb_points = data.shape[0]

"""
    Compute center
"""
center = np.mean(data, axis=0)

"""
    Compute mean distance to center with euclidean metric
"""
metric = "euclidean"
differences = data-center
distances_to_center = np.linalg.norm(differences, axis=1)
mean_distance_to_center = distances_to_center.sum()/len(distances_to_center)

nb_outliers = 0
for index in range(nb_points):
    datapoint = data[index]
    vector_to_center = datapoint-center
    distance_to_center = np.linalg.norm(vector_to_center)
    if distance_to_center > 3*mean_distance_to_center:
        print(datapoint)
        print(distance_to_center/mean_distance_to_center)
        print("")
        plt.plot(datapoint[0], datapoint[1], "o", color="red", markersize=1.5)
        nb_outliers += 1
print(f"{nb_outliers} outliers")


plt.title(f"outliers in red, {metric} metric")
plt.savefig(f"outliers, metric={metric}.pdf")
plt.close()

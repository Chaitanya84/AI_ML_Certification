import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# 1-D data points (reshape into 2D for scipy usage)
points = np.array([1, 2, 4, 5, 8, 10, 11, 12]).reshape(-1,1)

# Single Linkage (Minimum distance)
Z_single = linkage(points, method='single')

# Complete Linkage (Maximum distance)
Z_complete = linkage(points, method='complete')

# Plot dendrograms side-by-side
plt.figure(figsize=(14,6))

plt.subplot(1,2,1)
dendrogram(Z_single, labels=[str(p[0]) for p in points])
plt.title("Hierarchical Clustering (Single Linkage - MIN Distance)")
plt.xlabel("Data Points")
plt.ylabel("Distance")

plt.subplot(1,2,2)
dendrogram(Z_complete, labels=[str(p[0]) for p in points])
plt.title("Hierarchical Clustering (Complete Linkage - MAX Distance)")
plt.xlabel("Data Points")
plt.ylabel("Distance")

plt.tight_layout()
plt.show()

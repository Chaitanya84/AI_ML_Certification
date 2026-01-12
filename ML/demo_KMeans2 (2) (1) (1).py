import numpy as np
import matplotlib.pyplot as plt

# Data points
points = np.array([
    [1, 1], [3, 3], [4, 5], [5, 5], [6, 6], 
    [9, 9], [0, 3], [3, 0], [2, 2]
])

# Initial centroids
centroids = np.array([[2, 1], [2, 3], [4, 5]])

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2, axis=1))

# Run KMeans for 3 iterations
num_iterations = 3
for i in range(num_iterations):
    # Step 1: Assign points to the closest centroid
    clusters = {}
    for j in range(len(centroids)):
        clusters[j] = []

    for point in points:
        distances = euclidean_distance(centroids, point)
        cluster_idx = np.argmin(distances)
        clusters[cluster_idx].append(point)

    # Step 2: Update centroids
    new_centroids = np.array([np.mean(clusters[k], axis=0) for k in clusters])

    # Compute SSE (Sum of Squared Errors) for each cluster
    SSE_cluster = []
    for k in clusters:
        cluster_points = np.array(clusters[k])
        sse_k = np.sum((cluster_points - new_centroids[k])**2)
        SSE_cluster.append(sse_k)

    # Compute total SSE
    total_SSE = sum(SSE_cluster)

    # Display Iteration Results
    print("\nIteration", i+1)
    print("Centroids Used for SSE Calculation:")
    print(new_centroids)
    print("SSE for each cluster:", SSE_cluster)
    print("Total SSE:", total_SSE)

    centroids = new_centroids  # Update centroids

# Final Clustering Plot
colors = ['r', 'g', 'b']
plt.figure(figsize=(8,6))

for k in clusters:
    cluster_points = np.array(clusters[k])
    plt.scatter(cluster_points[:,0], cluster_points[:,1], color=colors[k], label='Cluster ' + str(k+1))
    plt.scatter(centroids[k,0], centroids[k,1], color='black', marker='X', s=200, label='Centroid ' + str(k+1))

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Final Clustering after 3 Iterations")
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # 1-unit grid lines
plt.xticks(np.arange(0, 11, 1))  # X-axis 1-unit spacing
plt.yticks(np.arange(0, 11, 1))  # Y-axis 1-unit spacing
plt.show()

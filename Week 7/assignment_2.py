import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Normalization function
def getNormalizedArray(dataArray):
    rows, cols = dataArray.shape
    normalizedArray = np.zeros_like(dataArray)

    for colIndex in range(cols):
        colElements = dataArray[:, colIndex]
        xMin = np.min(colElements)
        xMax = np.max(colElements)
        normalizedArray[:, colIndex] = (dataArray[:, colIndex] - xMin) / (xMax - xMin)
    
    return normalizedArray

# Euclidean Distance Calculation
def calculateEuclideanDistances(normalizedArray, centroids, K):
    rows, cols = normalizedArray.shape
    distances = np.zeros((rows, K))
    for i in range(K):
        distances[:, i] = np.sqrt(np.sum((normalizedArray - centroids[i]) ** 2, axis=1))
    return distances

# Assign Clusters
def assignClusters(distances, centroids, normalizedArray):
    clusters = np.argmin(distances, axis=1)
    newCentroids = np.zeros_like(centroids)
    
    for i in range(centroids.shape[0]):
        points = normalizedArray[clusters == i]
        if len(points) > 0:  # Avoid empty cluster issues
            newCentroids[i] = points.mean(axis=0)
    
    return clusters, newCentroids

# Plotting function
def plotClusters(normalizedArray, clusters, centroids, K):
    plt.figure(figsize=(10, 7))

    # Plot all points colored by cluster
    for i in range(K):
        plt.scatter(normalizedArray[clusters == i][:, 0], normalizedArray[clusters == i][:, 1], label=f'Cluster {i+1}')
    
    # Plot centroids
    plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='black', marker='X', label='Centroids')

    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.title('K-Means Clustering')
    plt.grid(True)
    plt.show()

# Apply K-means Clustering
def applyKMC(dataArray, K):
    # Normalize the data
    normalizedArray = getNormalizedArray(dataArray)

    # Randomly initialize centroids
    rows, cols = dataArray.shape
    random_indices = np.random.choice(rows, K, replace=False)
    centroids = normalizedArray[random_indices]
    print('Initial Centroids:')
    print(centroids)
    
    newCentroids = np.zeros_like(centroids)
    while not np.array_equal(centroids, newCentroids):
        centroids = newCentroids.copy()  # Update centroids for next iteration

        # Calculate distances from centroids
        distances = calculateEuclideanDistances(normalizedArray, centroids, K)

        # Assign clusters and update centroids
        clusters, newCentroids = assignClusters(distances, centroids, normalizedArray)

    print('Final Centroids:')
    print(newCentroids)

    # Plot the results
    plotClusters(normalizedArray, clusters, newCentroids, K)

# Usage
dataFile = 'KMC_student_dataset.xlsx'
dataFrame = pd.read_excel(dataFile)
dataArray = np.array(dataFrame).astype(float)

k = 3
applyKMC(dataArray, k)

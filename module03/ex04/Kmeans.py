import sys
import numpy as np
from csvreader import CsvReader
import matplotlib.pyplot as plt
import itertools


class KmeansClustering:
    def __init__(self, ncentroid=4, max_iter=30):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            None.
        Raises:
            This function should not raise any Exception.
        """
        self.centroids = X[np.random.choice(X.shape[0], size=self.ncentroid, replace=False)]
        print("initial centroids {}".format(self.centroids))
        if X.shape[0] < self.ncentroid:
            return None
        positions = []
        for i in range(self.max_iter):
            clusters = [[] for _ in range(self.ncentroid)]
            for row in X:
                nearest = False
                for j, centroid in enumerate(self.centroids):
                    distance = np.linalg.norm(centroid - row, 1)
                    if not nearest or distance < nearest[1]:
                        nearest = (j, distance)
                clusters[nearest[0]].append(row)
            # Save positions history to get a line from start to finish for each clusters
            current_positions = []
            for j, cluster in enumerate(clusters):
                matrix = np.array(cluster)
                self.centroids[j] = np.mean(matrix, axis=0)
                current_positions.append(self.centroids[j].tolist())
            positions.append(current_positions)
            if i >= 1 and positions[i - 1] == positions[i]:
                break
        return np.array(positions)

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        smallest weight -> Venus
        biggest height + smallest bone density -> Belt
        biggest height -> Mars
        remaining -> Earth
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
            This function should not raise any Exception.
        """
        if self.ncentroid != 4:
            return None
        res = []
        for row in X:
            nearest = False
            for j, centroid in enumerate(self.centroids):
                distance = np.linalg.norm(centroid - row, 1)
                if not nearest or distance < nearest[1]:
                    nearest = (j, distance, row)
            res.append(nearest[0])
        return np.array(res)

    def match_clusters(self):
        # TODO: Missing which clusters belong to which Solar Citizen
        # TODO: Check the values for each clusters
        # TODO: Dataset [height, weight, bone_density]
        # TODO: Belt: biggest mean height + Lowest bone density
        # TODO: Mars: second mean height
        # TODO: Venus: Lowest mean weights of the remaining
        # TODO: Earth: remaining cluster
        pass


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc != 4:
        print('Missing or too many arguments')
        print("Usage: Kmeans.py filepath='solar_system_census.csv' ncentroid=4 max_iter=30")
        exit()
    dataset_path, ncentroid, max_iter = sys.argv[1:]
    # Parse arguments
    try:
        ncentroid = int(ncentroid)
        if ncentroid < 2:
            raise ValueError("ncentroid should be >= 2")
    except BaseException:
        print("Invalid ncentroid `{}`".format(ncentroid))
    try:
        max_iter = int(max_iter)
        if max_iter < 0:
            raise ValueError("max_iter should be positive")
    except BaseException:
        print("Invalid max_iter `{}`".format(max_iter))
    # Open dataset
    dataset = False
    with CsvReader(dataset_path) as file:
        if file is None:
            print('Failed to read dataset')
            exit()
        dataset = np.array(file.getdata(), dtype='float')
    if dataset is False or len(dataset.shape) != 2 and dataset.shape[1] != 4:
        print('Invalid dataset')
        exit()
    # Remove "ID" column
    dataset = np.delete(dataset, 0, axis=1)
    # Fit and show results !
    kmeans = KmeansClustering(ncentroid=ncentroid, max_iter=max_iter)
    history = kmeans.fit(dataset)
    print("history", history)
    predictions = kmeans.predict(dataset)
    # Show the results
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    cmap = plt.cm.get_cmap('tab20c', ncentroid)
    markers = ['+', ',', 'o', '^']
    for i, value in enumerate(dataset):
        z, x, y = value
        ax.scatter3D(x, y, z, s=20, marker=markers[predictions[i] % 4], color=cmap(predictions[i]))
    for i in range(ncentroid):
        # Select the i-th row of the positions history
        line = history[0:, i]
        z, x, y = line[:, 0], line[:, 1], line[:, 2]
        ax.plot3D(x, y, z, color=cmap(i))
        last_z, last_x, last_y = z[-1], x[-1], y[-1]
        print("({}) last is {}".format(i, last_z))
        ax.scatter3D(last_x, last_y, last_z, s=60, marker=markers[predictions[i] % 4], color=cmap(i))
    plt.show()

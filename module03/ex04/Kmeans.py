import sys
import argparse
import numpy as np
from csvreader import CsvReader
import matplotlib.pyplot as plt


class KmeansClustering:
    def __init__(self, max_iter=30, ncentroid=4):
        if not isinstance(ncentroid, int) or ncentroid < 1:
            raise ValueError('ncentroid should be a positive number')
        if not isinstance(max_iter, int) or max_iter < 1:
            raise ValueError('max_iter should be a positive number')
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def fit(self, X: np.ndarray):
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
        if not isinstance(X, np.ndarray):
            return None
        if len(X.shape) != 2:
            return None
        self.centroids = X[np.random.choice(X.shape[0], size=self.ncentroid, replace=False)]
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

    def predict(self, X: np.ndarray):
        """
        Predict from wich cluster each datapoint belongs to.
        smallest weight -> Venus
        biggest height + smallest bone density -> Belt
        biggest height -> Mars
        remaining -> Earth
        Dataset: height,weight,bone_density
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(X, np.ndarray):
            return None
        if len(X.shape) != 2:
            return None

        # Map citizens to clusters
        clusters_citizens = [[] for _ in range(self.ncentroid)]
        citizens = []
        for row in X:
            nearest = False
            for j, centroid in enumerate(self.centroids):
                distance = np.linalg.norm(centroid - row, 1)
                if not nearest or distance < nearest[1]:
                    nearest = (j, distance, row)
            clusters_citizens[nearest[0]].append(row)
            citizens.append(nearest[0])
        citizens = np.array(citizens)

        if self.ncentroid != 4:
            return [citizens, []]

        # Map clusters to planets
        planets = dict()
        # Calculate all columns means per clusters
        cluster_means = np.array(
            [np.mean(np.array(cluster_citizens), axis=0) for cluster_citizens in clusters_citizens]
        )
        original_clusters = cluster_means.copy()
        # Lowest weight
        lowest_weight = cluster_means[:, 1].argmin()
        planets["Venus"] = cluster_means[lowest_weight]
        cluster_means = np.delete(cluster_means, lowest_weight, axis=0)
        # Bone density + Height
        biggest_height = cluster_means[:, 0].argmax()
        lowest_bone = cluster_means[:, 2].argmin()
        selected = None
        if biggest_height == lowest_bone:
            selected = biggest_height
        else:
            planets["Mars"] = cluster_means[biggest_height]
            cluster_means = np.delete(cluster_means, biggest_height, axis=0)
            selected = lowest_bone
        planets["Belt"] = cluster_means[selected]
        cluster_means = np.delete(cluster_means, selected, axis=0)
        # Mars
        if "Mars" not in planets:
            biggest_height = cluster_means[:, 0].argmax()
            planets["Mars"] = cluster_means[biggest_height]
            cluster_means = np.delete(cluster_means, biggest_height, axis=0)
        # Remaining is earth
        planets["Earth"] = cluster_means[0]

        # Map planets to an index
        indexed_planets = [False, False, False, False]
        for i, row in enumerate(original_clusters):
            for key, value in planets.items():
                if np.array_equal(value, row):
                    indexed_planets[i] = key
                    break
        return [citizens, indexed_planets]


if __name__ == '__main__':
    argc = len(sys.argv)

    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Dataset path')
    parser.add_argument('ncentroid', help='Amount of centroids', type=int, default=4)
    parser.add_argument('max_iter', help='Maximum number of iterations', type=int, default=30)
    args = parser.parse_args()

    dataset_path = args.filepath
    ncentroid = args.ncentroid
    max_iter = args.max_iter

    # Check arguments
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
    [predictions, planets] = kmeans.predict(dataset)
    print("predictions", predictions)
    print("planets", planets)

    # Show the results
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_xlabel("Height")
    ax.set_ylabel("Weight")
    ax.set_zlabel("Bone Density")
    cmap = plt.cm.get_cmap('tab20c', ncentroid)
    markers = ['+', ',', 'o', '^']
    for i, value in enumerate(dataset):
        x, y, z = value
        ax.scatter3D(x, y, z, s=20, marker=markers[predictions[i] % 4], color=cmap(predictions[i]))
    for i in range(ncentroid):
        # Select the i-th row of the positions history
        line = history[0:, i]
        x, y, z = line[:, 0], line[:, 1], line[:, 2]
        ax.plot3D(x, y, z, color=cmap(i))
        last_x, last_y, last_z = x[-1], y[-1],  z[-1]
        if ncentroid == 4:
            ax.scatter3D(last_x, last_y, last_z, s=60, marker=markers[predictions[i] % 4], color=cmap(i), label=planets[predictions[i]])
        else:
            ax.scatter3D(last_x, last_y, last_z, s=60, marker=markers[predictions[i] % 4], color=cmap(i))
    if ncentroid == 4:
        plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1, title='Planets')
    plt.show()

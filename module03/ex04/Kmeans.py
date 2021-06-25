import numpy as np


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
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
        self.centroids = X[np.random.choice(
            X.shape[0], size=self.ncentroid, replace=False)]
        if X.shape[0] < self.ncentroid:
            return None
        for i in range(self.max_iter):
            clusters = list([] for i in range(self.ncentroid))
            current_distances = []

            for row in X:
                nearest = False
                for j, centroid in enumerate(self.centroids):
                    distance = np.linalg.norm(centroid - row, 1)
                    if not nearest or distance < nearest[1]:
                        nearest = (j, distance)
                clusters[nearest[0]].append(row)

            for j, cluster in enumerate(clusters):
                matrix = np.array(cluster)
                self.centroids[j] = np.mean(matrix, axis=0)

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
        res = []
        for row in X:
            nearest = False
            for j, centroid in enumerate(self.centroids):
                distance = np.linalg.norm(centroid - row, 1)
                if not nearest or distance < nearest[1]:
                    nearest = (j, distance, row)
            res.append(nearest[0])
        # TODO: Missing which clusters belong to which Solar Citizen
        return np.array(res)

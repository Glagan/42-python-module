import numpy as np


class ColorFilter:
    def invert(self, array: np.ndarray) -> np.ndarray:
        """
        Inverts the color of the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        array = 0 + array  # copy
        array[:, :, :3] = 1 - array[:, :, :3]
        return array

    def to_red(self, array: np.ndarray) -> np.ndarray:
        """
        Applies a red filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        array = 0 + array  # copy
        array[:, :, :3] = array[:, :, :3] - self.to_green(array)[:, :, :3] - self.to_blue(array)[:, :, :3]
        return array

    def to_green(self, array: np.ndarray) -> np.ndarray:
        """
        Applies a green filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        array = 1 * array  # copy
        array[:, :, :3] = array[:, :, :3] * [0, 1, 0]
        return array

    def to_blue(self, array: np.ndarray) -> np.ndarray:
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        (x, y, c) = array.shape
        copy = np.zeros((x, y))  # copy
        array = np.dstack((copy, array[:, :, :]))  # copy
        blue = np.zeros((x, y, 2))
        if c == 4:
            return np.dstack((blue, array[:, :, 3:]))
        return np.dstack((blue, array[:, :, 3]))

    def to_celluloid(self, array: np.ndarray, shades: int = 4) -> np.ndarray:
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(shades, int):
            return None
        if shades < 4 or shades > 255:
            return None
        array = array.copy()
        limits = np.linspace(0, 1, shades + 1)
        for i in range(1, shades):
            array[(array > limits[i - 1]) & (array < limits[i])] = limits[i]
        return array

    def to_grayscale(self, array: np.ndarray, filter: str = 'w', *args, **kwargs) -> np.ndarray:
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = `mean` / `m`: performs the mean of RBG channels.
        For filter = `weight` / `w`: performs a weighted mean of RBG channels.
        Args:
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in [`m`,`mean`,`w`,`weight`]
            weights: [kwargs] list of 3 floats where the sum equals to 1,
            corresponding to the weights of each RBG channels.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if filter not in ['w', 'weight', 'weighted', 'm', 'mean']:
            return None
        if filter == 'mean' or filter == 'm':
            # (R + G + B) / 3
            array = 1 * array  # copy
            average = np.sum(array[:, :, :3], axis=2) / 3
            if array.shape[2] == 4:
                return np.dstack((average, average, average, array[:, :, 3]))
            return np.dstack((average, average, average))
        elif filter == 'weight' or filter == 'weighted' or filter == 'w':
            # (R * 0.299) + (G * 0.587) + (B * 0.114)
            if 'weights' in kwargs:
                weights = kwargs['weights']
                if not isinstance(weights, list):
                    return None
                if len(weights) != 3 or sum(weights) != 1:
                    return None
            else:
                weights = [0.299, 0.587, 0.114]
            array = 1 * array  # copy
            average = np.sum(array[:, :, :3] * weights, axis=2) / 3
            if array.shape[2] == 4:
                return np.dstack((average, average, average, array[:, :, 3]))
            return np.dstack((average, average, average))
        return None

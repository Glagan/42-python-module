import numpy as np


# TODO Handle transparency
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
        return 1 - array

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
        return array - self.to_green(array) - self.to_blue(array)

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
        return array * [0, 1, 0]

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
        # TODO ?????????????
        return array * [0, 0, 1]

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
        # TODO ??????????????
        limits = np.linspace(0, 1, shades)
        array[array < limits[0]] = limits[0]
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
        if filter not in ['w', 'weighted', 'm', 'mean']:
            return None
        # TODO ??????????????
        if filter == 'mean' or filter == 'm':
            # (R + G + B) / 3
            average = np.sum(array, axis=2) / 3
            return np.reshape(np.repeat(average, 3, axis=1), array.shape)
        elif filter == 'weighted' or filter == 'w':
            # (R * 0.299) + (G * 0.587) + (B * 0.114)
            if 'weights' in kwargs:
                weights = kwargs['weights']
                if not isinstance(weights, list):
                    return None
                if len(weights) != 3 or sum(weights) != 1:
                    return None
            else:
                weights = [0.299, 0.587, 0.114]
            weighted = np.sum(array * weights, axis=2)
            return np.reshape(np.repeat(weighted, 3, axis=1), array.shape)
        return None

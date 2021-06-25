import numpy as np


class ColorFilter:
    def invert(self, array):
        return 1 - array

    def to_blue(self, array):
        return array * [0, 0, 1]  # .zeros and .shape ???

    def to_green(self, array):
        return array * [0, 1, 0]

    def to_red(self, array):
        # return array * [1, 0, 0]
        return array - self.to_green(array) - self.to_blue(array)

    def to_celluloid(self, array, shades=4):
        # TODO: This should not be grayscaled...
        average = np.sum(array, axis=2) / 3
        shaded = np.round(average)
        return np.reshape(np.repeat(shaded, 3, axis=1), array.shape)

    def to_grayscale(self, array, filter='w'):
        if filter == 'mean' or filter == 'm':
            # TODO: I don't know
            # (R + G + B) / 3
            average = np.sum(array, axis=2) / 3
            return np.reshape(np.repeat(average, 3, axis=1), array.shape)
        elif filter == 'weighted' or filter == 'w':
            # TODO: It's burning, I don't know what's wrong here
            # (R * 0.299) + (G * 0.587) + (B * 0.114)
            weighted = array * [0.299, 0.587, 0.114]
            weighted = np.sum(array, axis=2)
            return np.reshape(np.repeat(weighted, 3, axis=1), array.shape)
        return array

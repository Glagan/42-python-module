import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image


class ImageProcessor:
    def load(self, path: str) -> np.ndarray:
        if path is None:
            return None
        try:
            im = image.imread(path)
            print('Loading image of dimensions {} x {}'.format(*im.shape[0:2]))
            return im
        except IOError as err:
            print('Could not load image: {}'.format(err))
        return None

    def display(self, arr: np.ndarray) -> None:
        plt.imshow(arr)
        plt.show()

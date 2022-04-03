from matplotlib import pyplot as plt
from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter

print("# Tests")

imp = ImageProcessor()
arr = imp.load("../resources/elon.png")
print(arr.shape)
# Output
# Loading image of dimensions 200 x 200

cf = ColorFilter()
# imp.display(cf.invert(arr))
# imp.display(cf.to_green(arr))
# imp.display(cf.to_red(arr))
# imp.display(cf.to_blue(arr))
# imp.display(cf.to_celluloid(arr))
# imp.display(cf.to_grayscale(arr, 'm'))
# imp.display(cf.to_grayscale(arr, 'weight'))
# imp.display(cf.to_grayscale(arr, 'weight', weights=[0.2, 0.3, 0.5]))

print("\n# Scale")

cf = ColorFilter()

for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert]:
    array = plt.imread("../resources/elon.png")
    plt.imshow(f(array))
    plt.show()

im = cf.to_grayscale(array, "m")
plt.imshow(im, cmap="gray")
plt.show()

im = cf.to_grayscale(array, "w", weights=[0.2126, 0.7152, 0.0722])
plt.imshow(im, cmap="gray")
plt.show()

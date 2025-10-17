from PIL import Image
import imageio
import numpy as np
from matplotlib import image
from matplotlib import pyplot


##Asenna kirjastot:
## pip3 install imageio
## pip3 install matplotlib
## pip3 install numpy
## pip3 install PIL


## Ei tarvitse osata ohjelmoida konvoluutiota, mutta
## tensorin ajatus pitää oppia ymmärtämään.


def process_convolution(img, kernel):
  result_img = img.copy()
  width, height, color = img.shape
  print(width, height, color)
  kernelw, kernelh = kernel.shape
  for c in range(color):
    for w in range(1, width - 1):
      for h in range(1, height - 1):
        summa = 0
        for w2 in range(kernelw):
          for h2 in range(kernelh):
            summa += img[w + w2 - 1, h + h2 - 1, c] * kernel[w2, h2]
        result_img[w + w2 - 1, h + h2 - 1, c] = summa
  return (result_img)


def get_blur_kernel():
  return np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9


def get_edge_detection_kernel():
  return np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])


def get_emboss_kernel():
  return np.array([[0, 1, 0], [0, 0, 0], [0, -1, 0]])


#image_file_path = '../images/perhonens.bmp'
image_file_path = '../images/lena.bmp'
# load the image
imageToProcess = imageio.imread(image_file_path, mode='RGB')
# convert image to numpy array
canvas = np.asarray(imageToProcess)
print(canvas.shape)
#kuva = imread(image_file_path, False)

kernel = get_emboss_kernel()
resultImage = Image.fromarray(process_convolution(canvas, kernel))

# display the array of pixels as an image
pyplot.imshow(resultImage)
#pyplot.imshow(kuva)

pyplot.show()

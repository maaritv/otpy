from PIL import Image
from numpy import asarray
from matplotlib import image
from matplotlib import pyplot
import numpy as np

## Tämä ohjelmakoodi tiedoksi.
## Tutustu miten käydään numpyllä läpi matriisi.
## ei tarvitse osata itse tehdä vastaavaa.

def show_image(imageToShow):
  # summarize shape of the pixel array
  # display the array of pixels as an image
  pyplot.imshow(imageToShow)
  pyplot.show()


##not muuttaa 0:n (musta) valkoiseksi ja 1:n (valkoinen) 0:ksi
def invert(source_array):
  result_array = source_array.copy()
  height, width = source_array.shape
  print(height, width)
  for h in range(0, height - 1):
    for w in range(0, width - 1):
      result_array[h, w] = not source_array[h, w]
  return result_array


image_file_path = '../images/bw.bmp'
# load the image
imageToProcess = Image.open(image_file_path)
# convert image to numpy array
data = asarray(imageToProcess)
print(type(data))
# summarize shape
print(data.shape)
inverted_array = invert(data)

# create Pillow image
resultImage = Image.fromarray(inverted_array)
print(type(resultImage))

# summarize image details
print(resultImage.mode)
print(resultImage.size)
show_image(resultImage)

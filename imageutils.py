import itertools

from PIL import Image


def readBinaryImage(file_name):
   im = Image.open(file_name)
   pixels = list(im.getdata())
   width, height = im.size
   pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

   for i, j in itertools.product(range(height), range(width)):
      pixels[i][j] = int(sum(pixels[i][j]) > 500)
   return pixels
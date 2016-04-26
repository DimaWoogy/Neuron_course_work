import itertools
import colorsys
import numpy

from PIL import Image


def read_binary_image(file_name):
   im = Image.open(file_name)
   pixels = list(im.getdata())
   width, height = im.size
   pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

   for i, j in itertools.product(range(height), range(width)):
      pixels[i][j] = int(sum(pixels[i][j]) > 500)
   return pixels

def save_array_as_image(array, max_val, min_val, output_file):
   res_array = [[(0, 0, 0, 0)]*len(array[0]) for val in array]
   for x in range(len(res_array)):
      for y in range(len(res_array[0])):
         h = (array[x][y] - min_val) / (max_val - min_val) * 120
         r, g, b = colorsys.hsv_to_rgb(h/360, 1., 1.)
         res_array[x][y] = [x * 255 for x in (r, g, b, 0.)]
   im = Image.fromarray(numpy.array(res_array).astype('uint8'))
   im.save(output_file)
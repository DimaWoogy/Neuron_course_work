import itertools
import os
import random
import imageutils

class Neuron(object):
   """Neuron consists implementation of classic neuron model"""
   def __init__(self, size, limit):
      self._weights = [[0] * size[1] for i in range(size[0])]
      self._size = size
      self._limit = limit

   def _fix_weights(self, data, func):
      for i, j in itertools.product(range(self._size[0]), range(self._size[1])):
         self._weights[i][j] = func(data[i][j], self._weights[i][j])

   def get_result(self, data):
      assert len(data) == self._size[0], "different sizes (X) of weights and data"
      assert len(data[0]) == self._size[1], "different sizes (Y) of weights and data"

      result = 0
      for i, j in itertools.product(range(self._size[0]), range(self._size[1])):
         result += data[i][j] * self._weights[i][j]

      return result > self._limit

   def learn(self, data, expected_answer):
      result = self.get_result(data)

      if result == expected_answer:
         return

      incFunc = lambda x, w: w + x
      decFunc = lambda x, w: w - x
      self._fix_weights(data, decFunc if result else incFunc)

      return result

   def get_weights(self):
      return self._weights

a = 'ABCDEFGHIGKLMNOPQR'
k = 5
perms = iter(itertools.product(a, repeat=k))
def get_next_permutation():
   global perms
   val = "".join(next(perms))
   return val

if __name__ == "__main__":
   neuron = Neuron((25, 15), 9)

   images_dir = os.path.join(os.getcwd(), 'images')
   weightsResultDir = os.path.join(images_dir, 'result')
   learnDir = os.path.join(images_dir, 'learn')
   for i in range(10):

      filesList = os.listdir(learnDir)
      random.shuffle(filesList)
      for file_name in filesList:
         file_path = os.path.join(learnDir, file_name)
         data = imageutils.read_binary_image(file_path)
         neuron.learn(data, file_name[0] == '5')
         imageutils.save_array_as_image(neuron.get_weights(), -6, 6,
            os.path.join(weightsResultDir, 'out'+get_next_permutation()+str(i)+'_'+file_name+'.jpg'), data)

   testDir = os.path.join(images_dir, 'test')
   for file_name in os.listdir(testDir):
      file_path = os.path.join(testDir, file_name)
      data = imageutils.read_binary_image(file_path)
      expected_answer = file_name[0] == '5'
      print((neuron.get_result(data), expected_answer))

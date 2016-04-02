import itertools
import os
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

      for data_list, weights_list in zip(data, self._weights):
         for value, weight in zip(data_list, weights_list):
            result += value * weight

      return result > self._limit

   def learn(self, data, expected_answer):
      result = self.get_result(data)

      if result == expected_answer:
         return

      incFunc = lambda x, w: w + x
      decFunc = lambda x, w: w - x
      self._fix_weights(data, decFunc if result else incFunc)

      return result


if __name__ == "__main__":
   neuron = Neuron((25, 15), 9)

   images_dir = os.path.join(os.getcwd(), 'images')

   learnDir = os.path.join(images_dir, 'learn')
   for i in range(10):
      for file_name in os.listdir(learnDir):
         file_path = os.path.join(learnDir, file_name)
         data = imageutils.readBinaryImage(file_path)
         neuron.learn(data, file_name[0] == '5')

   testDir = os.path.join(images_dir, 'test')
   for file_name in os.listdir(testDir):
      file_path = os.path.join(testDir, file_name)
      data = imageutils.readBinaryImage(file_path)
      expected_answer = file_name[0] == '5'
      print((neuron.get_result(data), expected_answer))
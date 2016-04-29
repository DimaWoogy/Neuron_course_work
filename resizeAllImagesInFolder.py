import sys
import os
from PIL import Image

for file_name in os.listdir(sys.argv[1]):
   im = Image.open(os.path.join(sys.argv[1], file_name))
   im = im.resize((480,400), Image.NEAREST)
   im.save(os.path.join(sys.argv[2], file_name))


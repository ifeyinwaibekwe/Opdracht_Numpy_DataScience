import numpy as np
from PIL import Image

class Foto:
    def __init__(self, path):
        self.path = path
    def convertto_array(self):
        image = Image.open(self.path)
        print(f'{self.path} will be transformed to numpy array.')
        return np.array(image)
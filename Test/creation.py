from foto import Foto

import numpy as np
import matplotlib.pyplot as plt

class Creation:
    def __init__(self, inst_foto : Foto ):
        self.np_image = inst_foto.convertto_array()
    def make_matrix(self, rows, columns):
        matrix = np.tile(self.np_image, (rows,columns , 1))  # The 1 means that the number of channels (e.g., RGB) remains unchanged.
        plt.figure(figsize=(5,10))
        plt.imshow(matrix)
        # plt.axis('off')
        plt.show()
    def make_oef2(self, columns):
        vflip = self.np_image[:, ::-1, :]
        hflip = self.np_image[::-1, :, :]
        vhflip = self.np_image[::-1, ::-1, :]
        basis= np.concatenate((self.np_image, vflip, hflip, vhflip), axis = 0)
        oef2 = np.tile(basis, (1, columns, 1 ))
        plt.figure(figsize=(4, 20))
        plt.imshow(oef2)
    def make_oef3(self, factor:int ):  # factor is het aantal rode kolommen, factor has to be an even number !!!!
        try:
            if factor%2!=0 or factor<2:
                raise ValueError(f'choose an even number, higher or equal to 2, instead of {factor}')
            else:
                rood = self.np_image.copy()
                rood[:,:, [1,2] ]=0
                groen= self.np_image.copy()
                groen[:,:, [0,2]]=0
                blauw = self.np_image.copy()
                blauw[:,:, [0,1]]=0
                # figuur vergroten (dubbel = factor4/2)
                hstretch = np.repeat(self.np_image, int(factor-2) , axis= 1)  # heigt stays constant
                vstretch = np.repeat(hstretch, int(factor-2) , axis = 0)
                row_a = np.tile(rood, (1, factor , 1 ))
                row_c = np.tile(blauw , (1, factor, 1))
                im_b = np.tile(groen , (int(factor-2) , 1, 1) )
                row_b = np.concatenate((im_b, vstretch, im_b) , axis = 1)
                oef3 = np.concatenate((row_a, row_b, row_c) , axis= 0)
                plt.figure(figsize= (5,10))
                plt.imshow(oef3)
        except ValueError as ve:
            print(ve)
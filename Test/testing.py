from foto import Foto
from creation import Creation

path1 = 'toekan.jpg'
foto1=Foto(path1)
creation1= Creation(foto1)
creation1.make_matrix(2,10)
creation1.make_oef2(16)
creation1.make_oef3(10)
from PIL import Image
import numpy as np
from textToBinary import textToBinary

string = "hi"

binary = textToBinary(string)

a = np.empty((len(binary), 8))

for i in range(len(binary)):
    for j in range(len(binary[i])):
        if binary[i][j] == '1':
            a[i][j] = 255
        else:
            a[i][j] = 0


            

im = Image.fromarray(a)
im.show()
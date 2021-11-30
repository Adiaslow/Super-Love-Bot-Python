import numpy as np
import matplotlib.pyplot as plt
from random import randint

def mandelbrot(n_rows, n_columns, iterations, cx, cy):
    # generator
    x_cor = np.linspace(-2, 2, n_rows)
    y_cor = np.linspace(-2, 2, n_columns)
    x_len = len(x_cor)
    y_len = len(y_cor)
    output = np.zeros((x_len,y_len))
    c = complex(cx, cy)
    for i in range(x_len):
        for j in range(y_len):
            z = complex(x_cor[i], y_cor[j])
            count = 0
            for k in range(iterations):
                z = (z * z) + c
                count = count + 1
                if (abs(z) > 4):
                    break
            output[i,j] = count
        print(int((i/x_len)*100),"% completed")

    print(output)
    plt.imshow(output.T, cmap='afmhot')
    
    plt.savefig("Julia.tiff", dpi = 3840)
    plt.axis("off")
    
    plt.show()
        
"""       
#randomizer
    
first1 = randint(-100, 100) / 100
first2 = randint(0, 100) / 100
firstOpRand = randint(0,3)
if firstOpRand == 0:
    firstOp = "+"
if firstOpRand == 1:
    firstOp = "-"
if firstOpRand == 2:
    firstOp = "*"
if firstOpRand == 3:
    firstOp = "/"
firstValue = str(first1) + str(firstOp) + str(first2) + 'j'
print(firstValue)
"""
mandelbrot(4000, 4000, 300, -0.42+0.7j, -0.42+0.3j)
import numpy as np 
import matplotlib.pyplot as plt 

def gradient (B, my_color1, my_color2):
    my_shape = B.shape[0]
    r=np.linspace(my_color1[2],my_color2[2],my_shape*2, dtype="uint8")
    g=np.linspace(my_color1[1],my_color2[1],my_shape*2, dtype="uint8")
    b=np.linspace(my_color1[0],my_color2[0],my_shape*2, dtype="uint8")
    k=0
    l=0
    
    for i,color in enumerate(zip(r,g,b)):
        if i<n:
            k=i
            for j in range(k+1):
                B[i, j]=color
                i=i-1
            i=k
        if i>=n:
            k=i
            i=n-1
            l=l+1
            j=l
            while j != n:
                B[i, j]=color
                i=i-1
                j=j+1
            i=k
    return B


color1= [255,128,0]
color2= [0,128,255]
size = 100
image=np.zeros((size, size, 3), dtype="uint8")

gradient(image, color1, color2)

plt.figure(1)
plt.imshow(image)
plt.show()
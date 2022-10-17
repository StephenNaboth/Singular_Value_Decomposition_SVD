# -*- coding: utf-8 -*-
"""
Author: Stephen
application of Singular Value Decomposition SVD in image compression



"""

# Commented out IPython magic to ensure Python compatibility.
from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
plt.rcParams['figure.figsize'] = [16, 10]
path = r"./images/landscape.jpg"

A = cv.imread(path) # or use -- imread(pathfull_matrices=#X = np.mean(A, -1);
X =  cv.cvtColor(A, cv.COLOR_BGR2GRAY) # convert to gray
img = plt.imshow(256 - X) # negative
img.set_cmap('gray')
plt.axis("off")
plt.show()

# Perform SVD
U, S, V_t = np.linalg.svd(X, full_matrices = False)

#U.shape, S.shape, V_t.shape

S = np.diag(S)

j =0
for r in [5 , 10 , 20]: 
    # approximation of X
    X_appr = U[:, :r] @ S[:r, :r] @ V_t[:r, :]
    plt.figure(j+1)
    j += 1
    img = plt.imshow(250 - X_appr)
    img.set_cmap('gray')
    plt.axis('off')
    plt.title(f"r = {r}")
    plt.show()

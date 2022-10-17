# **Singular Value Decompostion application to Image Compression**

The singular value decomposition (SVD) is an important matrix
factorization technique that provides a numerically stable matrix
decomposition that can be used for a variety of purposes such as to obtain low-rank approximations to matrices and to perform pseudo-inverses of non-square matrices to find the solution of a system
of equations $\text{Ax = b}$. 

Generally, we are interested in analyzing a large data set $X \in \mathbb{C}^{n\times m}$.
$$
\mathbf{X}=\left[\begin{array}{cccc}
\mid & \mid & & \mid \\
\mathbf{x}_1 & \mathbf{x}_2 & \cdots & \mathbf{x}_m \\
\mid & \mid & & \mid
\end{array}\right]
$$

For many systems $n \gg m$, resulting in a tall-skinny matrix, as opposed to a short-fat matrix when $n \ll m$. 
The SVD is a unique matrix decomposition that exists for every complex valued
matrix $X \in \mathbb{C}^{n\times m}$:
$$
\mathrm{X} = \mathrm{U\Sigma V}^*
$$
where $U  \in \mathbb{C}^{n\times n}$ and $V  \in \mathbb{C}^{m\times m}$ are unitary matrices with orthonormal columns, and $ \mathrm{\Sigma} \in \mathbb{C}^{n\times m} $ is a matrix with real, non-negative entries on the diagonal and
zeros off the diagonal.

When $n \geq m$, the matrix $\mathrm{\Sigma}$ has at most m non-zero elements on the diagonal, and may be written as
$
\boldsymbol{\Sigma}=\left[\begin{array}{l}
\hat{\Sigma} \\
0
\end{array}\right] \text {. }
$ Therefore, it is possible to exactly
represent X using the economy SVD:
$$
\mathrm{X} = \mathrm{U\Sigma V}^* = \left[\begin{array}{ll}
\hat{U} & \hat{U}^{\perp}
\end{array}\right]\left[\begin{array}{c}
\hat{\Sigma} \\
0
\end{array}\right] \mathrm{V}^* = \hat{U}\hat{\Sigma}\hat{V}^*
$$

We consder the image of a guy with beautiful landscape behind as shown below This image has 8192 by 5461 pixels.

Original                            |     Gray
:----------------------------------:|:----------------------------------------:
![landscape](/images/landscape.jpg) |  ![landscape_gray](/images/landscape_gray.png)


We apply the svd code on this image:

*   install necessary files in requirements.txt
*   run the svd.py 
*   The plots below show truncation of the columns to when r = 5, 10, 20 


r =5                          |    r =10                         | r=20
:----------------------------:|:--------------------------------:|:-------------------:
![r_5](/images/img_5.png)|![r_10](/images/img_10.png)  | ![r_20](/images/img_20.png) 


Plot the diagonal singular values:
*     Run the scd_analysis.py code
The result

![singular values](/images/singular_values_plot.png)

Test for around 90% of the cummulative energy where r = 1200. we get:


![r_1200](/images/img_1200.png)


The above steps can be done in the matlab file. Just by running SVD_1.m

.That's all. Thank You

import matplotlib.pyplot as plt
import numpy as np
import svd
U = svd.U
S = svd.S
V_t = svd.V_t

# anaysis 
plt.figure(figsize=[16,6])
plt.semilogy(np.diag(S))
plt.title("Singular values")
plt.show()

plt.figure(figsize=[16,6])
plt.plot(np.cumsum(np.diag(S))/np.sum(np.diag(S)))
plt.plot(1200, np.sum(np.diag(S[:1200,:1200]))/np.sum(np.diag(S)), marker='*', ls='none', ms=20, label='line with select markers')
plt.title("Singular values cummulative sum")
plt.show()

r = 1200
X_appr = U[:, :r] @ S[:r, :r] @ V_t[:r, :]
plt.figure()
img = plt.imshow(250 - X_appr)
img.set_cmap('gray')
plt.axis('off')
plt.title(f"r = {r}")
plt.show()

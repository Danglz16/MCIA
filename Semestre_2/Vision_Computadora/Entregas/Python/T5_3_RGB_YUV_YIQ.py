import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog

file_path = filedialog.askopenfilename(
    title='File Selector',
    filetypes=[("Images", "*.*;*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0
if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]
elif A.ndim == 2:
    A = np.dstack([A, A, A])

M_YUV = np.array([[0.30, 0.59, 0.11],
                  [-0.15, -0.29, 0.44],
                  [0.62, -0.52, -0.10]])

M_YIQ = np.array([[0.30, 0.59, 0.11],
                  [0.60, -0.27, -0.32],
                  [0.21, -0.52, 0.31]])

h, w, _ = A.shape
A_reshaped = A.reshape(-1, 3).T

YUV = M_YUV @ A_reshaped
YIQ = M_YIQ @ A_reshaped

YUV_img = YUV.T.reshape(h, w, 3)
YIQ_img = YIQ.T.reshape(h, w, 3)

plt.figure(); plt.imshow(A); plt.title('Original RGB'); plt.axis('off')

plt.figure(); plt.imshow(YUV_img[..., 0], cmap='gray'); plt.title('Canal Y (YUV)'); plt.axis('off')
plt.figure(); plt.imshow(YUV_img[..., 1], cmap='gray'); plt.title('Canal U (YUV)'); plt.axis('off')
plt.figure(); plt.imshow(YUV_img[..., 2], cmap='gray'); plt.title('Canal V (YUV)'); plt.axis('off')

plt.figure(); plt.imshow(YIQ_img[..., 0], cmap='gray'); plt.title('Canal Y (YIQ)'); plt.axis('off')
plt.figure(); plt.imshow(YIQ_img[..., 1], cmap='gray'); plt.title('Canal I (YIQ)'); plt.axis('off')
plt.figure(); plt.imshow(YIQ_img[..., 2], cmap='gray'); plt.title('Canal Q (YIQ)'); plt.axis('off')

plt.show()
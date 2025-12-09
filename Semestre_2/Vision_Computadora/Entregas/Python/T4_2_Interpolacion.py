import matplotlib.pyplot as plt
from skimage.io import imread
from tkinter import Tk, filedialog
from skimage.transform import resize

Tk().withdraw()
file_path = filedialog.askopenfilename(
    title='File Selector',
    filetypes=[("Images", "*.*;*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0
if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]

fx, fy = A.shape[0]*10, A.shape[1]*10

R1 = resize(A, (fx, fy), order=0, preserve_range=True, anti_aliasing=False)
R2 = resize(A, (fx, fy), order=1, preserve_range=True, anti_aliasing=False)
R3 = resize(A, (fx, fy), order=3, preserve_range=True, anti_aliasing=False)

plt.figure()
plt.subplot(2,2,1); plt.imshow(A);  plt.title('Imagen Pequeña');      plt.axis('off')
plt.subplot(2,2,2); plt.imshow(R1); plt.title('Zoom Vecino Cercano'); plt.axis('off')
plt.subplot(2,2,3); plt.imshow(R2); plt.title('Zoom Bilineal');       plt.axis('off')
plt.subplot(2,2,4); plt.imshow(R3); plt.title('Zoom Bicubica');       plt.axis('off')
plt.show()

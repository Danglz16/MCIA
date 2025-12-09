import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog
from skimage.morphology import dilation, erosion, opening, closing, skeletonize, thin

file_path = filedialog.askopenfilename(
    title='File Selector - Imagen A',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

A = imread(file_path).astype(float) / 255.0
if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]

if A.ndim == 3:
    Agris = rgb2gray(A)
else:
    Agris = A

ImBW = Agris > 0.5

SE = np.ones((3, 3), dtype=bool)

ImDil1 = dilation(ImBW, SE)
ImDil2 = dilation(ImDil1, SE)
ImDil3 = dilation(ImDil2, SE)

ImEro1 = erosion(ImBW, SE)
ImEro2 = erosion(ImEro1, SE)
ImEro3 = erosion(ImEro2, SE)

plt.figure()
plt.subplot(2,3,1); plt.imshow(ImBW, cmap='gray');   plt.title("Original");       plt.axis('off')
plt.subplot(2,3,2); plt.imshow(ImDil1, cmap='gray'); plt.title("Dilatación 1");   plt.axis('off')
plt.subplot(2,3,3); plt.imshow(ImDil2, cmap='gray'); plt.title("Dilatación 2");   plt.axis('off')
plt.subplot(2,3,4); plt.imshow(ImEro1, cmap='gray'); plt.title("Erosión 1");      plt.axis('off')
plt.subplot(2,3,5); plt.imshow(ImEro2, cmap='gray'); plt.title("Erosión 2");      plt.axis('off')
plt.subplot(2,3,6); plt.imshow(ImEro3, cmap='gray'); plt.title("Erosión 3");      plt.axis('off')

Open = opening(ImBW, SE)
Close = closing(ImBW, SE)

plt.figure()
plt.subplot(1,3,1); plt.imshow(ImBW, cmap='gray');   plt.title("Original");          plt.axis('off')
plt.subplot(1,3,2); plt.imshow(Open, cmap='gray');   plt.title("Apertura (Open)");   plt.axis('off')
plt.subplot(1,3,3); plt.imshow(Close, cmap='gray');  plt.title("Cierre (Close)");    plt.axis('off')

Borde = dilation(ImBW, SE).astype(float) - ImBW.astype(float)

plt.figure()
plt.subplot(1,2,1); plt.imshow(ImBW, cmap='gray');   plt.title("Original");          plt.axis('off')
plt.subplot(1,2,2); plt.imshow(Borde, cmap='gray');  plt.title("Borde Morfológico"); plt.axis('off')

Esqueleto_bwmorph = skeletonize(ImBW)
Esqueleto_bwskel  = thin(ImBW)

plt.figure()
plt.subplot(1,3,1); plt.imshow(ImBW, cmap='gray');             plt.title("Original");                     plt.axis('off')
plt.subplot(1,3,2); plt.imshow(Esqueleto_bwmorph, cmap='gray');plt.title("Esqueleto (bwmorph 'skel')");   plt.axis('off')
plt.subplot(1,3,3); plt.imshow(Esqueleto_bwskel,  cmap='gray');plt.title("Esqueleto (bwskel)");           plt.axis('off')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from tkinter import Tk, filedialog
from skimage.transform import AffineTransform, ProjectiveTransform, warp

Tk().withdraw()
file_path = filedialog.askopenfilename(
    title='File Selector',
    filetypes=[("Images", "*.*;*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

img_color = imread(file_path).astype(float) / 255.0
if img_color.ndim == 3 and img_color.shape[-1] == 4:
    img_color = img_color[..., :3]

if img_color.ndim == 3:
    img_gray = rgb2gray(img_color)
else:
    img_gray = img_color

plt.figure()
plt.imshow(img_gray, cmap='gray')
plt.title('Selecciona 3 puntos')
pts = plt.ginput(3)
plt.close()

xa = np.array([p[0] for p in pts])
ya = np.array([p[1] for p in pts])

xr = np.array([150, 300, 100])
yr = np.array([100, 250, 350])

M = np.array([
    [xa[0], ya[0], 1,     0,     0, 0],
    [    0,     0, 0, xa[0], ya[0], 1],
    [xa[1], ya[1], 1,     0,     0, 0],
    [    0,     0, 0, xa[1], ya[1], 1],
    [xa[2], ya[2], 1,     0,     0, 0],
    [    0,     0, 0, xa[2], ya[2], 1],
], dtype=float)

b = np.array([xr[0], yr[0], xr[1], yr[1], xr[2], yr[2]], dtype=float)
c = np.linalg.solve(M, b)

T = np.array([
    [c[0], c[1], c[2]],
    [c[3], c[4], c[5]],
    [0.0,  0.0,  1.0]
])

tform_affine = AffineTransform(matrix=T)
img_affine = warp(img_color, tform_affine, output_shape=img_color.shape[:2])

h, w = img_color.shape[:2]

pts_original = np.array([
    [ 50,   50],
    [w-50,  50],
    [ 50,  h-50],
    [w-50, h-50]
], dtype=float)

pts_destino = np.array([
    [ 30,   70],
    [w-20,  30],
    [ 70,  h-30],
    [w-40, h-20]
], dtype=float)

tform_persp = ProjectiveTransform()
tform_persp.estimate(pts_original, pts_destino)
img_persp = warp(img_color, tform_persp, output_shape=(h, w))

plt.figure(figsize=(8, 6))
plt.subplot(2,2,1); plt.imshow(img_color);   plt.title('Original');               plt.axis('off')
plt.subplot(2,2,2); plt.imshow(img_affine);  plt.title('Transformación afín');    plt.axis('off')
plt.subplot(2,2,3); plt.imshow(img_color);   plt.title('Original (perspectiva)'); plt.axis('off')
plt.subplot(2,2,4); plt.imshow(img_persp);   plt.title('Transformación perspectiva'); plt.axis('off')
plt.tight_layout()
plt.show()

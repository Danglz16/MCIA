import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from tkinter import Tk, filedialog

Tk().withdraw()
file_path = filedialog.askopenfilename(
    title='File Selector',
    filetypes=[("Images", "*.*;*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)

img_original_uint8 = imread(file_path)

if img_original_uint8.ndim == 3 and img_original_uint8.shape[-1] == 4:
    img_original_uint8 = img_original_uint8[..., :3]

if img_original_uint8.ndim != 3 or img_original_uint8.shape[2] != 3:
    img_rgb_double = np.repeat(img_original_uint8.astype(float) / 255.0, 3, axis=2) if img_original_uint8.ndim == 3 else np.dstack([img_original_uint8.astype(float)/255.0]*3)
else:
    img_rgb_double = img_original_uint8.astype(float) / 255.0

R = img_rgb_double[..., 0]
G = img_rgb_double[..., 1]
B = img_rgb_double[..., 2]

rows, cols, _ = img_rgb_double.shape

MAX = np.maximum(np.maximum(R, G), B)
MIN = np.minimum(np.minimum(R, G), B)
Delta = MAX - MIN
Delta[Delta == 0] = 1e-6

H = np.zeros((rows, cols))
S_hsv = np.zeros((rows, cols))
S_hls = np.zeros((rows, cols))

mask_R_max = (R == MAX)
H[mask_R_max] = ((G[mask_R_max] - B[mask_R_max]) / Delta[mask_R_max]) * 60.0

mask_G_max = (G == MAX)
H[mask_G_max] = (((B[mask_G_max] - R[mask_G_max]) / Delta[mask_G_max]) * 60.0) + 120.0

mask_B_max = (B == MAX)
H[mask_B_max] = (((R[mask_B_max] - G[mask_B_max]) / Delta[mask_B_max]) * 60.0) + 240.0

H[H < 0] += 360.0

V = MAX
mask_MAX_zero = (MAX == 0)
S_hsv[~mask_MAX_zero] = Delta[~mask_MAX_zero] / MAX[~mask_MAX_zero]
S_hsv[mask_MAX_zero] = 0

L = (MAX + MIN) / 2.0
mask_den_zero = (L == 0) | (L == 1)
denominador = 1 - np.abs(2 * L - 1)
denominador[denominador == 0] = 1e-6
S_hls[~mask_den_zero] = Delta[~mask_den_zero] / denominador[~mask_den_zero]
S_hls[mask_den_zero] = 0

H_norm = H / 360.0
S_hsv_norm = S_hsv
V_norm = V
S_hls_norm = S_hls
L_norm = L

def hsv2rgb_np(hsv):
    h = hsv[..., 0]
    s = hsv[..., 1]
    v = hsv[..., 2]

    i = np.floor(h * 6).astype(int)
    f = h * 6 - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)

    i = i % 6
    r = np.zeros_like(h)
    g = np.zeros_like(h)
    b = np.zeros_like(h)

    m0 = (i == 0); r[m0], g[m0], b[m0] = v[m0], t[m0], p[m0]
    m1 = (i == 1); r[m1], g[m1], b[m1] = q[m1], v[m1], p[m1]
    m2 = (i == 2); r[m2], g[m2], b[m2] = p[m2], v[m2], t[m2]
    m3 = (i == 3); r[m3], g[m3], b[m3] = p[m3], q[m3], v[m3]
    m4 = (i == 4); r[m4], g[m4], b[m4] = t[m4], p[m4], v[m4]
    m5 = (i == 5); r[m5], g[m5], b[m5] = v[m5], p[m5], q[m5]

    return np.stack([r, g, b], axis=-1)

hsv_matrix = np.dstack([H_norm, S_hsv_norm, V_norm])
img_hsv_to_rgb = hsv2rgb_np(hsv_matrix)

plt.figure(figsize=(14, 7))

plt.subplot(2,4,1); plt.imshow(img_rgb_double); plt.title("Original RGB"); plt.axis('off')

plt.subplot(2,4,2); plt.imshow(H_norm, cmap='gray'); plt.title("H (Tono) - HSV"); plt.axis('off')
plt.subplot(2,4,3); plt.imshow(S_hsv_norm, cmap='gray'); plt.title("S (Saturación) - HSV"); plt.axis('off')
plt.subplot(2,4,4); plt.imshow(V_norm, cmap='gray'); plt.title("V (Valor/Brillo) - HSV"); plt.axis('off')

plt.subplot(2,4,5); plt.imshow(img_hsv_to_rgb); plt.title("Reconstrucción HSV a RGB"); plt.axis('off')

plt.subplot(2,4,6); plt.imshow(H_norm, cmap='gray'); plt.title("H (Tono) - HLS"); plt.axis('off')
plt.subplot(2,4,7); plt.imshow(S_hls_norm, cmap='gray'); plt.title("S (Saturación) - HLS"); plt.axis('off')
plt.subplot(2,4,8); plt.imshow(L_norm, cmap='gray'); plt.title("L (Luminosidad) - HLS"); plt.axis('off')

plt.tight_layout()
plt.show()

input()
plt.close('all')

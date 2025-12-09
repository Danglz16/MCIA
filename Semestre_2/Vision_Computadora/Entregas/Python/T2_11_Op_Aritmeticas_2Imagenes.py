import matplotlib.pyplot as plt
from skimage.io import imread
from tkinter import Tk, filedialog
from skimage.transform import resize

file_path1 = filedialog.askopenfilename(
    title='File Selector - Imagen A',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)
A = imread(file_path1).astype(float) / 255.0

file_path2 = filedialog.askopenfilename(
    title='File Selector - Imagen B',
    filetypes=[("Images", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
)
B = imread(file_path2).astype(float) / 255.0

if A.ndim == 3 and A.shape[-1] == 4:
    A = A[..., :3]
if B.ndim == 3 and B.shape[-1] == 4:
    B = B[..., :3]

B = resize(B, A.shape, preserve_range=True)

suma = A + B
resta = A - B
multiplicacion = A * B
B_corr = B.copy()
B_corr[B_corr < 1e-5] = 1e-5
division = A / B_corr

plt.figure()
plt.subplot(2,4,2); plt.imshow(A); plt.title('A'); plt.axis('off')
plt.subplot(2,4,3); plt.imshow(B); plt.title('B'); plt.axis('off')
plt.subplot(2,4,5); plt.imshow(suma); plt.title('A+B'); plt.axis('off')
plt.subplot(2,4,6); plt.imshow(resta); plt.title('A-B'); plt.axis('off')
plt.subplot(2,4,7); plt.imshow(multiplicacion); plt.title('A.*B'); plt.axis('off')
plt.subplot(2,4,8); plt.imshow(division); plt.title('A./B'); plt.axis('off')


a = 0.25
suma_media = (A + B) / 2
suma_media_pon = a * A + (1 - a) * B

plt.figure()
plt.subplot(2,2,1); plt.imshow(A); plt.title('A'); plt.axis('off')
plt.subplot(2,2,3); plt.imshow(B); plt.title('B'); plt.axis('off')
plt.subplot(2,2,2); plt.imshow(suma_media); plt.title('(A+B)/2'); plt.axis('off')
plt.subplot(2,2,4); plt.imshow(suma_media_pon); plt.title(f'A+B media ponderada (a={a})'); plt.axis('off')


a_resta = 0.8
resta_media = (A - B) / 2
resta_media_pon = a_resta * A - (1 - a_resta) * B

plt.figure()
plt.subplot(2,2,1); plt.imshow(A); plt.title('A'); plt.axis('off')
plt.subplot(2,2,3); plt.imshow(B); plt.title('B'); plt.axis('off')
plt.subplot(2,2,2); plt.imshow(resta_media); plt.title('(A-B)/2'); plt.axis('off')
plt.subplot(2,2,4); plt.imshow(resta_media_pon); plt.title(f'A-B media ponderada(a={a_resta})'); plt.axis('off')


a_mult = 0.55
multi_media = (A * B) / 2
multi_media_pon = (a_mult * A) * ((1 - a_mult) * B)

plt.figure()
plt.subplot(2,2,1); plt.imshow(A); plt.title('A'); plt.axis('off')
plt.subplot(2,2,3); plt.imshow(B); plt.title('B'); plt.axis('off')
plt.subplot(2,2,2); plt.imshow(multi_media); plt.title('(A*B)/2'); plt.axis('off')
plt.subplot(2,2,4); plt.imshow(multi_media_pon); plt.title(f'A*B media ponderada (a={a_mult})'); plt.axis('off')


a_div = 0.25
B_div = B.copy()
B_div[B_div < 1e-5] = 1e-5
div_media = (A / B_div) / 2
div_media_pon = (a_div * A) / ((1 - a_div) * B_div)

plt.figure()
plt.subplot(2,2,1); plt.imshow(A); plt.title('A'); plt.axis('off')
plt.subplot(2,2,3); plt.imshow(B); plt.title('B'); plt.axis('off')
plt.subplot(2,2,2); plt.imshow(div_media); plt.title('(A/B)/2'); plt.axis('off')
plt.subplot(2,2,4); plt.imshow(div_media_pon); plt.title(f'A/B media ponderada (a={a_div})'); plt.axis('off')
plt.show()

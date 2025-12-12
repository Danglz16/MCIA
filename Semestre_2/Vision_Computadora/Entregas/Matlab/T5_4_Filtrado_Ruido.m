clear;
close all;
clc;

[file,path] = uigetfile({'*.*';'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = strcat(path,file);
A = imread(ruta);
img = im2double(A);

% FFT y espectro
f = fft2(img);
fshift = fftshift(f);
magnitude_spectrum = 20*log(abs(fshift)+1);
phase_spectrum = angle(fshift);

% Reconstrucción directa con IFFT
finv = ifft2(f);
f_back = abs(finv);

% Crear máscara para eliminar bandas de ruido
[rows, cols] = size(img);
mask = ones(rows, cols);
band_width = 10;
center_col = round(cols/2);

% Puedes ajustar la posición y ancho de la banda
mask(:, center_col-50:center_col-50+band_width-1) = 0;
mask(:, center_col+50-band_width+1:center_col+50) = 0;

% Aplicar máscara en el dominio frecuencial
fshift_masked = fshift .* mask;
magnitude_masked = 20*log(abs(fshift_masked)+1);

% IFFT de espectro retocado
f_ishift = ifftshift(fshift_masked);
img_restored = abs(ifft2(f_ishift));

% Visualización resultados
figure();
subplot(2,3,1); imshow(img,[]); title('Imagen de entrada'); axis off;
subplot(2,3,2); imshow(magnitude_spectrum,[]); title('Espectro de magnitud'); axis off;
subplot(2,3,3); imshow(mask,[]); title('Mascara de bandas de ruido'); axis off;
subplot(2,3,4); imshow(magnitude_masked,[]); title('Masked Spectrum'); axis off;
subplot(2,3,5); imshow(img_restored,[]); title('Imagen restaurada'); axis off;
subplot(2,3,6); imshow(phase_spectrum,[]); title('Espectro de fase'); axis off;
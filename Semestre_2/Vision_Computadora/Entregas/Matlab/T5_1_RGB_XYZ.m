clear;
close all;
clc;

[file,path] = uigetfile({'*.*';'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = strcat(path,file);
A = imread(ruta);
A = im2double(A);

% Matriz de RGB a XYZ
M_rgb2xyz = [0.41, 0.36, 0.18;
             0.21, 0.72, 0.07;
             0.02, 0.12, 0.95];
% Matriz XYZ a RGB
M_xyz2rgb = [3.24, -1.5, -0.5;
            -0.9, 1.88, 0.04;
             0.06, -0.2, 1.05];

[m, n, ~] = size(A); % Tamaño de la imagen

% Convertir de RGB a XYZ
rgb = reshape(A, [], 3);           % N x 3
xyz = rgb * M_rgb2xyz';            % N x 3
img_xyz = reshape(xyz, m, n, 3);   % Regresar a forma de imagen

% Convertir de XYZ a RGB
xyz2 = reshape(img_xyz, [], 3);    % N x 3
rgb2 = xyz2 * M_xyz2rgb';          % N x 3
img_rgb2 = reshape(rgb2, m, n, 3); % Regresar a forma de imagen
img_rgb2 = min(max(img_rgb2, 0), 1); % Limitar valores entre 0 y 1

% Mostrar imágenes
figure;
subplot(1,3,1); imshow(A); title('Original RGB');
subplot(1,3,2); imshow(img_xyz); title('Convertida a XYZ');
subplot(1,3,3); imshow(img_rgb2); title('RGB restaurada');

% Calcular Métricas de Calidad de Imagen
disp('Métricas de Calidad de Imagen');

% IMMSE (Error Cuadrático Medio de la Imagen)
mse = immse(A, img_rgb2);
fprintf('IMMSE: %.6f\n', mse);

% PSNR (Relación Señal/Ruido Pico)
peaksnr = psnr(img_rgb2, A);
fprintf('PSNR: %.2f dB\n', peaksnr);

% SSIM (Índice de Similitud Estructural)
[ssimval, ssimmap] = ssim(img_rgb2, A);
fprintf('SSIM: %.4f\n', ssimval);
clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = strcat(path,file);
A=imread(ruta);
A=im2double(A);

% Suavizado Gaussiano 15 x 15
M1515 = ones(15,15);
[mx, my] = size(M1515);
M1515 = M1515/(mx*my);

R1 = zeros(size(A));

if length(size(A)) == 3
    R1(:,:,1) = conv2(A(:, :, 1), M1515, 'same'); % M Cambia segun cuantas comboluciones se quieran agregar
    R1(:,:,2) = conv2(A(:, :, 2), M1515, 'same');
    R1(:,:,3) = conv2(A(:, :, 3), M1515, 'same');
end
figure,
subplot(221); imshow(A); title('Imagen Original A')
subplot(222); imshow(R1); title('A Gauseano 15x15 (Suavizado)')

% Perfilado 
% (Laplaciano + identidad) aplicado a la imagen para el perfilado
Laplacioano = [-1, -1, -1
                -1,  8, -1
                -1, -1, -1];

R2 = zeros(size(A));

if length(size(A)) == 3
    R2(:,:,1) = conv2(A(:, :, 1), Laplacioano, 'same'); % M Cambia segun cuantas comboluciones se quieran agregar
    R2(:,:,2) = conv2(A(:, :, 2), Laplacioano, 'same');
    R2(:,:,3) = conv2(A(:, :, 3), Laplacioano, 'same');
end
subplot(223); imshow(R2); title('A Laplaciano (Perfilado)')
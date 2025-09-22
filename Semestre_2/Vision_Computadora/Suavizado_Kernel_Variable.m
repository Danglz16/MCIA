clear;
close all;
clc;    

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = strcat(path,file);

A=imread(ruta);
A=im2double(A);

% 3 x 3
%M33 = ones(3,3);
%[mx, my] = size(M33);
%M33 = M33/(mx*my);

% 5 x 5
M55 = ones(5,5);
[mx, my] = size(M55);
M55 = M55/(mx*my);

% 11 x 11
M11 = ones(11,11);
[mx, my] = size(M11);
M11 = M11/(mx*my);

% 21 x 21
M21 = ones(21,21);
[mx, my] = size(M21);
M21 = M21/(mx*my);

R1 = zeros(size(A));
R2 = zeros(size(A));
R3 = zeros(size(A));

if length(size(A)) == 3
    R1(:,:,1) = conv2(A(:, :, 1), M55, 'same'); % M Cambia segun cuantas comboluciones se quieran agregar
    R1(:,:,2) = conv2(A(:, :, 2), M55, 'same');
    R1(:,:,3) = conv2(A(:, :, 3), M55, 'same');

    R2(:,:,1) = conv2(A(:, :, 1), M11, 'same'); % M Cambia segun cuantas comboluciones se quieran agregar
    R2(:,:,2) = conv2(A(:, :, 2), M11, 'same');
    R2(:,:,3) = conv2(A(:, :, 3), M11, 'same');

    R3(:,:,1) = conv2(A(:, :, 1), M21, 'same'); % M Cambia segun cuantas comboluciones se quieran agregar
    R3(:,:,2) = conv2(A(:, :, 2), M21, 'same');
    R3(:,:,3) = conv2(A(:, :, 3), M21, 'same');
end
if length(size(A)) == 2
    R = conv2(A, M, 'same');
end

figure,
subplot(221); imshow(A); title('Imagen Original A')
subplot(222); imshow(R1); title('R = A conv M')
subplot(223); imshow(R2); title('R = A conv M')
subplot(224); imshow(R3); title('R = A conv M')
close all;
clc;

[file1,path1] = uigetfile({'*.png';'*.jpg';'*.jpeg';'*.bmp';'*.gif'},'File Selector');

ruta1=strcat(path1,file1);

A=imread(ruta1);
A=im2double(A);

figure,
subplot(121);imshow(A); title('Imagen A');
subplot(122); imhist(A); title('Histograma de A');

% Histograma de imagen en gris
Agris = rgb2gray(A);
figure,
subplot(121);imshow(Agris); title('Imagen gris');
subplot(122); imhist(Agris); title('Histograma de A gris');

% Histograma por canal RGB
A_r=A(:,:,1);
A_g=A(:,:,2);
A_b=A(:,:,3);

figure;
subplot(232);imshow(A); title('Imagen A');
subplot(234);imhist(A_r); title('Histograma canal rojo');
subplot(235);imhist(A_g); title('Histograma canal verde');
subplot(236);imhist(A_b); title('Histograma canal azul');
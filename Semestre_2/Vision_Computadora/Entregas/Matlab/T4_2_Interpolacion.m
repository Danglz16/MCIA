clear;
close all;
clc;

[file,path] = uigetfile({'*.*';'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');

ruta = strcat(path,file);
A=imread(ruta);
A=im2double(A);

figure, 
subplot(221), imshow(A);title('Imagen Pequeña');

R1=imresize(A,10,'nearest');
R2=imresize(A,10,'bilinear');
R3=imresize(A,10,'bicubic');

subplot(222), imshow(R1);title('Zoom Vecino Cercano');
subplot(223), imshow(R2);title('Zoom Bilineal');
subplot(224), imshow(R3);title('Zoom Bicubica');
clear;
close all;
clc;

[file,path] = uigetfile({'*.png';'*.jpg';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = strcat(path,file);
A=imread(ruta);
A=im2double(A);

if length(size(A)) == 3
    A= rgb2gray(A);
end 

A = imbinarize(A);
SE = ones(5);

R1 = imdilate(A,SE);
R2 = imerode(A,SE);

figure,
subplot(131), imshow(A), title("Imagen Original")
subplot(132), imshow(R1), title("R1 = Dilatacion de 3x3 de A")
subplot(133), imshow(R2), title("R2 = Erosion de 3x3 de A")

Borde = R1-A;

figure,
subplot(131), imshow(A), title("Imagen Original")
subplot(132), imshow(Borde), title("Borde Morfologico")

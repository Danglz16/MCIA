clear;
close all;
clc;

[file,path] = uigetfile({'*.png';'*.jpg';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');

ruta = strcat(path,file);

tic

A=imread(ruta);
A=im2double(A);

figure;
subplot(521);imshow(A);title('Imagen Original A (x,y)')
subplot(522);imhist(A);title('Histograma de A')

% Suma de una constante A (Aclarar)
a = 0.25;

for a = 0.0:0.1:1.0
    R1 = zeros(size(A));
    R1 = a+A;
    subplot(523);imshow(R1);title('Imagen Resultante de A+a (x,y)')
    subplot(524);imhist(R1);title(a)
    pause(1);

    R2 = zeros(size(A));
    R2 = a-A;
    subplot(525);imshow(R2);title('Imagen Resultante de A-a (x,y)')
    subplot(526);imhist(R2);title(a)
    pause(1);

    R3 = zeros(size(A));
    R3 = a*A;
    subplot(527);imshow(R3);title('Imagen Resultante de A*a (x,y)')
    subplot(528);imhist(R3);title(a)
    pause(1);

    R4 = zeros(size(A));
    R4 = A/a;
    subplot(529);imshow(R4);title('Imagen Resultante de A/a (x,y)')
    subplot(5,2,10);imhist(R4);title(a)
    pause(1);

end

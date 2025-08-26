clear;
close all;
clc;

[file,path] = uigetfile({'*.png';'*.jpg';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');

ruta = strcat(path,file);

tic

A=imread(ruta);
A=im2double(A);

figure;
subplot(321);imshow(A);title('Imagen Original A (x,y)')
subplot(322);imhist(A);title('Histograma de A')

% Suma de una constante A (Aclarar)
a = 0.2;

for a = 0.0:0.1:1.0
    R1 = zeros(size(A));
    R1 = a+A;
    
    subplot(323);imshow(R1);title('Imagen Resultante de A+a (x,y)')
    subplot(324);imhist(R1);title(a)
    pause(1);

    R2 = zeros(size(A));
    R2 = a-A;
    
    subplot(325);imshow(R2);title('Imagen Resultante de A-a (x,y)')
    subplot(326);imhist(R2);title(a)
    pause(1);
end

clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');

ruta = strcat(path,file);

tic

A=imread(ruta);
A=im2double(A);
%  f(v):= (v-m)*255/(M-m)

m = 0.05;% Val minimo del histograma
M = 0.9;% Val Max del histograma

R = zeros(size(A));
R = ((A-m) * 1.0/(M-m));

figure;
subplot(221);imshow(A);title('Imagen Original');
subplot(222);imhist(A);title('Histograma de A');
subplot(223);imshow(R);title('Ajuste Lineal');
subplot(224);imhist(R);title('Histograma de R');
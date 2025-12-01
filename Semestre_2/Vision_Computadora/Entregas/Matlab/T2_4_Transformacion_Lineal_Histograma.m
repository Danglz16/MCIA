clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = fullfile(path, file);

A = imread(ruta);
A = im2double(A);

% --- Parámetros del ajuste lineal ---
m = 0.05;     % valor mínimo del histograma al que mapea 0
M = 0.90;     % valor máximo del histograma al que mapea 1

R = (A - m) / (M - m);

R = max(0, min(1, R));


figure;
subplot(2,2,1);imshow(A);title('Imagen Original');
subplot(2,2,2);
if size(A,3)==1
    imhist(A);
else
    imhist(rgb2gray(A));
end
title('Histograma de A');

subplot(2,2,3);imshow(R);title('Ajuste Lineal');
subplot(2,2,4);
if size(R,3)==1
    imhist(R);
else
    imhist(rgb2gray(R));
end
title('Histograma de R');

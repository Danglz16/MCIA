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
gamma = 2;
R = 1.0*(A/1.0).^(1/gamma);

figure;
subplot(221);imshow(A);title('Imagen Original');
subplot(222);imhist(A);title('Histograma de A');
%subplot(223);imshow(R);title('Ajuste de Gamma');
%subplot(224);imhist(R);title(gamma);

for gamma = 0.1:0.1:4
    R=1.0*(A/1.0).^(1/gamma);
    subplot(223);imshow(R);title('Ajuste de Gamma');
    subplot(224);imhist(R);title(gamma);
    pause(0.05);
end
clear all;
close all;
clc;

[file,path] = uigetfile({'*.png';'*.jpg';'*.jpeg';...
                            '*.bmp';'*.gif'},...
                            'File Selector');
ruta=strcat(path,file);

A=imread(ruta);
A=im2double(A);

R1=zeros(size(A));
R2=zeros(size(A));

R1 = histeq(A);

R2(:,:,1) = adapthisteq(A(:,:,1));
R2(:,:,2) = adapthisteq(A(:,:,2));
R2(:,:,3) = adapthisteq(A(:,:,3));


figure,
subplot(321);imshow(A);title('Imagen Original');
subplot(322);imhist(A);title('Histograma de A');
subplot(323);imshow(R1);title('Ecualizacion de histograma');
subplot(324);imhist(R1);title('Histograma de R1');

subplot(325);imshow(R2);title('Ecualizacion CLAHE');
subplot(326);imhist(R2);title('Histograma de R2');

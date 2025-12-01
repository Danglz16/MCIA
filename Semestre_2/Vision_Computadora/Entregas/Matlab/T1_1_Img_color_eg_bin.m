clear;
close all;
clc;

[file,path] = uigetfile({'*.png';'*.jpg';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');

A = imread(fullfile(path,file));
G = rgb2gray(A);
B = imbinarize(G);

figure;
subplot(131);imshow(A);title('Original');
subplot(132);imshow(G);title('Escala de Grises');
subplot(133);imshow(B);title('Binario');
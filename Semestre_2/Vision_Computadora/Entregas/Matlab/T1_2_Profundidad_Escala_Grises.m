clear;
close all;
clc;

[file,path] = uigetfile({'*.png';'*.jpg';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');

O = imread(fullfile(path,file));
A = rgb2gray(O);
A = im2double(A);

L2 = 2^2;
IQ2 = round(A*(L2-1))/(L2-1);

L3 = 2^3;
IQ3 = round(A*(L3-1))/(L3-1);

L4 = 2^4;
IQ4 = round(A*(L4-1))/(L4-1);

L5 = 2^5;
IQ5 = round(A*(L5-1))/(L5-1);

figure;
subplot(321); imshow(O); title('Original');
subplot(322); imshow(A); title('Escala de Grises');
subplot(323); imshow(IQ2); title('2 bits (4 niveles)');
subplot(324); imshow(IQ3); title('3 bits (8 niveles)');
subplot(325); imshow(IQ4); title('4 bits (16 niveles)');
subplot(326); imshow(IQ5); title('5 bits (32 niveles)');

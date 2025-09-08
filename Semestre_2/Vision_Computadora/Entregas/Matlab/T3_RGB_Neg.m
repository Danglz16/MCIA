clear;
close all;
clc;

[file,path] = uigetfile({'*.png';'*.jpg';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');

O = imread(fullfile(path,file));
[R,G,B] = imsplit(O);

allBlack = zeros(size(O,1,2),class(O));
justR = cat(3,R,allBlack,allBlack);
justG = cat(3,allBlack,G,allBlack);
justB = cat(3,allBlack,allBlack,B);

full = cat(3,R,G,B);
Neg = 255 - full;

figure
subplot(2,3,1); imshow(justR); title('Canal Rojo');
subplot(2,3,2); imshow(justG); title('Canal Verde');
subplot(2,3,3); imshow(justB); title('Canal Azul');
subplot(2,3,4); imshow(full); title('Imagen Completa');
subplot(2,3,5); imshow(Neg); title('Imagen Negativa');
clear all;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';...
                            '*.bmp';'*.gif'},...
                            'File Selector');
ruta=strcat(path,file);

A=imread(ruta);
A=im2double(A);
A= rgb2gray(A);
A= imbinarize(A);

[file2,path2] = uigetfile({'*.jpg';'*.png';'*.jpeg';...
                            '*.bmp';'*.gif'},...
                            'File Selector');
ruta2=strcat(path2,file2);

B=imread(ruta2);
B=im2double(B);
B= rgb2gray(B);
B= imbinarize(B);

[bx, by]=size(B);
A=imresize(A,[bx by]);

C = A&B;

figure,
subplot(131); imshow(A); title('Imagen A');
subplot(132); imshow(B); title('Imagen B');
subplot(133); imshow(C); title('Imagen C');

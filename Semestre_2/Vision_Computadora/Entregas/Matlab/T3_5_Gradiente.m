clear;
close all;
clc;

sobelX=[-1,0,1
       -2,0,2
       -1,0,1];

sobelY=[-1,-2,-1
         0, 0, 0
         1, 2, 1];

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = strcat(path,file);
A=imread(ruta);
A=im2double(A);

if length(size(A)) == 3
    A=rgb2gray(A);
end

Dx = conv2(A, sobelX, 'same');
Dy = conv2(A, sobelY, 'same');

Magnitud = sqrt(Dx.^2 + Dy.^2);
Angulo = atan2(Dy, Dx);

figure, imshow(A);title('Imagen Original A'); colormap gray
figure
subplot(221);imshow(Dx);title('Derivada de X en A'); colormap gray
subplot(222);imshow(Dy);title('Derivada de Y en A'); colormap gray
subplot(223);imshow(Magnitud);title('Magnitud = sqrt(Dx^2 + Dy^2)'); colormap gray
subplot(224);imshow(Angulo);title('Angulo = atan2(Dy,Dx)'); colormap gray

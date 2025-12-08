clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen A'); 
ruta=strcat(path,file);
A=imread(ruta);
A= im2double(A);

% Matrices para almacenar nuevas imagenes
[ax ay az] = size(A);
gris_prom = zeros(ax, ay);
gris_pres = zeros(ax, ay);
gris_matlab = rgb2gray(A);

% Canales RGB
A_R = A(:,:,1);
A_G = A(:,:,2);
A_B = A(:,:,3);

% Transformación a escala de grises media y precisa
for m=1:ax
    for n=1:ay
        gris_prom(m,n)=(A_R(m,n) + A_G(m,n) + A_B(m,n))/3.0;
        gris_pres(m,n)=0.21*A_R(m,n) + 0.72*A_G(m,n) + 0.07*A_B(m,n);
    end
end

figure,
subplot(221);imshow(A);title('Imagen original');
subplot(222);imshow(gris_prom);title('Gris promedio');
subplot(223);imshow(gris_pres);title('Gris precisa');
subplot(224);imshow(gris_matlab);title('Gris Matlab');

clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen A'); 
ruta=strcat(path,file);
A=imread(ruta);
A= im2double(A);
Agris = rgb2gray(A);

% Matrices para imagenes
[ax ay] = size(Agris);
sepia = zeros(ax, ay, 3);
verde = zeros(ax, ay, 3);
cian = zeros(ax, ay, 3);

% Colores objetivo
vr_sepia = 255/255.0;
vg_sepia = 150/255.0;
vb_sepia = 0/255.0;

% Verde
vr_verde=30/255.0;
vg_verde=255/255.0;
vb_verde=0/255.0;

% Cian
vr_cian=0/255.0;
vg_cian=255/255.0;
vb_cian=255/255.0;

for m=1:ax
    for n=1:ay
        if A(m,n)<0.5
            sepia(m,n,1) =(vr_sepia*Agris(m,n))/0.5;
            sepia(m,n,2) =(vg_sepia*Agris(m,n))/0.5;
            sepia(m,n,3) =(vb_sepia*Agris(m,n))/0.5;
        else
            sepia(m,n,1) = vr_sepia + ((1.0-vr_sepia)*(Agris(m,n)-0.5))/0.5;
            sepia(m,n,2) = vg_sepia + ((1.0-vg_sepia)*(Agris(m,n)-0.5))/0.5;
            sepia(m,n,3) = vb_sepia + ((1.0-vb_sepia)*(Agris(m,n)-0.5))/0.5;
        end
    end
end

% verde
for m=1:ax
    for n=1:ay
        if A(m,n)<0.5
            verde(m,n,1) =(vr_verde*Agris(m,n))/0.5;
            verde(m,n,2) =(vg_verde*Agris(m,n))/0.5;
            verde(m,n,3) =(vb_verde*Agris(m,n))/0.5;
        else
            verde(m,n,1) = vr_verde + ((1.0-vr_verde)*(Agris(m,n)-0.5))/0.5;
            verde(m,n,2) = vg_verde + ((1.0-vg_verde)*(Agris(m,n)-0.5))/0.5;
            verde(m,n,3) = vb_verde + ((1.0-vb_verde)*(Agris(m,n)-0.5))/0.5;
        end
    end
end

% Cian
for m=1:ax
    for n=1:ay
        if A(m,n)<0.5
            cian(m,n,1) =(vr_cian*Agris(m,n))/0.5;
            cian(m,n,2) =(vg_cian*Agris(m,n))/0.5;
            cian(m,n,3) =(vb_cian*Agris(m,n))/0.5;
        else
            cian(m,n,1) = vr_cian + ((1.0-vr_cian)*(Agris(m,n)-0.5))/0.5;
            cian(m,n,2) = vg_cian + ((1.0-vg_cian)*(Agris(m,n)-0.5))/0.5;
            cian(m,n,3) = vb_cian + ((1.0-vb_cian)*(Agris(m,n)-0.5))/0.5;
        end
    end
end

figure;
subplot(231);imshow(A);title('Imagen Original');
subplot(232);imshow(Agris);title('Escala de grises');
subplot(233);imshow(sepia);title('Escala de sepias');
subplot(235);imshow(verde);title('Escala de (30,255,0)');
subplot(236);imshow(cian);title('Escala de (0,255,255)');
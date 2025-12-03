clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen A'); 
ruta=strcat(path,file);
A=imread(ruta);
A= im2double(A);
Agris = rgb2gray(A);

% Matrices para las imagenes
[ax ay] = size(Agris);
R1 = zeros(ax, ay, 3);
R2 = zeros(ax, ay, 3);
R3 = zeros(ax, ay, 3);
R4 = zeros(ax, ay, 3);

% azul
vr_1 = -20/255.0;
vg_1 =  8/255.0;
vb_1 = 60/255.0;

% rojo
vr_2=1.4;
vg_2=0.9;
vb_2=0.9;

% naranja
vr_3=1.4;
vg_3=1.15;
vb_3=1.0;

% verde
vr_4= -10/255.0;
vg_4= 40/255.0;
vb_4= -10/255.0;

for m=1:ax
    for n=1:ay
        % Suma azul
        R1(m,n,1) = (vr_1+A(m,n,1));
        R1(m,n,2) = (vg_1+A(m,n,2));
        R1(m,n,3) = (vb_1+A(m,n,3));

        % Multiplicacion rojo
        R2(m,n,1) = (vr_2*A(m,n,1));
        R2(m,n,2) = (vg_2*A(m,n,2));
        R2(m,n,3) = (vb_2*A(m,n,3));
        
        % Multiplicacion naranja
        R3(m,n,1) = (vr_3*A(m,n,1));
        R3(m,n,2) = (vg_3*A(m,n,2));
        R3(m,n,3) = (vb_3*A(m,n,3));
        
        % Suma verde
        R4(m,n,1) = (vr_4+A(m,n,1));
        R4(m,n,2) = (vg_4+A(m,n,2));
        R4(m,n,3) = (vb_4+A(m,n,3));
    end
end

figure;
subplot(231);imshow(A);title('Imagen Original');
subplot(232);imshow(R1);title('Suma(-20,8,60)');
subplot(233);imshow(R2);title('Multi(1.4,0.9,0.9)');
subplot(235);imshow(R3);title('Multi(1.4,1.15,1)');
subplot(236);imshow(R4);title('Suma(-10,40,-10)');
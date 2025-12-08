clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen A'); 
ruta=strcat(path,file);
A=imread(ruta);
A= im2double(A);

% Convertir si es RGB
if size(A, 3) == 3
    A = rgb2gray(A);
end

% PREWITT
PrewittX = [-1 0 1; -1 0 1; -1 0 1];
PrewittY = PrewittX';
Dx_prewitt = conv2(A, PrewittX, 'same');
Dy_prewitt = conv2(A, PrewittY, 'same');
Mag_prewitt = sqrt(Dx_prewitt.^2 + Dy_prewitt.^2);

% SCHARR
ScharrX = [-3 0 3; -10 0 10; -3 0 3];
ScharrY = ScharrX';
Dx_scharr = conv2(A, ScharrX, 'same');
Dy_scharr = conv2(A, ScharrY, 'same');
Mag_scharr = sqrt(Dx_scharr.^2 + Dy_scharr.^2);

% SOBEL
SobelX = [-1 0 1; -2 0 2; -1 0 1];
SobelY = SobelX';
Dx_sobel = conv2(A, SobelX, 'same');
Dy_sobel = conv2(A, SobelY, 'same');
Mag_sobel = sqrt(Dx_sobel.^2 + Dy_sobel.^2);

figure('Name','Operadores de borde');
tiledlayout(3,3,'Padding','compact','TileSpacing','compact');

nexttile, imshow(A), title('Imagen original');

nexttile, imshow(Dx_sobel,[]), title('Sobel Dx');
nexttile, imshow(Dy_sobel,[]), title('Sobel Dy');

nexttile, imshow(Dx_prewitt,[]), title('Prewitt Dx');
nexttile, imshow(Dy_prewitt,[]), title('Prewitt Dy');

nexttile, imshow(Dx_scharr,[]), title('Scharr Dx');
nexttile, imshow(Dy_scharr,[]), title('Scharr Dy');

nexttile, imshow(Mag_sobel,[]), title('Magnitud Sobel');
nexttile, imshow(Mag_prewitt,[]), title('Magnitud Prewitt');
nexttile, imshow(Mag_scharr,[]), title('Magnitud Scharr');

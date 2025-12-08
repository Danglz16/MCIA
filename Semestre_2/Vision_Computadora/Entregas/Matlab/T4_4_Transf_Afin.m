clear;
close all;
clc;

[file,path] = uigetfile({'*.*';'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = strcat(path,file);

img_color = imread(ruta);
img_gray  = im2double(img_color);
if size(img_gray,3) == 3
    img_gray = rgb2gray(img_gray);
end

% Transformación afín genérica
figure, imshow(img_gray); title('Selecciona 3 puntos');
[xa, ya] = ginput(3);
close;

xr = [150; 300; 100];
yr = [100; 250; 350];

M = [
    xa(1), ya(1), 1,     0,     0, 0;
       0,     0, 0,  xa(1), ya(1), 1;
    xa(2), ya(2), 1,     0,     0, 0;
       0,     0, 0,  xa(2), ya(2), 1;
    xa(3), ya(3), 1,     0,     0, 0;
       0,     0, 0,  xa(3), ya(3), 1;
];
b = [xr(1); yr(1); xr(2); yr(2); xr(3); yr(3)];
c = M \ b;

T = [c(1), c(2), c(3);
     c(4), c(5), c(6)];

tform_affine = affine2d(T');
img_affine   = imwarp(img_color, tform_affine);

% Transformación perspectiva
[h, w, ~] = size(img_color);

pts_original = [  50   50;
                 w-50  50;
                  50  h-50;
                 w-50 h-50];

pts_destino  = [  30   70;
                 w-20  30;
                  70  h-30;
                 w-40 h-20];

tform_persp = fitgeotrans(pts_original, pts_destino, 'projective');
ref_out     = imref2d(size(img_color));
img_persp   = imwarp(img_color, tform_persp, 'OutputView', ref_out);

% --- Mostrar resultados ---
figure('Name','Transformaciones');
tiledlayout(2,2,'Padding','compact','TileSpacing','compact');

nexttile, imshow(img_color),    title('Original');
nexttile, imshow(img_affine),   title('Transformación afín');
nexttile, imshow(img_color),    title('Original (perspectiva)');
nexttile, imshow(img_persp),    title('Transformación perspectiva');

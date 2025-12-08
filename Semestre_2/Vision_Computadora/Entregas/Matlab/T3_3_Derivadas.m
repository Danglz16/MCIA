clear;
close all;
clc;

[file,path] = uigetfile({'*.*';'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = strcat(path,file);

A = imread(ruta);
if size(A,3) == 3
    A = rgb2gray(A);
end
A = im2double(A);

% Máscaras
Mx      = [-1 1];
My      = Mx';
Mdiag1  = [-2 -1  0; -1 0 1; 0 1 2];   % diagonal ↘︎
Mdiag2  = [0  1  2; -1 0 1; -2 -1 0];  % diagonal ↙︎
Msmooth = [1 2 1; 2 4 2; 1 2 1] / 16;
Memboss = [-2 -1 0; -1 1 1; 0 1 2];

% Derivadas y operaciones
Rx        = conv2(A, Mx, 'same');
Ry        = conv2(A, My, 'same');
Rdiag1    = conv2(A, Mdiag1, 'same');
Rdiag2    = conv2(A, Mdiag2, 'same');
Remboss   = conv2(A, Memboss, 'same');
A_smooth  = conv2(A, Msmooth, 'same');
Rx_smooth = conv2(A_smooth, Mx, 'same');

% Visualización
figure, imshow(A),          title('Original');
figure, imshow(Rx, []),     title('Derivada en X');
figure, imshow(Ry, []),     title('Derivada en Y');
figure, imshow(Rdiag1, []), title('Derivada diagonal 1');
figure, imshow(Rdiag2, []), title('Derivada diagonal 2');
figure, imshow(mat2gray(Remboss)), title('Emboss');
figure, imshow(Rx_smooth, []), title('Suavizado + Derivada X');

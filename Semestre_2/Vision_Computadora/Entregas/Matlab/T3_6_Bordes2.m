clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen A'); 
ruta = strcat(path,file);
A = imread(ruta);
A = im2double(A);

if size(A,3) == 3
    A = rgb2gray(A);
end

% Bordes
Bordes_sobel = edge(A,'Sobel');
Bordes_canny = edge(A,'Canny');

% Laplaciano
Lap = conv2(A, [0 -1 0; -1 4 -1; 0 -1 0], 'same');

% Perfilado (sharpen)
Perfilado = A - Lap;

% Media geométrica (ventana 3x3)
G = exp(conv2(log(A + eps), ones(3)/9, 'same'));

% Filtro máximo y mínimo (ventana 3x3)
Maximo = ordfilt2(A, 9, true(3));
Minimo = ordfilt2(A, 1, true(3));

figure('Name','Filtros espaciales');
tiledlayout(3,3,'Padding','compact','TileSpacing','compact');

nexttile, imshow(A),             title('Original');
nexttile, imshow(Bordes_sobel),  title('Bordes Sobel');
nexttile, imshow(Bordes_canny),  title('Bordes Canny');
nexttile, imshow(Lap,[]),        title('Laplaciano');
nexttile, imshow(Perfilado,[]),  title('Perfilado');
nexttile, imshow(G,[]),          title('Media geométrica');
nexttile, imshow(Maximo,[]),     title('Filtro máximo');
nexttile, imshow(Minimo,[]),     title('Filtro mínimo');

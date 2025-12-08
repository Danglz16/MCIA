clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen A'); 
ruta=strcat(path,file);
A=imread(ruta);
A= im2double(A);
if length(size(A))==3 % Si la imagen es RGB
    Agris=rgb2gray(A);
else
    Agris = A; 
end

% Matriz para la imagen
[ax ay] = size(Agris);
R = zeros(ax, ay, 3);
figure;

num_colors = 256;  % Colores

% Definir paleta de colores de MATLAB ('jet', 'hot', 'parula')
palette_name = 'jet';                         
palette = colormap(palette_name);             
palette = imresize(palette, [num_colors, 3]);

% Normalizar Agris al rango [1, num_colors]
Agris_normalized = round(Agris * (num_colors - 1)) + 1;

% Mapear nivel de gris a un color
for m = 1:size(Agris, 1)
    for n = 1:size(Agris, 2)
        color = Agris_normalized(m, n);
        R(m, n, :) = palette(color, :);
    end
end

% Visualización
subplot(121); imshow(A); title('Imagen original'); 
subplot(122); imshow(R); title(['Paleta: ', palette_name]); colorbar;
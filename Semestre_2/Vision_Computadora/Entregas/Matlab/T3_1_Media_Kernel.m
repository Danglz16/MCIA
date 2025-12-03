clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen A'); 
ruta=strcat(path,file);
A=imread(ruta);
A= im2double(A);

[ax, ay, az] = size(A);

% Kernels 2D para filtros de media
k33 = ones(3,3)/(3*3);
k55 = ones(5,5)/(5*5);
k77 = ones(7,7)/(7*7);

% Kernels 1D para filtros de media horizontal y vertical
kernel_horizontal = ones(1,10)/10;  % Media horizontal (fila)
kernel_vertical = ones(10,1)/10;    % Media vertical (columna)

% Aplicar filtros 2D
R33 = zeros(size(A));
R55 = zeros(size(A));
R77 = zeros(size(A));

for i = 1:az
    R33(:,:,i) = conv2(A(:,:,i), k33, 'same');
    R55(:,:,i) = conv2(A(:,:,i), k55, 'same');
    R77(:,:,i) = conv2(A(:,:,i), k77, 'same');
end

% Aplicar filtros 1D
R_horizontal = zeros(size(A));
R_vertical = zeros(size(A));

for i = 1:az
    R_horizontal(:,:,i) = conv2(A(:,:,i), kernel_horizontal, 'same');
    R_vertical(:,:,i) = conv2(A(:,:,i), kernel_vertical, 'same');
end

% Mostrar resultados
figure(1);
subplot(221); imshow(A); title('Imagen Original');
subplot(222); imshow(R33); title('Media 3x3');
subplot(223); imshow(R55); title('Media 5x5');
subplot(224); imshow(R77); title('Media 7x7');

figure(2);
subplot(131); imshow(A); title('Imagen Original');
subplot(132); imshow(R_horizontal); title('Media Horizontal 1x10');
subplot(133); imshow(R_vertical); title('Media Vertical 10x1');
clear;
close all;
clc;    

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = strcat(path,file);
A=imread(ruta);
A=im2double(A);

%M = [-1 , 1]; % Sirve para ver bordes

M = ones(1,10);
[mx, my] = size(M);
M = M/(mx*my);

R = zeros(size(A));

if length(size(A)) == 3
    R(:,:,1) = conv2(A(:, :, 1), M, 'same'); 
    R(:,:,2) = conv2(A(:, :, 2), M, 'same');
    R(:,:,3) = conv2(A(:, :, 3), M, 'same');
end
if length(size(A)) == 2
    R = conv2(A, M, 'same');
end

figure,
subplot(121); imshow(A); title('Imagen Original A')
subplot(122); imshow(R); title('R = A conv M')
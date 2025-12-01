close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = fullfile(path, file);

I = imread(ruta);
I = im2double(I);

% Pasar a gris sólo si es RGB
if length(size(I)) == 3
    A = rgb2gray(I);
else
    A = I;
end

[ax, ay] = size(A);

% Umbrales
u1 = 42/255;
u2 = 180/255;

R1 = zeros(size(A));
R2 = zeros(size(A));

for m = 1:ax
    for n = 1:ay
        if A(m,n) > u1
            R1(m,n) = 1;
        else
            R1(m,n) = 0;
        end

        if A(m,n) > u2
            R2(m,n) = 1;
        else
            R2(m,n) = 0;
        end
    end
end

% Cortar rango (192,255)
low = 192/255;
high = 255/255;

mask = (A >= low) & (A <= high);   % máscara en gris

C = I;
if length(size(I)) == 3
    % aplicar máscara a los 3 canales
    C(repmat(~mask,[1 1 3])) = 0;   % fondo negro
else
    C(~mask) = 0;
end

figure;

subplot(2,2,1);
imshow(I);
title('Imagen de entrada');

subplot(2,2,2);
imshow(R1);
title('Umbralizar, u = 42');

subplot(2,2,3);
imshow(R2);
title('Umbralizar, u = 180');

subplot(2,2,4);
imshow(C);
title('Cortar rango (192, 255)');

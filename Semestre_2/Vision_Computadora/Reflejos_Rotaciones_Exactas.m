clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');

ruta = strcat(path,file);
A=imread(ruta);
A=im2double(A);

R1 = zeros(size(A));
[ax, ay, az] = size(A);

% Reflejo Horizontal
for m=1:ax
    for n=1:ay
        for p=1:az
            R1(m,n,p) = A(m,ay-n+1,p);
        end
    end
end

% Reflejo Vertical
R2 = zeros(size(A));
for m=1:ax
    for n=1:ay
        for p=1:az
            R2(m,n,p) = A(ax-m+1,n,p);
        end
    end
end

% Rotacion 90 grados
R3 = zeros(ay, ax, az);
for m = 1:ay
    for n = 1:ax
        for p = 1:az
            R3(m, n, p) = A(ax - n + 1, m, p);
        end
    end
end

% Rotacion 180 grados
R4 = zeros(size(A));
for m=1:ax
    for n=1:ay
        for p=1:az
            R4(m,n,p) = A(ax-m+1,ay-n+1,p);
        end
    end
end

% Rotacion 270 grados
R5 = zeros(ay, ax, az);
for m= 1:ay
    for n = 1:ax
        for p = 1:az
            R5(m, n, p) = A(n, ay - m + 1, p);
        end
    end
end


figure,
subplot(231); imshow(A); title('Imagen Original A')
subplot(232); imshow(R1); title('Espejo Horizontal')
subplot(234); imshow(R2); title('Espejo Vertical')
subplot(233); imshow(R3); title('Rotacion 90 Grados')
subplot(235); imshow(R4); title('Rotacion 180 Grados')
subplot(236); imshow(R5); title('Rotacion 270 Grados')
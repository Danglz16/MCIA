close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector');
ruta = fullfile(path,file);

A = imread(ruta);
A = im2double(A);
A_color = A; 
A = rgb2gray(A);
A_Gris = A;
A = imbinarize(A);

[file2,path2] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector');
ruta2 = fullfile(path2,file2);

B = imread(ruta2);
B = im2double(B);
B_color = B;
B = rgb2gray(B);
B_Gris = B;
B = imbinarize(B);

%% --- COLOR ---
[bx, by, ~] = size(B_color);

% Asegurar que ambas sean RGB (3 canales)
if size(A_color,3) == 1
    A_color = cat(3, A_color, A_color, A_color);
end
if size(B_color,3) == 1
    B_color = cat(3, B_color, B_color, B_color);
end

A_color = imresize(A_color, [bx by]);

mask = (A_color > 0) & (B_color > 0);

C_color = A_color;
C_color(~mask) = 0;

figure,
subplot(1,3,1); imshow(A_color); title('Imagen A (color)');
subplot(1,3,2); imshow(B_color); title('Imagen B (color)');
subplot(1,3,3); imshow(C_color); title('A & B (color)');


%% --- GRIS ---
[bx,by] = size(B_Gris);
A_Gris = imresize(A_Gris,[bx by]);
C_Gris = A_Gris & B_Gris;

figure;
subplot(1,3,1); imshow(A_Gris); title('Imagen A (gris)');
subplot(1,3,2); imshow(B_Gris); title('Imagen B (gris)');
subplot(1,3,3); imshow(C_Gris); title('A & B (gris)');

%% --- BOOLEANO ---
[bx,by] = size(B);
A = imresize(A,[bx by]);
C = A & B;

figure;
subplot(1,3,1); imshow(A); title('Imagen A (binaria)');
subplot(1,3,2); imshow(B); title('Imagen B (binaria)');
subplot(1,3,3); imshow(C); title('A & B (binaria)');

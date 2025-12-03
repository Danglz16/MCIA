clear;
close all;
clc;

% Cartel
[file1, path1] = uigetfile({'*.png';'*.jpeg';'*.jpg'}, 'File Selector');
ruta1 = strcat(path1,file1);
M = im2double(imread(ruta1));

% Persona
[file2, path2] = uigetfile({'*.png';'*.jpeg';'*.jpg'}, 'File Selector');
ruta2 = strcat(path2,file2);
A = im2double(imread(ruta2));
A = histeq(A);              %Aplicacion de ecualizado
A =1.0*(A/1.0).^(1/1.8);    %Aplicacion de gama=1.8

% Fondo
[file3,path3] = uigetfile({'*.png';'*.jpeg';'*.jpg'}, 'File Selector');
ruta3=strcat(path3,file3);
F = im2double(imread(ruta3));

[fx fy fz] = size(F);
M=imresize(M,[fx fy]);
A=imresize(A,[fx fy]);

% Calcular la diferenca D = abs(M-A)
D = abs(M - A);

% Umbralizar U=D(D,x)
if length(size(D))==3 % Si es RGB
    Dgris=rgb2gray(D);
else
    Dgris = D;
end
umbral=0.225;
U = Dgris >= umbral; 

% Calcular R = (F AND NOT U) OR (A AND U)
NOT_U = 1 - U;
parte1 = F.*NOT_U;
parte2 = A.*U;
R = parte1 + parte2;

%4. Visualización del fotomontaje
figure;
subplot(3,2,1);imshow(M);title('M');
subplot(3,2,2);imshow(A);title('A');
subplot(3,2,3);imshow(Dgris);title('D');
subplot(3,2,4);imshow(U);title('U');
subplot(3,2,5);imshow(F);title('F');
subplot(3,2,6);imshow(R);title('R');
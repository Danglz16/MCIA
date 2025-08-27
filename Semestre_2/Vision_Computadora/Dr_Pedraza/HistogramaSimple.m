clear all;
close all;
clc;

[file,path] = uigetfile({'*.png';'*.jpg';'*.jpeg';...
                            '*.bmp';'*.gif'},...
                            'File Selector');
ruta=strcat(path,file);

tic
A=imread(ruta);
A=im2double(A);
figure;
subplot(221);imshow(A);title('Imagen Original A(x,y)');
subplot(222);imhist(A);title('Histograma de A');

% Suma de uma constante a
%a=0.2;

for a=0.0:0.1:1.0;
    R1=zeros(size(A));
    R1=A+a;
    subplot(223);imshow(R1);title('Imagen Resultante R1(x,y)=A(x,y)+a');
    subplot(224);imhist(R1);title(a);
    pause(1);
end


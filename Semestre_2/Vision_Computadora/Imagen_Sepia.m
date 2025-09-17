clear all;
close all;
clc

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = strcat(path,file);


A=imread(ruta);
A=im2double(A);

R=zeros(size(A));

% matrizSepia = [ 0.393, 0.769, 0.189;
%                    0.349, 0.686, 0.168;
%                    0.272, 0.534, 0.131 ];

R(:,:,1)=0.393*A(:,:,1)+0.769*A(:,:,2)+0.189*A(:,:,3);
R(:,:,2)=0.349*A(:,:,1)+0.686*A(:,:,2)+0.168*A(:,:,3);
R(:,:,3)=0.272*A(:,:,1)+0.534*A(:,:,2)+0.131*A(:,:,3);

figure
subplot(121);imshow(A);title('Original')
subplot(122);imshow(R);title('Sepia')
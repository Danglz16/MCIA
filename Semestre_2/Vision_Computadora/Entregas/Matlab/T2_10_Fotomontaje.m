close all;
clc;

% Fondo
[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Fondo'); 
ruta=strcat(path,file);
A=imread(ruta);
A= im2double(A);

% Primer plano
[file2,path2] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Primer Plano');
ruta2=strcat(path2,file2);
B=imread(ruta2);
B= im2double(B);
[bx, by, bz] = size(B);
A=imresize(A,[bx by]);

% Mascara Binaria
[file3,path3] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Mascara Binaria');
ruta3=strcat(path3,file3);
C=imread(ruta3);
C=im2double(C);
C=im2gray(C);
C=imbinarize(C);


NOTC=not(C);
T1 = B.*NOTC;
T2 = A.*C;
R=T1+T2;

figure,
subplot(331); imshow(B);title('B');
subplot(332); imshow(NOTC);title('B');
subplot(333); imshow(T1);title('B');
subplot(334); imshow(A);title('B');
subplot(335); imshow(C);title('B');
subplot(336); imshow(T2);title('B');
subplot(337); imshow(T1);title('B');
subplot(338); imshow(T2);title('B');
subplot(339); imshow(R);title('B');

figure, imshow(R);

matlabroot
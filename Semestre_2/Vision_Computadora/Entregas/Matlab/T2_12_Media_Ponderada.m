clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen A'); 
ruta=strcat(path,file);
A=imread(ruta);
A= im2double(A);

[file2,path2] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen B');
ruta2=strcat(path2,file2);
B=imread(ruta2);
B= im2double(B);

B = imresize(B, [size(A,1) size(A,2)]);

figure;title('Media Ponderada de A y B');
subplot(131);imshow(A);title('A');
subplot(132);imshow(B);title('B');

R3= zeros(size(A));
for a=0.1:0.1:1
    R3=a*A + (1-a)*B;
    subplot(133);imshow(R3);title(a);
    pause(0.2);
end
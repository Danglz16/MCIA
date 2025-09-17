clear all;
close all;
clc

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = strcat(path,file);


A=imread(ruta);
A=im2double(A);

if length(size(A)) == 3
    A = rgb2gray(A);
end

figure, imshow(A);

% Matriz R
[ax,ay] = size(A);
az=3;
R = zeros(ax,ay,az);
vr=0;
vg=18/255.0;
vb=154/255.0;
for m =1:ax
    for n =1:ay
        % si A<128 entonces
		% R.R:= vr·A/128; R.G:= vg·A/128; R.B:= vb·A/128
        if A(m,n) < 0.5
            R(m,n,1) = (vr*A(m,n))*0.5;
            R(m,n,2) = (vg*A(m,n))*0.5;
            R(m,n,3) = (vb*A(m,n))*0.5;
        else
        end
    end
end
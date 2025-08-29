clear all;
close all;
clc;

[file,path] = uigetfile({'*.png';'*.jpg';'*.jpeg';...
                            '*.bmp';'*.gif'},...
                            'File Selector');
ruta=strcat(path,file);
A=imread(ruta);

A=im2double(A);

if length(size(A))==3
    [ax,ay,az]=size(A);
    R=zeros(size(A));
    for m=1:ax
        for n=1:ay
            for o=1:az
                R(m,n,o)=1-A(m,n,o); 
            end
        end
    end
    
end

if length(size(A))==2
[ax,ay]=size(A);
    R=zeros(size(A));
    for m=1:ax
        for n=1:ay
            R(m,n)=1-A(m,n); 
        end
    end
    
end
figure;
subplot(121);imshow(A);title('Imagen Original A(x,y)');
subplot(122);imshow(R);title('Negativo Imagen R(x,y)');
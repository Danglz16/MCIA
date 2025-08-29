clear all;
close all;
clc;

[file1,path1] = uigetfile({'*.png';'*.jpg';'*.jpeg';...
                            '*.bmp';'*.gif'},...
                            'File Selector');
ruta1=strcat(path1,file1);
A=imread(ruta1);
A=im2double(A);


[file2,path2] = uigetfile({'*.png';'*.jpg';'*.jpeg';...
                            '*.bmp';'*.gif'},...
                            'File Selector');
ruta2=strcat(path2,file2);
B=imread(ruta2);
B=im2double(B);
[bx by bz]=size(B);

A=imresize(A,[bx by]);
[ax ay az]=size(A);

R1=zeros(size(A));
R2=zeros(size(B));

% Minimo de 2 imagenes
for m=1:ax
    for n=1:ay
        for o=1:az
            if(A(m,n,o)<=B(m,n,o))
                R1(m,n,o)=A(m,n,o);
            else
                R1(m,n,o)=B(m,n,o);
            end
        end
    end
end

% Maximo de 2 imagenes
for m=1:ax
    for n=1:ay
        for o=1:az
            if(A(m,n,o)>=B(m,n,o))
                R2(m,n,o)=A(m,n,o);
            else
                R2(m,n,o)=B(m,n,o);
            end
        end
    end
end

figure;
subplot(221);imshow(A);title('A');
subplot(222);imshow(B);title('B');
subplot(223);imshow(R1);title('min(A,B)');
subplot(224);imshow(R2);title('max(A,B)');



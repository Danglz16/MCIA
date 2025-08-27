clear all;
close all;
clc;

[file1,path1] = uigetfile({'*.png';'*.jpg';'*.jpeg';...
                            '*.bmp';'*.gif'},...
                            'File Selector');
ruta1=strcat(path1,file1);
A=imread(ruta1);

if length(size(A))==3
    A=rgb2gray(A);
end

A=imbinarize(A);
[file2,path2] = uigetfile({'*.png';'*.jpg';'*.jpeg';...
                            '*.bmp';'*.gif'},...
                            'File Selector');
ruta2=strcat(path2,file2);
B=imread(ruta2);

if length(size(B))==3
    B=rgb2gray(B);
end

B=imbinarize(B);

[ax ay]=size(A);
B=imresize(B,[ax ay]);

R1=zeros(size(A));
R1=and(A,B);
R2=zeros(size(A));
R2=or(A,B);
R3=zeros(size(A));
R3=xor(A,B);

figure,
subplot(2,3,1);imshow(A);title('A');
subplot(2,3,2);imshow(B);title('B');
subplot(2,3,4);imshow(R1);title('A AND B');
subplot(2,3,5);imshow(R2);title('A OR B');
subplot(2,3,6);imshow(R3);title('A XOR B');
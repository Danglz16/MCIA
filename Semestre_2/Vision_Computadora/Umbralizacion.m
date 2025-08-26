clear all;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';...
                            '*.bmp';'*.gif'},...
                            'File Selector');
ruta=strcat(path,file);

I=imread(ruta);
I=im2double(I);

%figure, imshow(A); title('Imagen Original');

if length(size(I)) == 3
    A = rgb2gray(I);
end

[ax, ay, az]=size(A);
umbral = 180/255;
R = zeros(size(A));

for m = 1:ax
    for n = 1:ay
        if A(m,n)>umbral
            R(m,n) = 1;
        else
            R(m,n) = 0;
        end
    end
end

figure, 
% subplot(131);imshow(I);title('Imagen Original');
% subplot(132);imshow(A);title('Imagen B/N');
subplot(133);imshow(R);title('Imagen Umbralizada');

% for umbral = 0.05:0.05:0.95
%     R = imbinarize(A,umbral);
%     subplot(133);imshow(R);title(umbral);
%     pause(0.5);
% end
%imwrite(R,'dgb2.jpg','jpg')
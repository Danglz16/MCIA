clear;
close all;
clc;

[file,path] = uigetfile({'*.*';'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = strcat(path,file);
A = imread(ruta);
A = im2double(A);

% Matriz de conversión RGB a YUV
M_YUV = [0.30 0.59 0.11; -0.15 -0.29 0.44; 0.62 -0.52 -0.10];

% Matriz de conversión RGB a YIQ
M_YIQ = [0.30 0.59 0.11; 0.60 -0.27 -0.32; 0.21 -0.52 0.31];

[h, w, ~] = size(A);
A_reshaped = reshape(A, [], 3)'; % 3 x N

YUV = M_YUV * A_reshaped;
YIQ = M_YIQ * A_reshaped;

YUV_img = reshape(YUV', h, w, 3);
YIQ_img = reshape(YIQ', h, w, 3);

figure, imshow(A), title('Original RGB');
figure, imshow(YUV_img(:,:,1), []), title('Canal Y (YUV)');
figure, imshow(YUV_img(:,:,2), []), title('Canal U (YUV)');
figure, imshow(YUV_img(:,:,3), []), title('Canal V (YUV)');
figure, imshow(YIQ_img(:,:,1), []), title('Canal Y (YIQ)');
figure, imshow(YIQ_img(:,:,2), []), title('Canal I (YIQ)');
figure, imshow(YIQ_img(:,:,3), []), title('Canal Q (YIQ)'); 
close all;
clc;

[file1,path1] = uigetfile({'*.png';'*.jpg';'*.jpeg';'*.bmp';'*.gif'},'File Selector');

ruta1=strcat(path1,file1);

A=imread(ruta1);
A=im2double(A);

% Canales RGB (convertidos a 0-255)
A_R = A(:,:,1) * 255;
A_G = A(:,:,2) * 255;
A_B = A(:,:,3) * 255;

num_puntos = 600;
idx = randperm(numel(A_R), min(num_puntos, numel(A_R))); 
R = A_R(idx);
G = A_G(idx);
B = A_B(idx);

figure('Color', 'white', 'Position', [100, 100, 1200, 400]);
subplot(141); imshow(A);title('Imagen original');

% Histograma: Canal Rojo vs Canal Verde
subplot(142);scatter(R, G, 10, 'k', 'filled');
xlabel('Canal Rojo (0-255)', 'Color', [1 0 0], 'FontWeight', 'bold');
ylabel('Canal Verde (0-255)', 'Color', [0 0.5 0], 'FontWeight', 'bold');
title('Canales R y G', 'FontSize', 12);
grid on;
xlim([0 255]); ylim([0 255]);
ax = gca;
ax.XColor = [1 0 0];
ax.YColor = [0 0.5 0];
ax.YDir = 'reverse';

% Histograma: Canal Verde vs Canal Azul 
subplot(143); scatter(G, B, 10, 'k', 'filled');
xlabel('Canal Verde (0-255)', 'Color', [0 0.5 0], 'FontWeight', 'bold');
ylabel('Canal Azul (0-255)', 'Color', [0 0 1], 'FontWeight', 'bold');
title('Canales G y B', 'FontSize', 12);
grid on;
xlim([0 255]); ylim([0 255]);
ax = gca;
ax.XColor = [0 0.5 0];
ax.YColor = [0 0 1];
ax.YDir = 'reverse';

% Histograma: Canal Rojo vs Canal Azul
subplot(144); scatter(R, B, 10, 'k', 'filled');
xlabel('Canal Rojo (0-255)', 'Color', [1 0 0], 'FontWeight', 'bold');
ylabel('Canal Azul (0-255)', 'Color', [0 0 1], 'FontWeight', 'bold');
title('Canales R y B', 'FontSize', 12);
grid on;
xlim([0 255]); ylim([0 255]);
ax = gca;
ax.XColor = [1 0 0];
ax.YColor = [0 0 1];
ax.YDir = 'reverse';

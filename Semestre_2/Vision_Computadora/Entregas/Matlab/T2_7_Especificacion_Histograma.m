close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = fullfile(path, file);

A = imread(ruta);
A = im2double(A);

figure;
subplot(231); imshow(A); title('Imagen A');
subplot(232); imhist(A); title('Histograma de A');

% Definir histograma de referencia. Se puede modificar por uniforme, gaussiano o exponencial. 
tipo_histograma = 'gaussiano'; 
switch lower(tipo_histograma)
    case 'uniforme'
        hist_ref = ones(256, 1) / 256; % Divide a la distribucion en nbins iguales
        
    case 'gaussiano'
        x = 0:255;  % Rango de x
        mu = 180;   % Media 
        sigma = 30; % Desviación estandar
        hist_ref = exp(-((x - mu).^2) / (2 * sigma^2))';
        hist_ref = hist_ref / sum(hist_ref);
        
    case 'exponencial'
        x = 0:255;
        lambda = 0.02;
        hist_ref = lambda * exp(-lambda * x)';
        hist_ref = hist_ref / sum(hist_ref);
end

% Calcular CDFs normalizando por el total de pixeles
cdf_A = cumsum(imhist(A)) / numel(A); 
cdf_ref = cumsum(hist_ref);

% Mapeo de intensidades usando interpolacion
R = zeros(size(A));
for i = 1:numel(A)
    [~, idx] = min(abs(cdf_ref - cdf_A(round(A(i)*255)+1)));
    R(i) = (idx-1)/255;
end

% Visualización de R
subplot(233); bar(0:255, hist_ref, 'FaceColor', [0.5 0.5 0.5]);
title('Histograma de referencia'); xlim([0 255]);
subplot(234); imshow(R); title('A transformada');
subplot(235); imhist(R); title('Histograma transformado');

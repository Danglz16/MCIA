clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen A'); 
ruta=strcat(path,file);
A=imread(ruta);
A= im2double(A);

% Crear filtros 2D  (media y gaussiano)
media11 = fspecial('average', [11 11]);      % Filtro media 11x11
media21 = fspecial('average', [21 21]);      % Filtro media 21x21
gauss21 = fspecial('gaussian', [21 21], 5);  % Filtro gaussiano 21x21 (σ = 5)
gauss41 = fspecial('gaussian', [41 41], 10); % Filtro gaussiano 41x41 (σ = 10)

% Aplicar filtros 
R1 = imfilter(A, media11, 'replicate');   % Media 11x11
R2 = imfilter(A, media21, 'replicate');   % Media 21x21
R3 = imfilter(A, gauss21, 'replicate');   % Gaussiana 21x21
R4 = imfilter(A, gauss41, 'replicate');   % Gaussiana 41x41

% Mostrar resultados
figure;
subplot(2,2,1); imshow(R1); title('Media 11x11');
subplot(2,2,2); imshow(R2); title('Media 21x21');
subplot(2,2,3); imshow(R3); title('Gaussiana 21x21');
subplot(2,2,4); imshow(R4); title('Gaussiana 41x41');

% Crear filtros 1D (horizontales y verticales)
media_horiz = fspecial('average', [1 31]);       % Filtro media horizontal
media_vert  = fspecial('average', [31 1]);       % Filtro media vertical
gauss_horiz = fspecial('gaussian', [1 61], 10);  % Gaussiana horizontal σ=10
gauss_vert  = fspecial('gaussian', [61 1], 10);  % Gaussiana vertical σ=10

% Aplicar filtros 
R5 = imfilter(A, media_horiz, 'replicate');   % Media horizontal
R6 = imfilter(A, media_vert, 'replicate');    % Media vertical
R7 = imfilter(A, gauss_horiz, 'replicate');   % Gaussiana horizontal
R8 = imfilter(A, gauss_vert, 'replicate');    % Gaussiana vertical

%  Mostrar resultados 
figure;
subplot(2,2,1); imshow(R5); title('Media 31x1 (horizontal)');
subplot(2,2,2); imshow(R6); title('Media 1x31 (vertical)');
subplot(2,2,3); imshow(R7); title('Gaussiana 61x1 (horizontal)');
subplot(2,2,4); imshow(R8); title('Gaussiana 1x61 (vertical)');

%  Filtros 2D
tic;  % Inicia cronómetro para filtro de media 11x11
T1 = imfilter(A, media11, 'replicate');  % Aplica el filtro con borde replicado
t_media11 = toc;  % Registra el tiempo transcurrido

tic;  % Filtro de media 21x21
T2 = imfilter(A, media21, 'replicate');
t_media21 = toc;

tic;  % Filtro gaussiano 21x21
T3 = imfilter(A, gauss21, 'replicate');
t_gauss21 = toc;

tic;  % Filtro gaussiano 41x41
T4 = imfilter(A, gauss41, 'replicate');
t_gauss41 = toc;

%  Filtros 1D

tic;  % Filtro media horizontal 1x31
T5 = imfilter(A, media_horiz, 'replicate');
t_mediaH = toc;

tic;  % Filtro media vertical 31x1
T6 = imfilter(A, media_vert, 'replicate');
t_mediaV = toc;

tic;  % Filtro gaussiano horizontal 1x61
T7 = imfilter(A, gauss_horiz, 'replicate');
t_gaussH = toc;

tic;  % Filtro gaussiano vertical 61x1
T8 = imfilter(A, gauss_vert, 'replicate');
t_gaussV = toc;


% Mostrar tiempos 
fprintf('\nTiempos de ejecución (en segundos):\n');
fprintf('Media 11x11         : %.6f\n', t_media11);
fprintf('Media 21x21         : %.6f\n', t_media21);
fprintf('Gaussiana 21x21     : %.6f\n', t_gauss21);
fprintf('Gaussiana 41x41     : %.6f\n', t_gauss41);
fprintf('Media 31x1 (H)      : %.6f\n', t_mediaH);
fprintf('Media 1x31 (V)      : %.6f\n', t_mediaV);
fprintf('Gaussiana 61x1 (H)  : %.6f\n', t_gaussH);
fprintf('Gaussiana 1x61 (V)  : %.6f\n', t_gaussV);
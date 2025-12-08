clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen A'); 
ruta=strcat(path,file);
A=imread(ruta);
A= im2double(A);

% Convertir si es RGB
if size(A, 3) == 3
    Agris = rgb2gray(A);
else
    Agris = A;
end

% Binarizar la imagen.
ImBW = imbinarize(Agris, 0.5);

SE = [1 1 1
      1 1 1
      1 1 1];

% Dilatación
ImDil1 = imdilate(ImBW, SE);
ImDil2 = imdilate(ImDil1, SE);
ImDil3 = imdilate(ImDil2, SE);

% Erosión
ImEro1 = imerode(ImBW, SE);
ImEro2 = imerode(ImEro1, SE);
ImEro3 = imerode(ImEro2, SE);

% Resultados
figure;
subplot(2,3,1), imshow(ImBW);      title("Original");
subplot(2,3,2), imshow(ImDil1);    title("Dilatación 1");
subplot(2,3,3), imshow(ImDil2);    title("Dilatación 2"); 
subplot(2,3,4), imshow(ImEro1);    title("Erosión 1"); 
subplot(2,3,5), imshow(ImEro2);    title("Erosión 2");
subplot(2,3,6), imshow(ImEro3);    title("Erosión 3"); 

% Apertura (Opening) y Cierre (Closing)
Open = imopen(ImBW, SE);
Close = imclose(ImBW, SE);

% Resultados de Apertura y Cierre
figure;
subplot(1,3,1), imshow(ImBW);    title("Original"); 
subplot(1,3,2), imshow(Open);    title("Apertura (Open)");
subplot(1,3,3), imshow(Close);   title("Cierre (Close)");

% Borde Morfológico
% El borde morfológico es (Dilatación de la Imagen Original) - (Imagen Original)
Borde = imdilate(ImBW, SE) - ImBW; 

figure;
subplot(1,2,1), imshow(ImBW);    title("Original"); 
subplot(1,2,2), imshow(Borde);   title("Borde Morfológico");

% Esqueletización 

% Opción 1: Usando bwmorph con 'skel'
Esqueleto_bwmorph = bwmorph(ImBW, 'skel', Inf); 

% Opción 2: Usando bwskel
Esqueleto_bwskel = bwskel(ImBW); 

% Resultados esqueletización
figure;
subplot(1,3,1), imshow(ImBW);                title("Original");
subplot(1,3,2), imshow(Esqueleto_bwmorph);   title("Esqueleto (bwmorph 'skel')");
subplot(1,3,3), imshow(Esqueleto_bwskel);    title("Esqueleto (bwskel)");


close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen A'); 
ruta=strcat(path,file);
A=imread(ruta);
A= im2double(A);

[file2,path2] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen B');
ruta2=strcat(path2,file2);
B=imread(ruta2);
B= im2double(B);

B = imresize(B, [size(A,1) size(A,2)]);

% Operaciones Aritméticas básicas
suma = A + B;        
resta = A - B;
multiplicacion = A .* B; 
B_corr = B; 
B_corr(B_corr < 1e-5) = 1e-5; % Evita división por cero
division = A ./ B_corr;

figure;
subplot(242); imshow(A); title('A');
subplot(243); imshow(B); title('B');
subplot(245); imshow(suma); title('A+B');
subplot(246); imshow(resta); title('A-B');
subplot(247); imshow(multiplicacion); title('A.*B');
subplot(248); imshow(division); title('A./B');

% Operaciones con corrección de saturación
% Suma con correccion de saturacion
a = 0.25;
suma_media = (A + B)/2;
suma_media_pon = a*A + (1-a)*B;

figure;
subplot(221); imshow(A); title('A');
subplot(223); imshow(B); title('B');
subplot(222); imshow(suma_media); title('(A+B)/2');
subplot(224); imshow(suma_media_pon); title(['A+B media ponderada (a=' num2str(a) ')']);

% Resta con correccion de saturacion
a_resta = 0.8;
resta_media = (A - B)/2;
resta_media_pon = a_resta*A - (1-a_resta)*B;

figure;
subplot(221); imshow(A); title('A');
subplot(223); imshow(B); title('B');
subplot(222); imshow(resta_media); title('(A-B)/2');
subplot(224); imshow(resta_media_pon); title(['A-B media ponderada(a=' num2str(a_resta) ')']);

% Multiplicación con correccion de saturacion
a_mult = 0.55;
multi_media = (A .* B)/2;
multi_media_pon = (a_mult*A) .* ((1-a_mult)*B);

figure;
subplot(221); imshow(A); title('A');
subplot(223); imshow(B); title('B');
subplot(222); imshow(multi_media); title('(A*B)/2');
subplot(224); imshow(multi_media_pon); title(['A*B media ponderada (a=' num2str(a_mult) ')']);

% División con correccion de saturacion
a_div = 0.25;
B_div = B;
B_div(B_div < 1e-5) = 1e-5;
div_media = (A ./ B_div)/2;
div_media_pon = (a_div*A) ./ ((1-a_div)*B_div); 

figure;
subplot(221); imshow(A); title('A');
subplot(223); imshow(B); title('B');
subplot(222); imshow(div_media); title('(A/B)/2');
subplot(224); imshow(div_media_pon); title(['A/B media ponderada (a=' num2str(a_div) ')']);
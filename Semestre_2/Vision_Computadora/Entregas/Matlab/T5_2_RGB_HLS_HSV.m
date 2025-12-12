clear;
close all;
clc;

[file,path] = uigetfile({'*.*';'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');
ruta = strcat(path,file);
img_original_uint8 = imread(ruta);

if size(img_original_uint8, 3) ~= 3
    img_rgb_double = repmat(im2double(img_original_uint8), [1 1 3]);
else
    img_rgb_double = im2double(img_original_uint8); 
end

% Separar los canales R, G, B
R = img_rgb_double(:,:,1);
G = img_rgb_double(:,:,2);
B = img_rgb_double(:,:,3);

% Obtener las dimensiones de la imagen
[rows, cols, ~] = size(img_rgb_double);

% Cálculo de MAX y MIN
MAX = max(max(R, G), B);
MIN = min(min(R, G), B);

% Diferencia entre MAX y MIN
Delta = MAX - MIN;

Delta(Delta == 0) = 1e-6;

% Inicializar canales HSV y HLS
H = zeros(rows, cols);
S_hsv = zeros(rows, cols);
S_hls = zeros(rows, cols);

% CÁLCULO DE H (Hue / Tono)

% Donde R es MAX
mask_R_max = (R == MAX);
H(mask_R_max) = ((G(mask_R_max) - B(mask_R_max)) ./ Delta(mask_R_max)) * 60;

% Donde G es MAX
mask_G_max = (G == MAX);
H(mask_G_max) = (((B(mask_G_max) - R(mask_G_max)) ./ Delta(mask_G_max)) * 60) + 120;

% Donde B es MAX
mask_B_max = (B == MAX);
H(mask_B_max) = (((R(mask_B_max) - G(mask_B_max)) ./ Delta(mask_B_max)) * 60) + 240;

% Ajustar H para que esté en el rango [0, 360) grados
% Si H es negativo, sumar 360
H(H < 0) = H(H < 0) + 360;

% CÁLCULO DE S (Saturation) y V (Value/Brillo) para HSV
V = MAX;
% S_hsv = (MAX - MIN) / MAX
% Evitar división por cero si MAX es 0 (negro puro)
mask_MAX_zero = (MAX == 0);
S_hsv(~mask_MAX_zero) = Delta(~mask_MAX_zero) ./ MAX(~mask_MAX_zero);
S_hsv(mask_MAX_zero) = 0; % Si MAX es 0, la saturación es 0

% CÁLCULO DE S (Saturation) y L (Luminance) para HLS
L = (MAX + MIN) / 2;

% Para evitar división por cero en la S de HLS (fórmula estándar HLS)
mask_den_zero = (L == 0) | (L == 1);
denominador = (1 - abs(2 * L - 1));
denominador(denominador == 0) = 1e-6; % Evitar división por cero

S_hls(~mask_den_zero) = Delta(~mask_den_zero) ./ denominador(~mask_den_zero);
S_hls(mask_den_zero) = 0; % Si el denominador es 0, saturación es 0


% Normalización y Preparación para Visualización
S_hsv_norm = S_hsv; 
V_norm = V;         
S_hls_norm = S_hls; 
L_norm = L;         

% El H de 0-360 grados debe normalizarse a 0-1
H_norm = H / 360.0;


% Convertir de vuelta a RGB para visualización
% Combinar canales H, S, V para HSV y convertir a RGB
% H debe estar en [0,1] para hsv2rgb
hsv_matrix = cat(3, H_norm, S_hsv_norm, V_norm);
img_hsv_to_rgb = hsv2rgb(hsv_matrix);


% Visualización de Resultados
figure('Units', 'normalized', 'Position', [0.1 0.1 0.8 0.8]); % Ajusta el tamaño de la figura

% Original RGB
subplot(2, 4, 1);
imshow(img_rgb_double);
title("Original RGB");
axis off;

% Componentes HSV
subplot(2, 4, 2);
imshow(H_norm, []); % [] para que imshow escale el rango del double
colormap(gca, 'gray'); % Para que H se vea en escala de grises
title("H (Tono) - HSV");
axis off;

subplot(2, 4, 3);
imshow(S_hsv_norm, []);
colormap(gca, 'gray');
title("S (Saturación) - HSV");
axis off;

subplot(2, 4, 4);
imshow(V_norm, []);
colormap(gca, 'gray');
title("V (Valor/Brillo) - HSV");
axis off;

% Reconstrucción HSV a RGB
subplot(2, 4, 5);
imshow(img_hsv_to_rgb);
title("Reconstrucción HSV a RGB");
axis off;

% Componentes HLS
subplot(2, 4, 6);
imshow(H_norm, []);
colormap(gca, 'gray');
title("H (Tono) - HLS");
axis off;

subplot(2, 4, 7);
imshow(S_hls_norm, []);
colormap(gca, 'gray');
title("S (Saturación) - HLS");
axis off;

subplot(2, 4, 8);
imshow(L_norm, []);
colormap(gca, 'gray');
title("L (Luminosidad) - HLS");
axis off;

pause; % Espera a que el usuario presione una tecla
close all; % Cierra todas las figuras
clear;
close all;
clc;

[file,path] = uigetfile({'*.*';'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'}, 'File Selector');

ruta = strcat(path,file);
A=imread(ruta);
A=im2double(A);

% Determinar si la imagen es a color o escala de grises
esColor = (ndims(A) == 3);
[filas_original, columnas_original, num_canales] = size(A);

%PLOTS
total_plots = 8; 
num_filas_subplot = 3;
num_columnas_subplot = 3;
plot_idx = 1; 

figure(); 
subplot(num_filas_subplot, num_columnas_subplot, plot_idx); plot_idx = plot_idx + 1;
imshow(A);
title('Imagen Original');


%  Traslación Manual
% Parámetros de traslación
dx_tras = 50; % Traslado en X (columnas a la derecha)
dy_tras = 30; % Traslado en Y (filas hacia abajo)

R_traslacion_manual = zeros(size(A), class(A));
for m_nueva = 1 + dy_tras : filas_original
    for n_nueva = 1 + dx_tras : columnas_original
        m_original = m_nueva - dy_tras;
        n_original = n_nueva - dx_tras;
        if esColor
            R_traslacion_manual(m_nueva, n_nueva, :) = A(m_original, n_original, :);
        else
            R_traslacion_manual(m_nueva, n_nueva) = A(m_original, n_original);
        end
    end
end
subplot(num_filas_subplot, num_columnas_subplot, plot_idx); plot_idx = plot_idx + 1;
imshow(R_traslacion_manual);
title(sprintf('Traslación (dx=%d, dy=%d)', dx_tras, dy_tras));


% Rotación 
% Ángulos de rotación en grados
angulos_rotacion = [-10, 10]; 

theta_rad_max = deg2rad(max(abs(angulos_rotacion)));
cos_theta = abs(cos(theta_rad_max));
sin_theta = abs(sin(theta_rad_max));

nueva_filas_rot = ceil(filas_original * cos_theta + columnas_original * sin_theta);
nueva_columnas_rot = ceil(filas_original * sin_theta + columnas_original * cos_theta);

centro_orig_x = columnas_original / 2;
centro_orig_y = filas_original / 2;

centro_nueva_x = nueva_columnas_rot / 2;
centro_nueva_y = nueva_filas_rot / 2;


% Rotaciones con Interpolación de Vecino Más Próximo
for i = 1:length(angulos_rotacion)
    angulo = angulos_rotacion(i);
    theta_rad = deg2rad(angulo);

    R_rotacion_NN = zeros(nueva_filas_rot, nueva_columnas_rot, num_canales, class(A));

    for m_out = 1 : nueva_filas_rot
        for n_out = 1 : nueva_columnas_rot
            x_out_centrado = n_out - centro_nueva_x;
            y_out_centrado = m_out - centro_nueva_y;

            x_orig_centrado = x_out_centrado * cos(theta_rad) + y_out_centrado * sin(theta_rad);
            y_orig_centrado = -x_out_centrado * sin(theta_rad) + y_out_centrado * cos(theta_rad);
            
            x_orig = x_orig_centrado + centro_orig_x;
            y_orig = y_orig_centrado + centro_orig_y;

            x_pixel = round(x_orig);
            y_pixel = round(y_orig);

            if x_pixel >= 1 && x_pixel <= columnas_original && ...
               y_pixel >= 1 && y_pixel <= filas_original
                if esColor
                    R_rotacion_NN(m_out, n_out, :) = A(y_pixel, x_pixel, :);
                else
                    R_rotacion_NN(m_out, n_out) = A(y_pixel, x_pixel);
                end
            end
        end
    end
    
    subplot(num_filas_subplot, num_columnas_subplot, plot_idx); plot_idx = plot_idx + 1;
    imshow(R_rotacion_NN);
    if angulo == -10
        title('Rotar -10º (Vecino Más Próximo)');
    elseif angulo == 10
        title('Rotar 10º (Vecino Más Próximo)');
    end
end


% Rotación con Interpolación Bilineal (para -10 grados para comparación)
disp('Calculando rotación con interpolación Bilineal...');
angulo_bilinear = -10; 
theta_rad_bilinear = deg2rad(angulo_bilinear);

R_rotacion_Bilinear = zeros(nueva_filas_rot, nueva_columnas_rot, num_canales, class(A));

for m_out = 1 : nueva_filas_rot
    for n_out = 1 : nueva_columnas_rot
        x_out_centrado = n_out - centro_nueva_x;
        y_out_centrado = m_out - centro_nueva_y;

        x_orig_centrado = x_out_centrado * cos(theta_rad_bilinear) + y_out_centrado * sin(theta_rad_bilinear);
        y_orig_centrado = -x_out_centrado * sin(theta_rad_bilinear) + y_out_centrado * cos(theta_rad_bilinear);
        
        x_orig = x_orig_centrado + centro_orig_x;
        y_orig = y_orig_centrado + centro_orig_y;

        x1 = floor(x_orig);
        y1 = floor(y_orig);
        x2 = x1 + 1;
        y2 = y1 + 1;

        a = x_orig - x1;
        b = y_orig - y1;
        
        if x1 >= 1 && x2 <= columnas_original && ...
           y1 >= 1 && y2 <= filas_original
            if esColor
                for canal = 1:num_canales
                    val11 = A(y1, x1, canal);
                    val21 = A(y1, x2, canal);
                    val12 = A(y2, x1, canal);
                    val22 = A(y2, x2, canal);

                    R_rotacion_Bilinear(m_out, n_out, canal) = ...
                        val11 * (1-a) * (1-b) + ...
                        val21 * a * (1-b) + ...
                        val12 * (1-a) * b + ...
                        val22 * a * b;
                end
            else 
                val11 = A(y1, x1);
                val21 = A(y1, x2);
                val12 = A(y2, x1);
                val22 = A(y2, x2);

                R_rotacion_Bilinear(m_out, n_out) = ...
                    val11 * (1-a) * (1-b) + ...
                    val21 * a * (1-b) + ...
                    val12 * (1-a) * b + ...
                    val22 * a * b;
            end
        end
    end
end
subplot(num_filas_subplot, num_columnas_subplot, plot_idx); plot_idx = plot_idx + 1;
imshow(R_rotacion_Bilinear);
title('Rotación -10º (Bilineal)');


% Transformaciones de Escala

% Parámetros de escala
ax1 = 0.8; ay1 = 0.8;
ax2 = 2; ay2 = 0.5;

% Transformación de Escala R1 (Reducción)
nueva_filas_R1 = round(filas_original * ay1);
nueva_columnas_R1 = round(columnas_original * ax1);

R_escala_R1 = zeros(nueva_filas_R1, nueva_columnas_R1, num_canales, class(A));

for m_out = 1 : nueva_filas_R1
    for n_out = 1 : nueva_columnas_R1
        x_orig = n_out / ax1;
        y_orig = m_out / ay1;

        x1 = floor(x_orig); y1 = floor(y_orig);
        x2 = x1 + 1; y2 = y1 + 1;
        a = x_orig - x1; b = y_orig - y1;

        if x1 >= 1 && x2 <= columnas_original && y1 >= 1 && y2 <= filas_original
            if esColor
                for canal = 1:num_canales
                    val11 = A(y1, x1, canal); val21 = A(y1, x2, canal);
                    val12 = A(y2, x1, canal); val22 = A(y2, x2, canal);
                    R_escala_R1(m_out, n_out, canal) = ...
                        val11 * (1-a) * (1-b) + val21 * a * (1-b) + ...
                        val12 * (1-a) * b + val22 * a * b;
                end
            else 
                val11 = A(y1, x1); val21 = A(y1, x2);
                val12 = A(y2, x1); val22 = A(y2, x2);
                R_escala_R1(m_out, n_out) = ...
                    val11 * (1-a) * (1-b) + val21 * a * (1-b) + ...
                    val12 * (1-a) * b + val22 * a * b;
            end
        end
    end
end
subplot(num_filas_subplot, num_columnas_subplot, plot_idx); plot_idx = plot_idx + 1;
imshow(R_escala_R1);
title('Escala R1- Reducir al 80%%');


% Transformación de Escala R2 (Aumento en X, Reducción en Y)
nueva_filas_R2 = round(filas_original * ay2);
nueva_columnas_R2 = round(columnas_original * ax2);

R_escala_R2 = zeros(nueva_filas_R2, nueva_columnas_R2, num_canales, class(A));

for m_out = 1 : nueva_filas_R2
    for n_out = 1 : nueva_columnas_R2
        x_orig = n_out / ax2;
        y_orig = m_out / ay2;

        x1 = floor(x_orig); y1 = floor(y_orig);
        x2 = x1 + 1; y2 = y1 + 1;
        a = x_orig - x1; b = y_orig - y1;

        if x1 >= 1 && x2 <= columnas_original && y1 >= 1 && y2 <= filas_original
            if esColor
                for canal = 1:num_canales
                    val11 = A(y1, x1, canal); val21 = A(y1, x2, canal);
                    val12 = A(y2, x1, canal); val22 = A(y2, x2, canal);
                    R_escala_R2(m_out, n_out, canal) = ...
                        val11 * (1-a) * (1-b) + val21 * a * (1-b) + ...
                        val12 * (1-a) * b + val22 * a * b;
                end
            else 
                val11 = A(y1, x1); val21 = A(y1, x2);
                val12 = A(y2, x1); val22 = A(y2, x2);
                R_escala_R2(m_out, n_out) = ...
                    val11 * (1-a) * (1-b) + val21 * a * (1-b) + ...
                    val12 * (1-a) * b + val22 * a * b;
            end
        end
    end
end
subplot(num_filas_subplot, num_columnas_subplot, plot_idx); plot_idx = plot_idx + 1;
imshow(R_escala_R2);
title(sprintf('Escala R2 (ax=%.1f, ay=%.1f) ', ax2, ay2));

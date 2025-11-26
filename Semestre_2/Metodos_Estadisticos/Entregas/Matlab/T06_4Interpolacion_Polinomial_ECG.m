close all;
clc;

%% Interpolación polinomial con una señal de ECG

x_mat = load('../Datos/100m.mat');
ecg_val = x_mat.val;
ecg = (ecg_val - 0) / 200;
ecg = ecg';

fs = 360;
ts = 1/fs;

ecg = ecg(:, 2);
t = (0:length(ecg)-1) * ts;

n_puntos = 512;
x_data_ecg = t(1:n_puntos);
y_data_ecg = ecg(1:n_puntos);

figure;
plot(t, ecg);
xlabel('Tiempo (s)');
ylabel('Amplitud (mV)');
title('Señal de ECG Original');
grid on;

%% Interpolación de Newton y tiempo de ejecución

tic;
newton_coef_ecg = newton_coeffs_improved(x_data_ecg, y_data_ecg);
x_interp_ecg = linspace(x_data_ecg(1), x_data_ecg(end), 512);
y_interp_ecg = zeros(size(x_interp_ecg));
for i = 1:length(x_interp_ecg)
    y_interp_ecg(i) = newton_eval(newton_coef_ecg, x_data_ecg, x_interp_ecg(i));
end
tiempo_ejecucion = toc;

fprintf('Tiempo de ejecución de la interpolación: %.4f segundos\n', tiempo_ejecucion);

%% Gráfica completa

figure;
plot(t, ecg, 'b', 'LineWidth', 0.5);
hold on;
plot(x_interp_ecg, y_interp_ecg, 'r', 'LineWidth', 1.2);
plot(x_data_ecg, y_data_ecg, 'go', 'MarkerSize', 3);
xlabel('Tiempo (s)');
ylabel('Amplitud (mV)');
title('Interpolación polinómica de Newton sobre señal ECG');
legend('ECG original', 'Interpolación Newton', 'Puntos de interpolación');
grid on;
hold off;

%% Zoom 512 puntos

figure;
plot(x_data_ecg, y_data_ecg, 'go-', 'MarkerSize', 3);
hold on;
plot(x_interp_ecg, y_interp_ecg, 'r-');
xlabel('Tiempo (s)');
ylabel('Amplitud (mV)');
title('Zoom: primeros 512 puntos con interpolación');
grid on;
margen_x = 0.2 * (x_data_ecg(end) - x_data_ecg(1));
xlim([x_data_ecg(1) - margen_x, x_data_ecg(end) + margen_x]);
y_min = min(y_data_ecg);
y_max = max(y_data_ecg);
margen_y = 0.5 * (y_max - y_min);
ylim([y_min - margen_y, y_max + margen_y]);
hold off;

%% Zoom primeros 30 puntos

segmento_zoom = 30;
margen_x_100 = 0.05 * (x_data_ecg(segmento_zoom) - x_data_ecg(1));
y_min_100 = min(y_data_ecg(1:segmento_zoom));
y_max_100 = max(y_data_ecg(1:segmento_zoom));
margen_y_100 = 0.1 * (y_max_100 - y_min_100);

figure;
plot(x_data_ecg(1:segmento_zoom), y_data_ecg(1:segmento_zoom), 'go-', 'MarkerSize', 3);
hold on;
idx_zoom = (x_interp_ecg >= x_data_ecg(1)) & (x_interp_ecg <= x_data_ecg(segmento_zoom));
plot(x_interp_ecg(idx_zoom), y_interp_ecg(idx_zoom), 'r-');
xlabel('Tiempo (s)');
ylabel('Amplitud (mV)');
title(sprintf('Zoom detallado: primeros %d puntos', segmento_zoom));
grid on;
xlim([x_data_ecg(1) - margen_x_100, x_data_ecg(segmento_zoom) + margen_x_100]);
ylim([y_min_100 - margen_y_100, y_max_100 + margen_y_100]);
hold off;

%% Funciones Newton

function coef_new = newton_coeffs_improved(x, f_x)
    n = length(x);
    F = zeros(n, n);
    F(:, 1) = f_x(:);
    for j = 2:n
        for i = 1:(n - j + 1)
            F(i, j) = (F(i+1, j-1) - F(i, j-1)) / (x(i+j-1) - x(i));
        end
    end
    coef_new = diag(F)';
end

function result = newton_eval(coef, x_data, x_val)
    n = length(coef);
    result = coef(n);
    for k = n-1:-1:1
        result = result .* (x_val - x_data(k)) + coef(k);
    end
end

clear all;
close all;
clc;

n = input('Escribe el Orden de la ecuacion: ');

x=[1 2 3 4 5 6 7];
% y=f(x)
y=[0.5 2.5 2.0 4.0 3.5 6.0 5.5];

N = length(x);
x = x(:); y = y(:);

% Precalcular sumas de potencias de x hasta 2n
Sx = zeros(1, 2*n + 1);  % Sx(k+1) = sum(x.^k)
for k = 0:2*n
    Sx(k+1) = sum(x.^k);
end

% Matriz A (tamaño (n+1)x(n+1))
A = zeros(n+1, n+1);
for i = 0:n
    for j = 0:n
        A(i+1, j+1) = Sx(i + j + 1);  % sum(x^(i+j))
    end
end

% Vector b
b = zeros(n+1, 1);
for i = 0:n
    b(i+1) = sum(y .* (x.^i));
end

p = A \ b;

y_hat = zeros(size(x));
for i = 0:n
    y_hat = y_hat + p(i+1) * (x.^i);
end

% Métricas
SS_res = sum((y - y_hat).^2);
SS_tot = sum((y - mean(y)).^2);
R2 = 1 - SS_res/SS_tot;

% R^2 ajustado (k = n predictores: x, x^2, ..., x^n)
k = n;
R2_adj = 1 - (1 - R2) * (N - 1) / (N - k - 1);

% Correlación entre y reales y y_hat
r_val = corr(y, y_hat);

% Graficar Curva
x_aux = linspace(min(x), max(x), 500).';
y_aux = zeros(size(x_aux));
for i = 0:n
    y_aux = y_aux + p(i+1) * (x_aux.^i);
end
figure;
plot(x, y, 'o', 'LineWidth', 3); grid on; hold on;
plot(x_aux, y_aux,'c', 'LineWidth', 2);
title(sprintf('Regresion Polinomica de grado n = %d', n));
xlabel('x'); ylabel('f(x)');
legend('Datos','Regresion Polinomica','Location','best');

fprintf('Coeficientes (x0..xn) en orden creciente de grado:\n');
disp(p.');
fprintf('R^2       = %.6f\n', R2);
fprintf('corr(y, y_hat) = %.6f\n', r_val);
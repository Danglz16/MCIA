close all;
clc;

% Puntos
x0 = 1;
f_x0 = log(x0);
x1 = 3;
f_x1 = log(x1);
x2 = 6;
f_x2 = log(x2);

% Punto a interpolar
x = 2;

%  Interpolación polinomial (Newton, grado 2)

% Diferencias divididas (coeficientes de Newton)
b0 = f_x0;
b1 = (f_x1 - f_x0) / (x1 - x0);
b2 = ( ((f_x2 - f_x1) / (x2 - x1)) - ((f_x1 - f_x0) / (x1 - x0)) ) / (x2 - x0);

% Polinomio en el punto x
f2_x = b0 + b1*(x - x0) + b2*(x - x0)*(x - x1);

% Valor real
f_x_real = log(x);

% Curva real
x_real = x0:0.01:x2;
f_real = log(x_real);

% Polinomio de Newton en todo el intervalo
f_newton = b0 + b1*(x_real - x0) + b2.*(x_real - x0).*(x_real - x1);

% --- Gráfica ---
figure;
plot(x_real, f_real, 'LineWidth', 2);
hold on;
grid on;
title('Interpolación Polinomial (Newton, grado 2)');
xlabel('X');
ylabel('Log(x)');

% Puntos base
plot(x0, f_x0, 'ro', 'LineWidth', 2);
plot(x1, f_x1, 'ro', 'LineWidth', 2);
plot(x2, f_x2, 'ro', 'LineWidth', 2);

x_vec = [x0 x1 x2];
y_vec = [f_x0 f_x1 f_x2];
plot(x_vec, y_vec, 'r', 'LineWidth', 2); 

% Polinomio interpolante
plot(x_real, f_newton, 'g--', 'LineWidth', 2);

% Punto real vs punto interpolado
plot(x, f_x_real, 'bo', 'LineWidth', 2);
plot(x, f2_x, 'go', 'LineWidth', 2);

legend('Real', 'Puntos base', 'Línea base', ...
       'Polinomio Newton', 'Real en x', 'Interpolado', ...
       'Location', 'best');


close all;
clc;

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

% Interpolación cuadrática (Lagrange)
L0 = ((x - x1)*(x - x2)) / ((x0 - x1)*(x0 - x2));
L1 = ((x - x0)*(x - x2)) / ((x1 - x0)*(x1 - x2));
L2 = ((x - x0)*(x - x1)) / ((x2 - x0)*(x2 - x1));

f2_x = f_x0*L0 + f_x1*L1 + f_x2*L2;

% Valor real
f_x_real = log(x);

% Curva real
x_real = x0:0.01:x2;
f_real = log(x_real);

% --- Gráfica ---
figure;
plot(x_real, f_real, 'LineWidth', 2);
title('Interpolación Cuadrática');
xlabel('X');
ylabel('Log(x)');
grid on;
hold on;

plot(x0, f_x0, 'ro', 'LineWidth', 2);
plot(x1, f_x1, 'ro', 'LineWidth', 2);
plot(x2, f_x2, 'ro', 'LineWidth', 2);

x_vec = [x0 x1 x2];
y_vec = [f_x0 f_x1 f_x2];
plot(x_vec, y_vec, 'r', 'LineWidth', 2); 

plot(x, f_x_real, 'bo', 'LineWidth', 2);
plot(x, f2_x, 'go', 'LineWidth', 2);
legend('Real', 'Puntos base', 'Línea base', 'Real en x', 'Interpolado');

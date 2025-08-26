clear all;
close all;
clc;

x=[1 2 3 4 5 6 7];
% y=f(x)
y=[0.5 2.5 2.0 4.0 3.5 6.0 5.5];

figure;
plot(x,y,'o','LineWidth',3); grid on;
title('Regresion Cuadratica');
xlabel('x'); ylabel('f(x)');

% Elementos de A
n      = length(x);
Sx     = sum(x);
Sx2    = sum(x.^2);
Sx3    = sum(x.^3);
Sx4    = sum(x.^4);
Sy     = sum(y);
Sxy    = sum(x.*y);
Sx2y   = sum((x.^2).*y);

% Matriz
A = [ n    Sx    Sx2;
      Sx   Sx2   Sx3;
      Sx2  Sx3   Sx4 ];

b = [ Sy; Sxy; Sx2y ];

% Coeficientes
r = A\b
a0 = r(1); a1 = r(2); a2 = r(3);

% Curva
x_aux = linspace(x(1), x(end), 500);
y_aux = a0 + a1*x_aux + a2*(x_aux.^2);

% Grafica
hold on;
plot(x_aux, y_aux, 'LineWidth', 2);
legend('Datos','Regresion Cuadratica','Location','best');

% Coef. Determinación / Correlación
y_hat = a0 + a1*x + a2*(x.^2);

SS_res = sum((y - y_hat).^2);
SS_tot = sum((y - mean(y)).^2);
R2 = 1 - SS_res/SS_tot;   
r_val = corr(y(:), y_hat(:)); 
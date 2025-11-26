clear;
close all;
clc;
syms x

% --- Función polinómica ---
f_poly = x^4 - 3*x^2 + 2;
a1 = 1;                 % punto de expansión
n1 = 4;                 % orden (>= grado del polinomio para exactitud)
t_poly = taylor(f_poly, x, a1, 'Order', n1+1);
fprintf('Polinómica: f(x) = x^4 - 3x^2 + 2, expandida en a = %g, orden = %d\n', a1, n1);
disp(t_poly);

% Tabla polinómica
x_vals = (-2:0.5:3).';
f_poly_num = matlabFunction(f_poly);
t_poly_num = matlabFunction(t_poly);
tab_poly = table(x_vals, f_poly_num(x_vals), t_poly_num(x_vals), ...
                 abs(f_poly_num(x_vals) - t_poly_num(x_vals)), ...
                 'VariableNames', {'x','f_real','f_taylor','error_abs'});
disp('Tabla polinómica:');
disp(tab_poly);

% --- Función trigonométrica ---
f_trig = sin(x);
a2 = 0;                 % Maclaurin
n2 = 9;                 % orden impar para sin (hasta x^9)
t_trig = taylor(f_trig, x, a2, 'Order', n2+1);
fprintf('\nTrigonométrica: f(x) = sin(x), expandida en a = %g, orden = %d\n', a2, n2);
disp(t_trig);

% Tabla trigonométrica
x_vals2 = (-pi:pi/6:pi).';
f_trig_num = matlabFunction(f_trig);
t_trig_num = matlabFunction(t_trig);
tab_trig = table(x_vals2, f_trig_num(x_vals2), t_trig_num(x_vals2), ...
                 abs(f_trig_num(x_vals2) - t_trig_num(x_vals2)), ...
                 'VariableNames', {'x','f_real','f_taylor','error_abs'});
disp('Tabla trigonométrica:');
disp(tab_trig);

clear;
close all;
clc;

xt=[0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0,...
    9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3];
f_x=[1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, ...
    2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25];

plot(xt,f_x,'o','LineWidth',2);
title('Interpolacion Segmentaria Cuadratica');
xlabel('x');
ylabel('f(x)');
grid on;

len = length(xt);

for n = 1:len-2
    x0 = xt(n);     y0 = f_x(n);
    x1 = xt(n+1);   y1 = f_x(n+1);
    x2 = xt(n+2);   y2 = f_x(n+2);
    
    A = [x0^2 x0 1;
         x1^2 x1 1;
         x2^2 x2 1];
    coef = A\[y0; y1; y2];
    
    a = coef(1);
    b = coef(2);
    c = coef(3);
    
    x = x0:0.01:x1;
    fx_ = a*x.^2 + b*x + c;
    
    hold on;
    plot(x,fx_,'r','Linewidth',2);
    
    pause(1);
end
figure;
plot(xt,f_x,'o','LineWidth',2);
title('Interpolacion Segmentaria Cuadratica (MATLAB spline)');
xlabel('x');
ylabel('f(x)');
grid on;
axis = ([0 14 0 2]);
hold on;

x_dense = xt(1):0.01:xt(end);
f_spline = spline(xt, f_x, x_dense);

plot(x_dense, f_spline, 'r', 'LineWidth',2);
clear;
close all;
clc;

xt=[0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0,...
    9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3];
f_x=[1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, ...
    2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25];


plot(xt,f_x,'o','LineWidth',2);
title('Interpolacion Segementaria Lineal');
xlabel('x');
ylabel('f(x)');
grid on;
len=length(xt); 

for n=1:len-1
    m = (f_x(n+1)-f_x(n))/(xt(n+1)-xt(n));
    x=xt(n):0.01:xt(n+1);
    fx_=f_x(n)+m*(x-xt(n));
    hold on;
    plot(x,fx_,'r','Linewidth',2);
    if n > 4
        plot(x,fx_,'r','Linewidth',2);
    end
    
    pause(1);
end

figure;
plot(xt,f_x,'o','LineWidth',2);
title('Interpolacion Segmentaria Cubica (MATLAB spline)');
xlabel('x');
ylabel('f(x)');
grid on;
axis = ([0 14 0 2]);
hold on;

x_dense = xt(1):0.01:xt(end);
f_spline = spline(xt, f_x, x_dense);

plot(x_dense, f_spline, 'r', 'LineWidth',2);
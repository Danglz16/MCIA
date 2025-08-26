clear all;
close all;
clc;

x0 = 1;
f_x0 = log(x0);
x1 = 6;
f_x1 = log(x1);
x = 2;
f1_x = f_x0+(((f_x1-f_x0)/(x1-x0))*(x-x0));

f1_x_ver = log(x);

x_real = x0:0.01:x1;
f_real = log(x_real);

figure;
plot(x_real,f_real,'LineWidth',2);
title('Interpolación Lineal')
xlabel('X');
ylabel('Log(x)');
grid on;
hold on;
plot(x0,f_x0,'ro','LineWidth',2);
plot(x1,f_x1,'ro','LineWidth',2);

x_vec = [x0 x1];
y_vec = [f_x0 f_x1];
line(x_vec,y_vec,'Color','red');

plot(x,f1_x_ver,'bo','LineWidth',2)
plot(x,f1_x,'ro','LineWidth',2)
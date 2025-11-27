clear;
close all;
clc;

M = readmatrix('../Datos/puntos_mano.csv');
x = M(:,1);
y = M(:,2);

plot(x,y,'ob','Linewidth',2)
ylabel('f(x)');
xlabel('x');
axis = ([0 30 0 42]);
title('Curva Paramétrica para Mano');
grid on;
hold on;

tam = length(y);
t   = linspace(0,10,tam);
t2  = 0:0.01:10;

xt = spline(t,x,t2);
yt = spline(t,y,t2);

plot(xt,yt,'Linewidth',2);
leg = legend('Puntos','Curva');

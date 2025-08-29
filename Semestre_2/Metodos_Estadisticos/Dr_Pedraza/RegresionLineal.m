clear all;
close all;
clc;

x=[1 2 3 4 5 6 7];
% y=f(x)
y=[0.5 2.5 2.0 4.0 3.5 6.0 5.5];

figure,
plot(x,y,'o','LineWidth',3);
title('Regresion Lineal de un conjunto de puntos');
xlabel('x');
ylabel('f(x)');
grid on;

n=length(x);

sum_xi=sum(x);
sum_xi2=sum(x.^2);

sum_yi=sum(y);
sum_xiyi=sum(x.*y);

A=[    n   sum_xi
    sum_xi sum_xi2];
b=[sum_yi
   sum_xiyi];

r=inv(A)*b;
a0=r(1);
a1=r(2);
x_aux=x(1):0.01:x(n);
%x_aux=x(1):(x(n)-x(1))/100:x(n);
y_aux=a0+(a1*x_aux);

hold on;
plot(x_aux,y_aux,'LineWidth',2);

legend('Datos','Regresion Lineal');


clear all;
close all;
clc;

x0=1;
x1=2.5;
x2=4;

f_x0=log(x0);
f_x1=log(x1);
f_x2=log(x2);

xi=x0:0.01:x2;

fxi=log(xi);

x=2;
f1_ver=log(x);

figure;
plot(xi,fxi,'LineWidth',2);
title('Interpolacion Cuadrática de f(x)=ln(x)');
xlabel('x');
ylabel('ln(x)');
grid on;
hold on;

plot(x0,f_x0,'bo','LineWidth',2);
plot(x1,f_x1,'bo','LineWidth',2);
plot(x2,f_x2,'bo','LineWidth',2);
plot(x,f1_ver,'ro','LineWidth',2);

b0=f_x0;
f_x1_x0=(f_x1-f_x0)/(x1-x0);
b1=f_x1_x0;
f_x2_x1=(f_x2-f_x1)/(x2-x1);
f_x2_x1_x0=(f_x2_x1-f_x1_x0)/(x2-x0);
b2=f_x2_x1_x0;

a0=b0-b1*x0+b2*x0*x1;
a1=b1-b2*x0-b2*x1;
a2=b2;

x_ref=x0:0.01:x2;
f2_x=a0+a1*x_ref+a2*x_ref.^2;

plot(x_ref,f2_x,'c','LineWidth',2);

x_sqr=2;
f_sqr=a0+a1*x_sqr+a2*x_sqr.^2;
plot(x_sqr,f_sqr,'co','LineWidth',2);

Ev=abs(((f1_ver-f_sqr)/f1_ver)*100)

axis square;


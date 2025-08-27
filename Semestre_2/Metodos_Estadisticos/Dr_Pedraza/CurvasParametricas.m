clear all;
close all;
clc;
xi=[-1 0 1 0 1];
yi=[0 1 0.5 0 -1];


n=length(xi);
t=linspace(0,1,100);

x_t=(((64*t-(352/3)).*t+60).*t-(14/3)).*t-1;

y_t=((((-64/3)*t+48).*t-(116/3)).*t+11).*t;

figure;
subplot(121);
plot(t,x_t,'r','LineWidth',3); title('Curva parametrica para x(t)');
xlabel('t');ylabel('x(t)');
grid on;
subplot(122);
plot(t,y_t,'r','LineWidth',3); title('Curva parametrica para y(t)');
xlabel('t');ylabel('y(t)');
grid on;

figure;
plot(xi,yi,'o','LineWidth',3);
grid on;
hold on;
plot(x_t,y_t,'r','LineWidth',3);
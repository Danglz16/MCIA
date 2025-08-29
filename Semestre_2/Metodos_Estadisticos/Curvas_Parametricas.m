clear all;
close all;
clc;

xi = [-1 0 1 0 1];
yi = [0 1 0.5 0 -1];

%figure;
%plot(xi,yi,'o','LineWidth',2);
%grid on;
n = length(xi);
t= linspace(0, 1, 100);

x_t = ((((((64.*t)-(352/3)).*t)+60).*t)-(14/3)).*t-1;
y_t = ((((((-64/3).*t)+48).*t)-(116/3)).*t+11).*t;

figure;
subplot(121);
plot(t,x_t,'r','LineWidth',2); title('Curva Parametrica x(t)');
xlabel('t'); ylabel('x(t)');

subplot(122);
plot(t,y_t,'b','LineWidth',2); title('Curva Parametrica y(t)');
xlabel('t'); ylabel('y(t)');

figure;
plot(xi, yi,'o','LineWidth',2); 
grid on;
hold on;
plot(x_t, y_t,'r','LineWidth',2);
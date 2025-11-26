close all;
clc;

x=[10 20 30 40 50 60 70 80];
y=[25 70 380 550 610 1220 830 1450];

plot(x,y,'ob','LineWidth',2);
grid on;
n=length(x);

sum_xi=sum(x);
sum_xi2=sum(x.^2);
sum_yi=sum(y);
sum_xiyi=sum(x.*y);
A=[   n   sum_xi
   sum_xi sum_xi2];
d=[sum_yi
   sum_xiyi];
b=A\d;
a0=b(1);
a1=b(2);
x_aprox=10:100;
y_aprox=a0+(a1*x_aprox);
hold on;
plot(x_aprox,y_aprox,'r','LineWidth',2);title('Regresión Lineal');

p = polyfit(x, y, 1);      
y_polyfit = polyval(p, x_aprox);

plot(x_aprox, y_polyfit, '--k', 'LineWidth', 2);

title('Regresión Lineal: Método Manual vs polyfit/polyval');
legend('Datos', 'Manual', 'polyfit', 'Location', 'northwest');
xlabel('x');
ylabel('y');
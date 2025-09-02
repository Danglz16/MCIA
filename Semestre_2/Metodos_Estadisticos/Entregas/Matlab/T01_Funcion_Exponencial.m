clear all;
close all;
clc;

format long

x = 0.5;
nc = 5;
e_x = 0;
n = 6;

Es = (0.5 * 10^(2-nc));

Vv = 1.648721271;
Aprox_ant = 0;

e_x = e_x + ((x^0)/factorial(0));
Aprox_act = e_x;

Ev = abs((Vv-e_x)/Vv)*100;
Ea = abs((Aprox_act-Aprox_ant)/Aprox_act)*100;

for m=1:n-1
    Aprox_ant = Aprox_act;
    e_x = e_x + ((x^m)/factorial(m));
    Aprox_act = e_x;
    Ev_new = abs((Vv-e_x)/Vv)*100;
    Ea_new = abs((Aprox_act-Aprox_ant)/Aprox_act)*100;
    Ev = [Ev,Ev_new];
    Ea = [Ea,Ea_new];
end

plot(Ev,'r','LineWidth',2);
xlabel('Numero de terminos');
ylabel('% error verdadero ');
hold on;
title('Comportamiento del error');
plot(Ea,'b','LineWidth',2);
legend('ev(%)','ea(%)');

grid on;

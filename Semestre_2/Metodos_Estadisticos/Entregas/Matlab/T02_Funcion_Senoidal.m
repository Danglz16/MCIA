clear all;
close all;
clc;

format long
tic
x = pi/6;
nc = 5;
sen_x = 0;

n = 6;

Es = (0.5 * 10^(2-nc));

Vv = 0.5;
Aprox_ant = 0;

sen_x = sen_x + x;
Aprox_act = sen_x;

Ev = abs((Vv-sen_x)/Vv)*100;
Ea = abs((Aprox_act-Aprox_ant)/Aprox_act)*100;

for m=1:n-1
    Aprox_ant = Aprox_act;
    sen_x = sen_x + ((-1)^m)*((x^(2*m+1))/factorial(2*m+1));
    Aprox_act = sen_x;
    Ev_new = abs((Vv-sen_x)/Vv)*100;
    Ea_new = abs((Aprox_act-Aprox_ant)/Aprox_act)*100;
    Ev = [Ev,Ev_new];
    Ea = [Ea,Ea_new];
end

plot(Ev,'r','LineWidth',2);
xlabel('Numero de terminos');
ylabel('% error verdadero');
hold on;
title('Comportamiento del error');
plot(Ea,'b','LineWidth',2);
legend('ev(%)','ea(%)');

grid on;
toc

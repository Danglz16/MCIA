clear;
close all;
clc;

format long
tic

x = pi/3;
nc = 5;
n = 6;

Es = (0.5 * 10^(2-nc))

Vv= 0.5;
Aprox_ant=0;

cos_x=1;
Aprox_act=cos_x;

Ev= abs((Vv-cos_x)/Vv)*100;
Ea= abs((Aprox_act-Aprox_ant)/Aprox_act)*100;

for m=1:n-1
    Aprox_ant=Aprox_act;
    cos_x=cos_x + (((-1)^m)*((x^(2*m))/factorial(2*m)));
    Aprox_act=cos_x;
    Ev_new=abs((Vv-cos_x)/Vv)*100;
    Ea_new=abs((Aprox_act-Aprox_ant)/Aprox_act)*100;
    if Ea_new>100
    Ea_new=Ea_new-(Ea_new-80);
    end
    Ev=[Ev,Ev_new];
    Ea=[Ea,Ea_new];
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


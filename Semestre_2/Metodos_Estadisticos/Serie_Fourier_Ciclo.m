clear all;
close all;
clc;
w0=pi;
T=(2*pi)/w0;
t=-T/2:pi/300:T/2;
cte=4/pi;
term=200;
% Funcion impar por que contiene senos
%Armonico=(1/n)*sin(n*w0*t);
Armonico = 0;
plot(t,Armonico,'b','LineWidth',2);

for n=1:2:term
    Armonico=Armonico +((1/n)*sin(n*w0*t));
    plot(t,Armonico,'b','LineWidth',2);
    axis square;
    grid on;
    pause(0.3);
end
f_t=cte*Armonico;
plot(t,f_t,'b','LineWidth',2);
axis square
grid on;

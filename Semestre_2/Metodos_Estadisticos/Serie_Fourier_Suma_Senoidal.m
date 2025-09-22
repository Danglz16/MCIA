clear all;
close all;
clc;
N=128;
w0= 120*pi;
T= 2*pi/w0;
t=0:T/(N-1):T;
f=sin(w0*t)+0.2*sin(3*w0*t)+0.1*sin(11*w0*t);
plot(t,f,'LineWidth',3);
grid on;

F = fft(f);
Fshift = ffshift(F);
figure;
stem(abs(Fshift), 'MarkerFaceColor','blue');
title('Espectro de Amplitud |F(n)|');
xlabel('n');
ylabel('|F(n)|')
grid on;

w0=2*pi/T;
n=N;

%n=-16:15;
%w=n*w0;
%figure;
%stem (w, abs (F) , 'MarkerFaceColor', 'blue');
%title ('Espectro de Amplitud |F(w)|');
%xlabel('w');
%ylabel ('|F(w)|');
%grid on;
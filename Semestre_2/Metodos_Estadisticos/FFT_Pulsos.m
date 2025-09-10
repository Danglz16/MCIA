clear all;
close all;
clc;

p=1;
T=2;
k = 0:31;
f = (k<8) | (k>23);

plot(k,f,'o', 'LineWidth',2);
grid on;

N = length(k);
F = fft(f)/N;

aux = F;
F(1:16) = aux(17:32);
F(17:32) = aux(1:16);
stem(abs(F),'MarkerFaceColor','blue');
title('Espectro de Amplitud |F(n)|');
xlabel('n');
ylabel('|F(n)|');
grid on;

w0=2*pi/T;
n=-16:15;
w=n*w0;
figure
stem(w,abs(F), "MarkerFaceColor",'blue');
title('Espectro de Amplitud |F(w)|');
xlabel('w');
ylabel('|F(w)|');
grid on;
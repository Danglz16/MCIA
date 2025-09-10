clear all;
close all;
clc;
n=-30:1:30;
prim=(1./(abs(n)*pi));
second=(1-(-1).^n);
Cn=prim.*second;
 
h = stem(n,Cn);
set(h(1),'MarkerFaceColor','blue');
grid on;
title('Espectro de Frecuencia Discreta');
xlabel('n');
ylabel('|Cn|');

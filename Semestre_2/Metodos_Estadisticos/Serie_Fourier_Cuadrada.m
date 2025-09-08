clear all;
close all;
clc;
t=-1:0.01:1;
mul=4/pi;
w0=pi;
n=1;
primer_armonico=(1/n)*sin(n*w0*t);
plot(t,primer_armonico,'r','LineWidth',2);

n=3;
tercer_armonico=(1/n)*sin(n*w0*t);
hold on;
plot(t,tercer_armonico,'g','LineWidth',2);
 
n=5;
quinto_armonico=(1/n)*sin(n*w0*t);
plot(t,quinto_armonico,'c','LineWidth',2);
 
f_t=mul*(primer_armonico + tercer_armonico + quinto_armonico);
 
plot(t, f_t,'b','LineWidth',2);
grid on;

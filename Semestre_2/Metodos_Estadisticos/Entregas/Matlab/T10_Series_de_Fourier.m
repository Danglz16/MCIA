close all;
clc;

mul = 2;
w0 = 1;                 % frecuencia fundamental
t  = -pi:0.01:pi;
t2 = -3*pi:0.01:-pi;
t3 =  pi:0.01:3*pi;

ytotal  = 0;
ytotal2 = 0;
ytotal3 = 0;

N = 50;

for n = 1:N
    y  = ((2/n)*(-1)^(n+1))*sin(n*t);
    y2 = ((2/n)*(-1)^(n+1))*sin(n*t2);
    y3 = ((2/n)*(-1)^(n+1))*sin(n*t3);

    ytotal  = ytotal  + y;
    ytotal2 = ytotal2 + y2;
    ytotal3 = ytotal3 + y3;
end

ytotal(1:3)   = ytotal(4);
ytotal2(1:3)  = ytotal2(4);
ytotal3(1:3)  = ytotal3(4);
ytotal(625:629)  = ytotal(625);
ytotal2(625:629) = ytotal2(625);
ytotal3(625:629) = ytotal3(625);

figure;
plot(t, ytotal,'k', t2, ytotal2,'k', t3, ytotal3,'k','LineWidth',2);
title('Serie de Fourier truncada (N=50)');
xlabel('t');
ylabel('f(t)');
grid on;

% --------- Espectro de amplitud ---------
n  = 1:N;
Bn = (2./n).* (-1).^(n+1);    % coeficientes senoidales
wn = n*w0;                    % frecuencias angulares

figure;
stem(wn, abs(Bn), 'filled');
title('Espectro de amplitud |B_n| vs \omega_n');
xlabel('\omega_n');
ylabel('|B_n|');
grid on;

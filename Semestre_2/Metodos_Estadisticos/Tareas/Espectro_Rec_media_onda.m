clear; close all; clc;

N = 30;                    % número de armónicos a cada lado
n = -N:N;                  % índices de armónicos
Cn = zeros(size(n));       % vector de coeficientes complejos Cn

for kidx = 1:numel(n)
    k = n(kidx);
    if k == 0
        Cn(kidx) = 1/pi;                  % DC
    elseif abs(k) == 1
        Cn(kidx) = -1j*sign(k)/2;         % C_{+1}=-j/2, C_{-1}=+j/2
    elseif mod(abs(k),2) == 0             % armónicos pares
        m = abs(k)/2;
        Cn(kidx) = -2/(pi*(4*m^2 - 1));   % a_{2m}/2
    else
        Cn(kidx) = 0;                     % el resto no aporta
    end
end

% Grafica del espectro de amplitud |Cn|
h = stem(n, abs(Cn), 'filled'); grid on;
title('Espectro de Amplitud |C_n| - Senoidal Rectificada 1/2 Onda');
xlabel('n (índice armónico)');
ylabel('|C_n|');

% Opcional: resaltar DC, fundamental y algunos pares
% hold on;
% [~,i0]  = min(abs(n-0));
% [~,i1p] = min(abs(n-1));
% [~,i1m] = min(abs(n+1));
% set(h, 'MarkerFaceColor', 'b');
% plot(n(i0),  abs(Cn(i0)),  'o', 'MarkerSize',7, 'MarkerFaceColor',[0 0.6 0]);  % DC en verde
% plot(n(i1p), abs(Cn(i1p)), 'o', 'MarkerSize',7, 'MarkerFaceColor',[0.85 0 0]); % +1 en rojo
% plot(n(i1m), abs(Cn(i1m)), 'o', 'MarkerSize',7, 'MarkerFaceColor',[0.85 0 0]); % -1 en rojo
% legend('|C_n|','DC','\pm1','Location','northeast');

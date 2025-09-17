clear all;
close all;
clc;

%%% Procesamiento de una se�al de audio usando MATLAB

%%% Selecci�n del tipo de filtrado
% 1 -> Pasa bajo
% 2 -> Pasa alto
% 3 -> Pasa banda

tipo=1;

%%% Leer la se�al de audio

%[y,fs]=wavread('Yabu_mono');
%[y,fs] = audioread('Yabu_mono.wav');
[y,fs] = audioread('Mas que tu amigo.wav');

% y -> muestras de la se�al
% fs-> frecuencia de muestreo

% Graficar la se�al original
subplot(411)
T=length(y)/fs;
t=linspace(0,T,T*fs);
plot(t,y)
title('SE�AL ORIGINAL')% T�tulo
xlabel('Tiempo (s)')         % Etiqueta del eje X
ylabel('Amplitud (V)')      % Etiqueta del eje Y

% xlim([0 20/])            % L�mite de la se�al

%%% Reproducir la se�al de audio

%%% wavplay(0.1*y,fs)
%%% Nota: la funcion wavplay es obsoleta
%%% y en su lugar se utilizan audioplayer y play

player = audioplayer(0.1*y,fs);
play(player);

%%% FFT de la se�al

subplot(412)

% Llamado a la funci�n que calcula la FFT

fft_signal(y,fs);title('ESPECTRO DE LA SE�AL ORIGINAL');
xlim([0 4e3]);

%%% Filtrado de la se�al

switch tipo
    case 1
        % C�lculo de los coeficientes del filtro (filtro pasa bajas)
        % Este filtrado deja solo la se�al por debajo de 500 Hz        

        titulo='FILTRO PASA BAJAS';

        % Frecuencia normalizada

        fNorm = 1000 / (fs/2);
        [b,a] = butter(10, fNorm, 'low');

    case 2

        %- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        % C�lculo de los coeficientes del filtro (filtro pasa altas)

        % Este filtrado deja solo la se�al por encima de 500 Hz

        titulo='FILTRO PASA ALTAS';

        % Frecuencia normalizada

        fNorm = 1000 / (fs/2);

        [b,a] = butter(10, fNorm, 'high');

    otherwise

        %- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        % C�lculo de los coeficientes del filtro (filtro pasa banda)

        % Este filtrado deja solo la se�al de 2KHz a 3KHz

        % Frecuencias normalizadas

        titulo='FILTRO PASA BANDA';

        Wp = [2e3 3e3]/(fs/2); Ws = [1.5e3 3.5e3]/(fs/2);

        Rp = 3; Rs = 40; % Rizado de la banda de paso y de parada (s)

        [n,Wn] = buttord(Wp,Ws,Rp,Rs);% Orden del filtro y frecuencia de corte �ptima

        [b,a] = butter(n,Wn);      % Coeficientes del filtro       

        %- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

end

% Filtrado de la se�al

y_Low = filtfilt(b, a, y);

% Graficaci�n de la se�al en el tiempo

subplot(413)

plot(t,y_Low)

title('SE�AL FILTRADA')

xlabel('Tiempo (s)')

ylabel('Amplitud (V)')


% Graficaci�n de la se�al en frecuencia

subplot(414)

% Llamado a la funci�n que calcula la FFT

fft_signal(y_Low,fs);title('ESPECTRO DE LA SE�AL FILTRADA')

xlim([0 4e3]);

ylim([0 0.01]);
pause(25);

player = audioplayer(y_Low,fs);
play(player);

clear all;
close all;
clc;

%%% Procesamiento de una señal de audio usando MATLAB
%%% Señal compuesta de 3 frecuencias
%%% Selección del tipo de filtrado
% 1 -> Pasa bajo
% 2 -> Pasa alto
% 3 -> Pasa banda
% 4 -> Supresor de banda (NO INCLUIDO EN ESTE PROGRAMA, HAY QUE IMPLAMENTARLO)

tipo=1;

%%% Crear señal de audio

% Frecuencia fundamental

f0=1e3; % 1KHz

% Amplitud

a=2; % V=4

% Frecuencia de muestreo

fs=44.1e3; % Frecuencia de una señal de audio CD

% Tiempo de duración en segundos

T=2;

% Vector de tiempo

t=linspace(0,T,T*fs);

% Creación de la señal

% Primer señal (tono 1)

s1=1.0*a*sin(2*pi*(1.0*f0)*t);

% Segunda señal (tono 2)

s2=0.75*a*sin(2*pi*(1.5*f0)*t);

% Tercera señal (tono 3)

s3=0.5*a*sin(2*pi*(2*f0)*t);

% Señal compuesta (suma de tres tonos)

y = s1 + s2 + s3;

% Graficar la señal original

subplot(411)
plot(t,y)
title('SEÑAL ORIGINAL')% Título
xlabel('Tiempo (s)')         % Etiqueta del eje X
ylabel('Amplitud (V)')      % Etiqueta del eje Y
xlim([0 20/1000])            % Límite de la señal

%%% Grabar y reproducir la señal de audio

% wavwrite(0.1*y,fs,'audio')

%  wavplay(0.1*y,fs)

%%% FFT de la señal

subplot(412)

% Llamado a la función que calcula la FFT

fft_signal(y,fs);title('ESPECTRO DE LA SEÑAL ORIGINAL');
xlim([0 2500]);


%%% Filtrado de la señal

switch tipo

    case 1

        % Cálculo de los coeficientes del filtro (filtro pasa bajas)
        % Este filtrado deja solo la señal de 1000 Hz
        % Frecuencia normalizada

        titulo='FILTRO PASA BAJAS';
        fNorm = 1200 / (fs/2);
        [b,a] = butter(10, fNorm, 'low');

    case 2

        %- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        % Cálculo de los coeficientes del filtro (filtro pasa bajas)
        % Este filtrado deja solo la señal de 2000 Hz
        % Frecuencia normalizada

        titulo='FILTRO PASA ALTAS';
        fNorm = 1900 / (fs/2);
        [b,a] = butter(10, fNorm, 'high');  

    case 3

        %- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        % Cálculo de los coeficientes del filtro (filtro pasa banda)
        % Este filtrado deja solo la señal de 1500 Hz
        % Frecuencias normalizadas

        titulo='FILTRO PASA BANDA';
        fNorm_1 = 1250 / (fs/2); % 1250  % 1000
        fNorm_2 = 1700 / (fs/2); % 1700  % 2000
        [b_alta,a_alta]   = butter(10, fNorm_1, 'high');
        [b,a] = butter(10, fNorm_2, 'low');
        y_alta=filtfilt(b_alta, a_alta, y);
        y=y_alta;                       

%         Wp = [1490 1510]/(fs/2); Ws = [1410 1560]/(fs/2);
%         Rp = 3; Rs = 40;
%         [n,Wn] = buttord(Wp,Ws,Rp,Rs)
%         [b,a] = butter(n,Wn);
%         y_Low = filtfilt(b,a,y);

        %- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    otherwise
              
end

% Filtrado de la señal

y_Low = filtfilt(b, a, y);

% Graficación de la señal en el tiempo

subplot(413);
plot(t,y_Low);
title('SEÑAL FILTRADA');
xlabel('Tiempo (s)');
ylabel('Amplitud (V)');
xlim([0 20/1000]);

% Graficación de la señal en frecuencia

subplot(414)

% Llamado a la función que calcula la FFT

fft_signal(y_Low,fs);title('ESPECTRO DE LA SEÑAL FILTRADA')
xlim([0 2500])
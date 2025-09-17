clear all;
close all;
clc;

%%% Procesamiento de una señal de audio usando MATLAB
%%% Crear señal de audio
% Frecuencia fundamental
f0=1e3;  % 1kHz

% Amplitud
a=4;  % V=4
% Frec muestreo
fs=44.1e3;

% Tiempo de duración (seg)
T=1.5;

L=round(T*fs);  % Numero de muestras

% Frecuencia normalizada
fn=f0/fs;

% Crear la señal de audio

y=1*a*sin(2*pi*fn*(0:L-1))+0.5*a*sin(4*pi*fn*(0:L-1));

% Graficar la señal
figure,
subplot(411);
plot((0:L-1)/fs,y);
title('Señal original');
xlabel('Tiempo (s)');
ylabel('Amplitud (V)');
xlim([0 10/1000]);     % Limite de la señal en x

subplot(412);
% Llamar a la funcion que calcula la FFT
fft_signal(y,fs);
xlim([0 2500]);

%%% Filtrado de la señal
% Frecuencia normalizada
fNorm= 1200 / (fs/2);

% calculo de los coeficientes del filtro (filtro pasa bajas)
[b,a]=butter(5, fNorm, 'low');

% Filtrado de la señal
y_Low = filtfilt(b,a,y);

% Graficar la señal en el tiempo
subplot(413);
plot((0:L-1)/fs,y_Low);
title('SEÑAL FILTRADA');
xlabel('Tiempo (s)');
ylabel('Amplitud (V)');
xlim([0 10/1000]);

% Grafica de la señal en frecuencia
subplot(414);
% Llamar a la función que caclula la FFT
fft_signal(y_Low,fs);
title('ESPECTRO DE LA SEÑAL FILTRADA');
xlim([0 2500]);
ylim([0 4]);



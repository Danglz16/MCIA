clear all;
close all;
clc;

%%% Procesamiento de una se�al de audio usando MATLAB
%%% Crear se�al de audio
% Frecuencia fundamental
f0=1e3;  % 1kHz

% Amplitud
a=4;  % V=4
% Frec muestreo
fs=44.1e3;

% Tiempo de duraci�n (seg)
T=1.5;

L=round(T*fs);  % Numero de muestras

% Frecuencia normalizada
fn=f0/fs;

% Crear la se�al de audio

y=1*a*sin(2*pi*fn*(0:L-1))+0.5*a*sin(4*pi*fn*(0:L-1));

% Graficar la se�al
figure,
subplot(411);
plot((0:L-1)/fs,y);
title('Señal original');
xlabel('Tiempo (s)');
ylabel('Amplitud (V)');
xlim([0 10/1000]);     % Limite de la se�al en x

subplot(412);
% Llamar a la funcion que calcula la FFT
fft_signal(y,fs);
xlim([0 2500]);

%%% Filtrado de la se�al
% Frecuencia normalizada
fNorm= 1200 / (fs/2);

% calculo de los coeficientes del filtro (filtro pasa bajas)
[b,a]=butter(5, fNorm, 'low');

% Filtrado de la se�al
y_Low = filtfilt(b,a,y);

% Graficar la se�al en el tiempo
subplot(413);
plot((0:L-1)/fs,y_Low);
title('SEÑAL FILTRADA');
xlabel('Tiempo (s)');
ylabel('Amplitud (V)');
xlim([0 10/1000]);

% Grafica de la se�al en frecuencia
subplot(414);
% Llamar a la funci�n que caclula la FFT
fft_signal(y_Low,fs);
title('ESPECTRO DE LA SEÑAL FILTRADA');
xlim([0 2500]);
ylim([0 4]);



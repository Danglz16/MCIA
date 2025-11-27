close all;
clc;

%https://la.mathworks.com/help/signal/ug/filtering-data-with-signal-processing-toolbox.html
% wform = ecg(100);
% plot(wform)
% axis([0 500 -1.25 1.25])
% text(31,-0.4,'Q')
% text(36,1.1,'R')
% text(41,-1,'S')
%x = cos(2*pi*100*t)+0.5*randn(size(t));

%% Procesamiento de una señal de audio usando MATLAB
%% Selección del tipo de filtrado
% 1 -> Pasa bajo
% 2 -> Pasa alto
% 3 -> Pasa banda
% 4 -> Reprime banda
tipo=2;
cont=0;
%% Crear señal de audio
% Frecuencia fundamental
f0=8e3; % 8KHz
% Amplitud
a=3; % V=4
% Frecuencia de muestreo
fs=44.1e3; % Frecuencia de una señal de audio CD
% Tiempo de duración en segundos
T=1.5;
% Vector de tiempo
t=linspace(0,T,T*fs);
% Creación de la señal
% Primer señal (tono 1)
%s1=a*sin(2*pi*f0*t);
s1=cos(2*pi*100*t)+0.5*randn(size(t));
% Segunda señal (tono 2)
s2=0.75*a*sin(2*pi*(1.5*f0)*t);
% Tercera señal (tono 3)
s3=0.5*a*sin(2*pi*(2*f0)*t);
% señal compuesta (suma de dos tonos)
y = s1 + s2 + s3;
% Graficar la señal original
subplot(411)
plot(t,y)
title('señal ORIGINAL')% Titulo
xlabel('Tiempo (s)')         % Etiqueta del eje X
ylabel('Amplitud (V)')      % Etiqueta del eje Y
xlim([0 20/f0])            % Limite de la señal
%% Grabar y reproducir la señal de audio
% wavwrite(0.1*y,fs,'audio')
% wavplay(0.1*y,fs)
%pause(5);
%player=audioplayer(0.1*y,fs);
%play(player)
%% FFT de la señal
subplot(412)
% Llamado a la funcion que calcula la FFT
fft_signal(y,fs);title('ESPECTRO DE LA señal ORIGINAL')
xlim([0 f0*3])
%% Filtrado de la señal
switch tipo
    case 1
        % Calculo de los coeficientes del filtro (filtro pasa bajas)
        % Este filtrado deja solo la señal de 1000 Hz
        % Frecuencia normalizada
        titutlo='FILTRO PASA BAJAS';
        fNorm = 15e3 / (fs/2);
        [b,a] = butter(10, fNorm, 'low');
    case 2
        %- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        % Calculo de los coeficientes del filtro (filtro pasa bajas)
        % Este filtrado deja solo la señal de 2000 Hz
        % Frecuencia normalizada
        titutlo='FILTRO PASA ALTAS';
        fNorm = 15e3 / (fs/2);
        [b,a] = butter(10, fNorm, 'high');
    case 3
        %- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        % Calculo de los coeficientes del filtro (filtro pasa banda)
        % Este filtrado deja solo la señal de 1500 Hz
        % Frecuencias normalizadas
        titutlo='FILTRO PASA BANDA';
        Wp = [11.5e3 12.5e3]/(fs/2); Ws = [11e3 13e3]/(fs/2);
        Rp = 3; Rs = 40;
        [n,Wn] = buttord(Wp,Ws,Rp,Rs)
        [b,a] = butter(n,Wn);       
        %- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    otherwise
        %- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        % Calculo de los coeficientes del filtro (filtro pasa banda)
        % Este filtrado elimina solo la señal de 1500 Hz
        % Frecuencias normalizadas
        fNorm_1 = 11e3 / (fs/2); % 
        fNorm_2 = 13e3 / (fs/2); %
        [b,a] = butter(10, fNorm_1, 'low');
        [b_alta,a_alta]= butter(10, fNorm_2, 'high');
        y_alta=filtfilt(b_alta, a_alta, y);
        y_baja=filtfilt(b, a, y);
        cont=1;     
        %- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
end
% Filtrado de la señal
if (cont==1)
y_Low = y_alta+y_baja;
cont=0;
else
    y_Low = filtfilt(b, a, y);
end
% Graficacion de la señal en el tiempo
subplot(413)
plot(t,y_Low)
title('señal FILTRADA')
xlabel('Tiempo (s)')
ylabel('Amplitud (V)')
xlim([0 20/f0])

% Graficacion de la señal en frecuencia
subplot(414)
% Llamado a la funcion que calcula la FFT
fft_signal(y_Low,fs);title('ESPECTRO DE LA señal FILTRADA')
xlim([0 3*f0])
% InterpSegmentariaCuadraticaNPuntos.m
% Programa que calcula la interpolación
% lineal (spline), y cuadrática 
% de una serie de puntos
%
% Dr. JCPO Copyright 23-02-2022
%
%

clear all:
close all;
clc;

% Entrada de datos
% x=[3.0 4.5 7.0 9.0];
% y=[2.5 1.0 2.5 0.5];


x=[0.9 1.3 1.9 2.1 2.6 3.0 3.9 4.4 4.7 5.0 6.0 7.0 8.0 9.2 10.5 11.3 11.6 12.0 12.6 13.0 13.3];
y=[1.3 1.5 1.85 2.1 2.6 2.7 2.4 2.15 2.05 2.1 2.25 2.3 2.25 1.95 1.4 0.9 0.7 0.6 0.5 0.4 0.25];


n=length(x);

plot(x,y,'go','LineWidth',3);

%axis([x(1) x(n) f_x(n) f_x(1)]);
axis([0 14 -2 8]);
hold on;
%plot(x,f_x,'r','LineWidth',3);

hold on;
m=zeros(length(x));
pause;
for k=1:n-1
    m(k)=(y(k+1)-y(k))/(x(k+1)-x(k));
    x_aux=x(k):0.01:x(k+1);
    f_aux=y(k)+m(k)*(x_aux-x(k));
    plot(x_aux,f_aux,'r','LineWidth',3);
    grid on;
    pause;
end

x=[0.9 1.3 1.9 2.1 2.6 3.0 3.9 4.4 4.7 5.0 6.0 7.0 8.0 9.2 10.5 11.3 11.6 12.0 12.6 13.0 13.3];
y=[1.3 1.5 1.85 2.1 2.6 2.7 2.4 2.15 2.05 2.1 2.25 2.3 2.25 1.95 1.4 0.9 0.7 0.6 0.5 0.4 0.25];


[ax ay]=size(x);    % Tamaño de la matriz
m=ay;   % No. de puntos
n=m-1;  % No. de intervalos
C=3*n;   % No. de coeficientes
Ceros=zeros(C); % Matriz de ceros

fprintf('Número de Puntos, m: %g \n',m);
fprintf('Número de Intervalos, n: %g \n',n);
fprintf('Número de Coeficientes, C: %g \n',C);

% display(x);
% display(y);

% LLENADO DE LA MATRIZ DE CEROS

% PASO 1: Formación de la Matriz A
A=Ceros;

% PASO 2: Condicion IV (2a. Derivada, a1=0)
A(1,1)=1;

% PASO 2: Condición I (Nodos Internos)
s=1;
for v=1:3:C-3
    if s==1
        u=v+1;
        A(u,v)=x(s+1)*x(s+1);
        A(u,v+1)=x(s+1);
        A(u,v+2)=1;
        
        A(u+1,v+3)=A(u,v);
        A(u+1,v+4)=A(u,v+1);
        A(u+1,v+5)=A(u,v+2);
    end
    if s>1
        u=2*s;
        A(u,v)=x(s+1)*x(s+1);
        A(u,v+1)=x(s+1);
        A(u,v+2)=1;
        
        A(u+1,v+3)=A(u,v);
        A(u+1,v+4)=A(u,v+1);
        A(u+1,v+5)=A(u,v+2);
    end
    s=s+1;
end

% PASO 4: Condición II (Extremos)

A(2*s,1)=x(1)*x(1);
A(2*s,2)=x(1);
A(2*s,3)=1;

A(2*s+1,C)=1;
A(2*s+1,C-1)=x(m);
A(2*s+1,C-2)=x(m)*x(m);

% PASO 5: Condición III (1a. Derivada, Continuidad)
t=2*s+2;
w=1;
for v=1:3:C-3
    if w==1
        u=t;
        A(u,v)=2*x(w+1);
        A(u,v+1)=1;
        
        A(u,v+3)=-A(u,v);
        A(u,v+4)=-A(u,v+1);
    end
    if w>1
        u=(2*s+2)+w-1;
        A(u,v)=2*x(w+1);
        A(u,v+1)=1;
        
        A(u,v+3)=-A(u,v);
        A(u,v+4)=-A(u,v+1);
    end
    t=t+1;
    w=w+1;
end

fprintf('\nMatriz A: %g \n');
display(A);


% PASO 6: Formación del vector B

% Condicion IV (2a. Derivada, a1=0)
b(1)=0;

% Condición I (Nodos Internos)
cont=0;
for a=2:m-1
    if cont==0
        b(a)=y(a);
        b(a+1)=b(a);
    end
    if cont>0
        b(a+cont)=y(a);
        b(a+cont+1)=b(a+cont);
    end
    cont=cont+1;
end

% Condición II (Extremos)
b(2*cont+2)=y(1);
b(2*cont+3)=y(4);

% Condición III (1a. Derivada, Continuidad)
for L=2*cont+4:C
    b(L)=0;
end

B=b';
fprintf('\nVector B: %g \n');
display(B);

% PASO 7: Solución. Cálculo de los coeficientes
Coef=inv(A)*B;
fprintf('\nCoeficientes, Ai Bi Ci:\n');
disp(Coef);

% PASO 8: Formación y graficado de los polinomios cuadráticos

title('Interpolación segmentaria cuadrática');
xlabel('x');
ylabel('f(x)');
grid on;
hold on;

% plot(x,y,'r');
% axis([0 14 -1 5]);
d=1;
for t=1:3:C-1
    a=Coef(t+0);
    b=Coef(t+1);
    c=Coef(t+2);
    rango=x(d):0.01:x(d+1);
    [ax ay]=size(rango);
    int=ay;
    clear F;
    for r=1:int
        F(r)=a*rango(r)^2+b*rango(r)+c;
    end
    pause;
    plot(rango,F,'b','LineWidth',2);
    %axis([0 14 -1 5]);
    hold on;
    d=d+1;
end


clear all;
close all;
clc;

x=[0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0,...
    9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3];
f_x=[1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, ...
    2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25];

% x=[1 3 4 5 6];
% f_x=log(x);


m=length(x);
n=length(x);

xres=x(1):0.01:x(n);
xlon=length(xres);
yres=zeros(1,xlon);

for s=1:xlon
    yresNew(s)=Newtint2025_02(x,f_x,xres(s));
    yresLag(s)=Lagrange2025_02(x,f_x,xres(s));
end


figure

plot(x,f_x,'o','LineWidth',3);
hold on;
plot(x,f_x,'r','LineWidth',2);
plot(x,f_x,'k*','LineWidth',4);
plot(x,f_x,'r','LineWidth',2);
%axis([0 14 -2 8]);
grid on;
plot(xres,yresNew,'b','LineWidth',10);
plot(xres,yresLag,'g','LineWidth',2);
%t1=toc

x_des=2;
y_des=Newtint2025_02(x,f_x,x_des);
plot(x_des,y_des,'ro','LineWidth',4);



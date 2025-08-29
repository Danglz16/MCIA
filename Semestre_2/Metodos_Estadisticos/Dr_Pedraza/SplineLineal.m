clear all;
close all;
clc;

% x=[3.0 4.5 7.0 9.0];
% f_x=[2.5 1.0 2.5 0.5];

x=[0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0,...
    9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3];
f_x=[1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, ...
    2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25];


n=length(x);


plot(x,f_x,'bo','LineWidth',3);

axis([0 14 -4 4]);
grid on;
hold on;
pause;
for s=1:n-1
    x_test=x(s):0.01:x(s+1);
    m=(f_x(s+1)-f_x(s))/(x(s+1)-x(s));
    f_test=f_x(s)+m*(x_test-x(s));
    plot(x_test,f_test,'r','LineWidth',3);
    pause;
end
% x_test=x(1):0.01:x(2);
% m0=(f_x(2)-f_x(1))/(x(2)-x(1));
% f_test=f_x(1)+m0*(x_test-x(1));
% 
% hold on;
% plot(x_test,f_test,'r','LineWidth',3);
% 
% x_test=x(2):0.01:x(3);
% m0=(f_x(3)-f_x(2))/(x(3)-x(2));
% f_test=f_x(2)+m0*(x_test-x(2));
% hold on;
% plot(x_test,f_test,'r','LineWidth',3);
% 
% 
% 

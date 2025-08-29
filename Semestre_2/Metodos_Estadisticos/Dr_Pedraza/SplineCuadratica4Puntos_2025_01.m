clear all;
close all;
clc;

x=[3.0 4.5 7.0 9.0];
f_x=[2.5 1.0 2.5 0.5];

plot(x,f_x,'bo','LineWidth',3);
pause;
A=[4.5 1 0 0 0 0 0 0;
   0 0 20.25 4.5 1 0 0 0;
   0 0 49 7 1 0 0 0;
   0 0 0 0 0 49 7 1;
   3 1 0 0 0 0 0 0;
   0 0 0 0 0 81 9 1;
   1 0 -9 -1 0 0 0 0;
   0 0 14 1 0 -14 -1 0];
b=[ 1
    1
    2.5
    2.5
    2.5
    0.5
    0
    0];
sol=inv(A)*b;
a1=0;
b1=sol(1);
c1=sol(2);
a2=sol(3);
b2=sol(4);
c2=sol(5);
a3=sol(6);
b3=sol(7);
c3=sol(8);
sol_new=[a1,sol'];

hold on;
n=length(x);
t=0;
for s=1:n-1
    x_test=x(s):0.01:x(s+1);
    f_test=sol_new(t+1)*x_test.^2+sol_new(t+2)*x_test+sol_new(t+3);
    plot(x_test,f_test,'r','LineWidth',3);
    t=t+3;
    pause;
end





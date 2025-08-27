function yint = Newtint2025_01(x,y,xx)
% Newtint: Newton interpolating polynomial
% yint = Newtint(x,y,xx): Uses an (n ? 1)?order Newton
% interpolating polynomial based on n data points (x, y)
% to determine a value of the dependent variable (yint)
% at a given value of the independent variable, xx.
% input:
% x = independent variable
% y = dependent variable
% xx = value of independent variable at which
% interpolation is calculated
% output:
% yint = interpolated value of dependent variable
% compute the finite divided differences in the form of a
% difference table

% Applied Numerical Methods with MATLAB
% 2017, McGraw-Hill
%

n = length(x);
if length(y)~=n, error('x and y must be same length'); end
b = zeros(n,n);
% assign dependent variables to the first column of b.
b(:,1) = y(:); % the (:) ensures that y is a column vector.
for jj = 2:n
    for ii = 1:n-jj+1
        b(ii,jj) = (b(ii+1,jj-1)-b(ii,jj-1))/(x(ii+jj-1)-x(ii));
    end
end

% use the finite divided differences to interpolate
xt = 1;
yint = b(1,1);

for jj = 1:n-1
    xt = xt*(xx-x(jj));
    yint = yint+b(1,jj+1)*xt;
end
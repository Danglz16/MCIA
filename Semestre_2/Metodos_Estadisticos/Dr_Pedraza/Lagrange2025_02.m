function yint = Lagrange2025_01(x,y,xx)
% Lagrange: Lagrange interpolating polynomial
% yint = Lagrange(x,y,xx): Uses an (n ? 1) ?order
% Lagrange interpolating polynomial based on n data points
% to determine a value of the dependent variable (yint) at
% a given value of the independent variable, xx.
% input:
% x = independent variable
% y = dependent variable
% xx = value of independent variable at which the
% interpolation is calculated
% output:
% yint = interpolated value of dependent variable
%
% Applied Numerical Methods with MATLAB
% 2017, McGraw-Hill
%


n = length(x);
if length(y) ~= n, error('x and y must be same length'); end
s = 0;
for ii = 1:n
    product = y(ii);
    for jj = 1:n
        if ii ~= jj
            product = product*(xx - x(jj))/(x(ii) - x(jj));
        end
    end
    s = s + product;
end
yint = s;
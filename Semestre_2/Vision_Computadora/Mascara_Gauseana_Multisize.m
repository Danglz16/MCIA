clear;
close all;
clc;

gauss33 = [1 2 1
           2 4 2
           1 2 1];

div = sum(sum(gauss33));
gauss33 = gauss33/div;

figure, 
subplot(121), imagesc(gauss33);
subplot(122), surf(gauss33)

gauss55 = conv2(gauss33,gauss33);
div = sum(sum(gauss55));
gauss55 = gauss55/div;
figure,
subplot(121), imagesc(gauss55);
subplot(122), surf(gauss55)

gauss99 = conv2(gauss55,gauss55);
div = sum(sum(gauss99));
gauss99 = gauss99/div;
figure,
subplot(121), imagesc(gauss99);
subplot(122), surf(gauss99)

gauss1717 = conv2(gauss99,gauss99);
div = sum(sum(gauss1717));
gauss1717 = gauss1717/div;
figure,
subplot(121), imagesc(gauss1717);
subplot(122), surf(gauss1717)
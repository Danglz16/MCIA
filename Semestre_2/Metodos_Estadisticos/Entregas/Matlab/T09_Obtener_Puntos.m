img = imread('../Datos/Mano.jpg');
imshow(img);
hold on;
h = impoly;
pos = getPosition(h);
x = pos(:,1);
y = pos(:,2);

%M = [x y];
%csvwrite('puntos_mano.csv', M);

save('puntos_mano.mat','x','y');
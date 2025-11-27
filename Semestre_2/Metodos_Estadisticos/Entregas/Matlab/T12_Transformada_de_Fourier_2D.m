close all;
clc;

%Imagen 1
ImagenA=imread('../Datos/flor.jpeg');
imagenA=rgb2gray(ImagenA);
imagenA=im2double(imagenA);

%Imagen 2
ImagenB=imread('../Datos/terry.png');
imagenB=rgb2gray(ImagenB);
imagenB=im2double(imagenB);

%Display images
figure, imshow(imagenA);
title('Image A - Flor');
figure, imshow(imagenB);
title('Image B - Perro');

%Perform 2D FFTs
fftA = fft2(double(imagenA));
fftB = fft2(double(imagenB));

%Display magnitude and phase of 2D FFTs
figure, 
%imshow(abs(fftshift(fftA)),[24 100000]), colormap gray
imagesc(100*log(1+abs(fftshift(fftA)))); colormap(gray)
title('Image A FFT2 Magnitude')

figure,
surfl(abs(fftshift(fftA)));
shading interp; colormap(bone)
title('Image A FFT2 Magnitude 3D')

figure, imshow(angle(fftshift(fftA)),[-pi pi]), colormap gray
title('Image A FFT2 Phase')

figure,
surfl(angle(fftshift(fftA)));
shading interp; colormap(bone)
title('Image A FFT2 Phase 3D')

figure, 
%imshow(abs(fftshift(fftB)),[24 100000]), colormap gray
imagesc(100*log(1+abs(fftshift(fftA)))); colormap(gray)
title('Image B FFT2 Magnitude')
figure, imshow(angle(fftshift(fftB)),[-pi pi]), colormap gray
title('Image B FFT2 Phase')


%Switch magnitude and phase of 2D FFTs

fftC = abs(fftA).*exp(1i*angle(fftB));
fftD = abs(fftB).*exp(1i*angle(fftA));

%Perform inverse 2D FFTs on switched images
imageC = ifft2(fftC);
imageD = ifft2(fftD);

%Calculate limits for plotting

cmin = min(min(abs(imageC)));
cmax = max(max(abs(imageC)));

dmin = min(min(abs(imageD)));
dmax = max(max(abs(imageD)));


%Display switched images
figure, imshow(abs(imageC), [cmin cmax]), colormap gray
title('Image C  Magnitude')
figure, imshow(abs(imageD), [dmin dmax]), colormap gray
title('Image D  Magnitude')

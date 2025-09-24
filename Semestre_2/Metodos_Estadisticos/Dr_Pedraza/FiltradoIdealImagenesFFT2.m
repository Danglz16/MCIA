clear;
close all;
clc;

[file1,path1] = uigetfile(...
{'*.jpg;*.jpeg;*.bmp;*.tiff;*.png;*.gif'}, ...
   'Select a File');

examina1=strcat(path1,file1);

A=imread(examina1);
imageA=im2double(A);
if length(size(A)) == 3
    imageA=rgb2gray(imageA);
end

%Display image
figure, imagesc(imageA);colormap(gray);
title('imageA');

%Perform 2D FFTs
fftA = fft2(imageA);


%Display magnitude and phase of 2D FFTs

fftA_Abs=abs(fftshift(fftA));
fftA_Angle=angle(fftshift(fftA));

% figure,imshow(fftA_Abs);
% figure,imshow(fftA_Angle);
figure,
%imagesc(fftA_Abs);colormap(gray);
imagesc(100*log(1+fftA_Abs)); colormap(gray);
title('Image A FFT2 Magnitude');
figure,
surfl(fftA_Abs);
shading interp; colormap(bone);

figure,imagesc(fftA_Angle);colormap(gray);
figure,
surfl(fftA_Angle);
shading interp; colormap(bone);

mask_lp=zeros(size(imageA));
mask_hp=zeros(size(imageA));
mask_bp=zeros(size(imageA));
mask_sp=zeros(size(imageA));

[ax,ay]=size(imageA);
cx=round(ax/2);
cy=round(ay/2);

% Tamaño del filtro
tam=20;

mask_lp(cx-tam:cx+tam,cy-tam:cy+tam)=1;

mask_hp=1-mask_lp;

figure,
imagesc(mask_lp);colormap(gray);

lim_sup=21;
lim_inf=11;
mask_bp(cx-lim_sup:cx+lim_sup, cy-lim_sup:cy+lim_sup)=1;
mask_bp(cx-lim_inf:cx+lim_inf, cy-lim_inf:cy+lim_inf)=0;
 
mask_sp=1-mask_bp;

figure, 
subplot(221);imagesc(mask_lp);colormap(gray);
subplot(222);imagesc(mask_hp);colormap(gray);
subplot(223);imagesc(mask_bp);colormap(gray);
subplot(224);imagesc(mask_sp);colormap(gray);

fftA_Abs_Mask=fftA_Abs.*mask_sp;
fftA_Angle_Mask=fftA_Angle.*mask_sp;

figure,
imagesc(100*log(1+fftA_Abs_Mask)); colormap(gray);
title('Image A FFT2 Magnitude Filtered');
figure,
surfl(fftA_Abs_Mask);
shading interp; colormap(bone);

figure, imshow(fftA_Angle_Mask,[-pi pi]), colormap gray
title('Image A FFT2 Phase Filtered')
figure,
surfl(fftA_Angle_Mask);
shading interp; colormap(gray);

fftA_Abs_Mask_Inv=ifftshift(fftA_Abs_Mask);
fftA_Angle_Mask_Inv=ifftshift(fftA_Angle_Mask);

fftA_Back=fftA_Abs_Mask_Inv.*exp(i*fftA_Angle_Mask_Inv);

imageA_Back=ifft2(fftA_Back);

cmin=min(min(abs(fftA_Back)));
cmax=max(max(abs(fftA_Back)));

figure,
imagesc(abs(imageA_Back));colormap(gray);




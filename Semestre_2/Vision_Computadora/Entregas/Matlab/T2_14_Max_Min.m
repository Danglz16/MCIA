clear;
close all;
clc;

[file,path] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen A'); 
ruta=strcat(path,file);
A=imread(ruta);
A= im2double(A);

[file2,path2] = uigetfile({'*.jpg';'*.png';'*.jpeg';'*.bmp';'*.gif'},'File Selector - Imagen B');
ruta2=strcat(path2,file2);
B=imread(ruta2);
B= im2double(B);

[bx by bz] = size(B);
A=imresize(A,[bx by]);

%MAX
for m=1:bx
    for n=1:by
        for p=1:bz
            if A(m,n,p) >= B(m,n,p)
                Rmax(m,n,p) = A(m,n,p);
            else
                Rmax(m,n,p) = B(m,n,p);
            end
        end
    end
end


%MIN
Rmin=zeros(size(A));
for m=1:bx
    for n=1:by
        for p=1:bz
            if A(m,n,p) <= B(m,n,p)
                Rmin(m,n,p) = A(m,n,p);
            else
                Rmin(m,n,p) = B(m,n,p);
            end
        end
    end
end

figure;
subplot(221); imshow(A);title('A');
subplot(223); imshow(B);title('B');
subplot(222); imshow(Rmin);title('Min(A,B)');
subplot(224); imshow(Rmax);title('Max(A,B)');
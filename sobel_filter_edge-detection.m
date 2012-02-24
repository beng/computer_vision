% Ben Gelb
% Intro to CV
% Edge Detection

% clear everything from workplace
clear
clc

% read in image
im = imread('raingirl.jpg');

% convert to double[0,1]
imd = double(im)./255;

% convert to grayscale
img = rgb2gray(im);
% figure,imshow(img);

% ---------- SOBEL FILTER ----------
% Sobel method finds edges using the Sobel approximation to the derivative.
% It returns edges at those points where the gradient of I is maximum.

% calculate sobel filter matrix
sobelfilter = fspecial('sobel');

% % doing some tests
% a=conv2(img,sobelfilter/2);
% figure,imshow(abs(a),[]);
% figure,imshow(a,[]);
% figure,imshow(a);

% find vertical and horizontal edges
% imh = imfilter(imd, sobelfilter./2);
% imv = imfilter(imd, transpose(sobelfilter)/.2);
imh = imfilter(img, sobelfilter./2);
imv = imfilter(img, transpose(sobelfilter)./2);
imvh = abs(imh + imv);
min(imh(:))
max(imh(:))
min(imvh(:))
max(imvh(:))

figure, imshow(imh), title('IM Horizontal 50% Decrease');
figure, imshow(imv), title('IM Vertical 50% Decrease');
figure, imshow(imvh), title('SUM OF H AND V');


% ---------- EDGE FUNCTION ----------
% Laplacian of Gaussian method finds edges by looking for zero crossings 
% after filtering I with a Laplacian of Gaussian filter.

% [BW,thresh] = edge(img, 'log');     % returns threshold value
imlog = edge(img, 'log', [], 4.7 );
figure, imshow(imlog), title('LoG Sigma = 4.7');


% Canny method finds edges by looking for local maxima of the gradient of I.
% The gradient is calculated using the derivative of a Gaussian filter. 

% [a,b] = edge(img, 'canny');
imcanny = edge(img, 'canny', [], 5);
imcanny2 = edge(img, 'canny', [], 7);
figure, imshow(imcanny), title('Canny Sigma = 5');
figure, imshow(imcanny2), title('Canny Sigma = 7');

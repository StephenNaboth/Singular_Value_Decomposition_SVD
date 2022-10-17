
A = imread('./SVD/images/landscape.jpg');
X = double(rgb2gray(A));
nx = size(X,1);
ny = size(X,2);

% calulate SVD 
[U, S, V] = svd(X,'econ');
%
figure, subplot(3,3,1);
imagesc(X), axis off
title("Original")

plotind = 2;
for r = [5,10, 20, 30, 40, 60, 70, 90];
    %approximation of X 
    X_app = U(:, 1:r)*S(1:r,1:r)*V(:,1:r)';
    subplot(3,3,plotind), plotind = plotind + 1;
    imagesc(X_app), axis off
    % storage percentage is calculated here
    title(['r=',num2str(r,'%d'),', ',num2str(100*r*(nx+ny)/(nx*ny),'%2.2f'),'% storage']);
end

%%
figure, subplot(1,2,1)
semilogy(diag(S),'k','LineWidth',1.2), grid on
xlabel('r')
ylabel('Singular value, \sigma_r')
%xlim([700 3000]); ylim([700 3000])
subplot(1,2,2)
semilogy(cumsum(diag(S))/sum(diag(S)),'k','LineWidth',1.2), grid on
xlabel('r')
ylabel('Cumulative Energy')
%xlim([-50 1550]); ylim([0 1.1])

%% From the graph on the right for 90% accuracy we have k around 1200
% now test
figure, subplot(1,2,1)
imagesc(X), axis off
title("Original");

%approximation of X at r = 1200
r = 1200;
X_app_1200 = U(:, 1:r)*S(1:r,1:r)*V(:,1:r)';
subplot(1,2,2), plotind = plotind + 1;
imagesc(X_app_1200), axis off
title(['r=',num2str(r,'%d'),', ',num2str(100*r*(nx+ny)/(nx*ny),'%2.2f'),'% storage']);

%% Correlation Matrices
XXt = X*X';
XtX = X'*X;
figure, subplot(1,2,1);
imagesc(XXt), axis off

subplot(1,2,2);
imagesc(XtX), axis off


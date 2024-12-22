clear all
path="C:\Users\X1\Documents\studies\experiments\noise\noise\Vout_vs_f2andVdc.xlsx";
data=readtable(path);
%R=rmmissing(data{:,1});
%f1=rmmissing(data{:,1});
%f2=rmmissing(data{:,2});
%%%%first figure-constant delta f
R=1e4;
f_2=data{1,1};
gain=6e4;
vdc=[61,100.4,152,200.2,246.4];
vout=([10.4,13.3,17.6,19.1,15.5].*10)./(1000*(gain^2));
%vout=cell2table(data{3:7,2});
idc=vdc./(R*1000);
i_rmssq=vout./(R^2);
x=linspace(1e-6,1e-4,10000);
func=@(a,i) a(1).*i+a(2);
x0=[9.4079e-18,2.7867e-22];
fit=fminsearch(@(a) norm(func(a,idc)-i_rmssq),x0)
y_fit=func(fit,x);
loglog(idc,i_rmssq,'O')
hold on
loglog(x,y_fit)
ylim([1e-23,1e-20])
%%%%%%%%second figure- constant I
% R=1e4;
% f_2=data{13:18,1};
% vdc=data{11,1};
% vout=data{13:18,2};
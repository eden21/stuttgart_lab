clear all
path="C:\Users\X1\Documents\studies\experiments\noise\noise\Vout_vs_f2andVdc.xlsx";
data=readtable(path);
R=1e4;
f_2=[330,1000,3300,1e4,3.3e4,1e5];
gain=6e4;
vdc=201.2/1000;
vout=([2.1,2.5,3.3,5.2,9.8,19].*10)./(1000*((R*gain)^2));
%v_afgain=(vout./gain).^2;
x=linspace(1e0,1e6,10000);
func=@(a,f) a(1).*i+a(2);
x0=[0,0];
fit=fminsearch(@(a) norm(func(a,f_2)-v_afgain),x0)
y_fit=func(fit,x);
loglog(f_2,v_afgain,'O')
hold on
loglog(x,y_fit)
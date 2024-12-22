clear all
path="C:\Users\X1\Documents\studies\experiments\noise\noise\V_out_vs_deltaf.xlsx";
data=readtable(path);
%R=rmmissing(data{:,1});
f1=rmmissing(data{:,1});
f2=rmmissing(data{:,2});
deltaf=f2-f1;
gain=600000;
v_n_sq=7.2222e-12;
v_out=([10.9,32.5,93.8,310,944].*10)./(1000*(gain^2));
v_j=v_out-v_n_sq;
%v_out=([10.9,32.5,93.8,310,944]./1000./gain).^2.*1e15;
func=@(a,df) a(1).*df.^(a(2))%a(1).*df+a(2);
x0=[0,2];
fit=fminsearch(@(a) norm(func(a,deltaf)-v_j),x0)
x=linspace(0,1e6,10000);
y_fit=func(fit,x);
plot(deltaf,v_out,'O')
hold on
plot(x,y_fit)
xlim([0,1e6])
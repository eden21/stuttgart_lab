clear all
path="C:\Users\X1\Documents\studies\experiments\noise\noise\Vout_vs_R.xlsx";
data=readtable(path);
R=rmmissing(data{:,1});
gain=600000;
v_out=(rmmissing(data{:,3}).*10)./(1000*(gain^2))
f1=10;
f2=1e5;
v_n=v_out(1)
y=(v_out-v_n)./(f2-f1);
func=@(a,R) a(1).*R+a(2)
x0=[1.2e-21,1.87e-18];
fit=fminsearch(@(a) norm(func(a,R)-v_out),x0)
y_fit=func(fit,R);
loglog(R,y,'O')
hold on
plot(R,y_fit)
xlim([1e-1,1e5])
ylim([1e-18,1e-15])
%v_error=
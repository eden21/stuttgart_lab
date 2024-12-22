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
x0=[1.89e-20,9.1146e-20];
fit=fminsearch(@(a) norm(func(a,R)-v_out),x0)
x=linspace(1,1e5,1000);
y_fit=func(fit,x);
fig=figure;
loglog(R,y,'O')
hold on
plot(x,y_fit)
xlim([1e-1,1e5])
ylim([-1,1e-15])
grid()
xlabel('Resistance R [\Omega]')
ylabel('Squared Average Voltage per Hertz U^2 in [V^2/Hz]')
legend('Data','fit',Location='northwest')
savefig('C:\Users\X1\Documents\MATLAB\lab\noise\voltage_vs_R.fig')
saveas(fig,'C:\Users\X1\Documents\MATLAB\lab\noise\voltage_vs_R.eps')
%v_error=
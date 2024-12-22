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
func=@(a,f) a(1).*f+a(2);
x0=[4.619e-24,8.0331e-20];
fit=fminsearch(@(a) norm(func(a,f_2)-vout),x0)
y_fit=func(fit,x);
fig=figure;
loglog(f_2,vout,'O')
hold on
loglog(x,y_fit)
grid()
xlabel('frequency f_2 [Hz]')
ylabel('Squared Average Voltage U^2 [V^2]')
legend('Data','fit',Location='northwest')
savefig('C:\Users\X1\Documents\MATLAB\lab\noise\voltage_vs_f2_shot_noise.fig')
saveas(fig,'C:\Users\X1\Documents\MATLAB\lab\noise\voltage_vs_f2_shot_noise.eps')
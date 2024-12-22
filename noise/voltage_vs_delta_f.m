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
func=@(a,df) a(1).*df+a(2);
x0=[2.6194e-16,1.4852e-14];
fit=fminsearch(@(a) norm(func(a,deltaf)-v_j),x0)
x=linspace(0,1e6,10000);
y_fit=func(fit,x);
fig=figure;
loglog(deltaf,v_out,'O')
hold on
plot(x,y_fit)
xlim([0,1e6])
grid()
xlabel('Bandwidth \Deltaf [Hz]')
ylabel('Squared Average Voltage U^2 [V^2]')
legend('Data','fit',Location='northwest')
savefig('C:\Users\X1\Documents\MATLAB\lab\noise\voltage_vs_deltaf.fig')
saveas(fig,'C:\Users\X1\Documents\MATLAB\lab\noise\voltage_vs_deltaf.eps')
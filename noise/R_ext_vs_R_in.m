clear all

R=[10,1e4,1e5];
f1=ones(1,4).*10;
f2=[1e3,3.3e3,1e4,3.3e4];
V_ext_data=[3,5.4,12.3,33.6;
            5.6,13.9,37.6,114.5;
            26.7,83,205.1,380];
V_in_data=[2.9,5,11.1,32.2;
           5.2,12.8,34.9,111.5;
           26,84,246,776];
gain=600000;
data=((V_in_data-V_ext_data).*10)./(1000*(gain^2));
deltaf=f2-f1;
fig=figure;
plot(deltaf,data,'.-')
xlabel('Bandwidth \Deltaf [Hz]')
ylabel('Squared Average difference \DeltaU^2[V^2]')
legend('R=10\Omega','R=10k\Omega','R=100k\Omega',Location='northwest')
grid()
savefig('C:\Users\X1\Documents\MATLAB\lab\noise\R_ext_deltaf.fig')
saveas(fig,'C:\Users\X1\Documents\MATLAB\lab\noise\R_ext_deltaf.png')




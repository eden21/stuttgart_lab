clear all
path="C:\Users\X1\Documents\studies\experiments\noise\noise\V_out_vs_deltaf.xlsx";
data=readtable(path)
%R=rmmissing(data{:,1});
f1=rmmissing(data{:,1});
f2=rmmissing(data{:,2});
deltaf=log10(f2-f1);
gain=600000;
v_out=log10(([10.9,32.5,93.8,310,944]./1000./gain).^2);
func=@(a,df) log10(a)+log10(df);
x0=-17;
fit=fminsearch(@(a) norm(func(a,deltaf)-v_out),x0)
y_fit=func(fit,deltaf);
plot(deltaf,v_out,'O')
hold on
plot(deltaf,y_fit)
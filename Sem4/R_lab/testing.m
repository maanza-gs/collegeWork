syms n x;
 f=piecewise(-pi < x < 0, 1 + x/pi, 0 < x < pi, 1 - x/pi);
 L=pi;
 
 a0=1/L*(int(f,x,-pi,0)+int(f,0,pi));
 an=1/L*(int(f*cos(n*pi*x/L),-pi,0)+int(f*cos(n*pi*x/L),0,pi));
 bn=1/L*(int(f*sin(n*pi*x/L),-pi,0)+int(f*sin(n*pi*x/L),0,pi));
 
 exp = [a0/2,(subs(an*cos(n*pi*x/L)+bn*sin(n*pi*x/L),n,[1 2 3 4]))];
 
 fplot(sum(exp(1,1)),[0 2*L])
 hold on
 fplot(sum(exp(1,1:2)),[0 2*L])
 fplot(sum(exp(1,1:3)),[0 2*L])
 fplot(sum(exp(1,1:4)),[0 2*L])
 fplot(sum(exp(1,1:5)),[0 2*L]) %Fourier Plot
 fplot(f,[0 2*L]) %Function Plot
 hold off
 legend('1','2','3','4','5','realboi')
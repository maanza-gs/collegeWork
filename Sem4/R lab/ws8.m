syms x n;
f=piecewise(0 < x < pi/2, x, pi/2 < x < pi, pi - x);
L=pi;
a0=2/L*(int(f,x,0,pi/2)+int(f,pi/2,pi));
an=2/L*(int(f*cos(n*pi*x/L),0,pi/2)+int(f*cos(n*pi*x/L),pi/2,pi));
bn=2/L*(int(f*sin(n*pi*x/L),0,pi/2)+int(f*sin(n*pi*x/L),pi/2,pi));
halfCos = [a0/2,(subs(an*cos(n*pi*x/L),n,[1 2 3 4]))];  %cosine half-range
halfSin = [0,(subs(bn*sin(n*pi*x/L),n,[1,2,3,4]))];  %sine hlaf-range
fplot(sum(halfCos(1,1)),[0 L]) %HalfCos Plot
hold on
fplot(sum(halfCos(1,1:2)),[0 L])
fplot(sum(halfCos(1,1:3)),[0 L])
fplot(sum(halfCos(1,1:4)),[0 L])
fplot(sum(halfCos(1,1:5)),[0 L])
fplot(f,[0 L])

figure()
fplot(sum(halfSin(1,1)),[0 L]) %HalfSin Plot
hold on
fplot(sum(halfSin(1,1:2)),[0 L])
fplot(sum(halfSin(1,1:3)),[0 L])
fplot(sum(halfSin(1,1:4)),[0 L])
fplot(sum(halfSin(1,1:5)),[0 L])
fplot(f,[0 L])
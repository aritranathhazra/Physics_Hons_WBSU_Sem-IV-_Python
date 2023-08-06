def f(x,y):
    return (1+x)*y+1-3*x+x*x
x,y,h=0.0,0.0,0.05
for i in range(1000):
    k1=h*f(x,y)
    k2=h*f(x+h,y+k1)
    y=y+0.5*(k1+k2)
    x=x+h
print(x,y)
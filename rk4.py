def f(x,y):
    return (1+x)*y+1-3*x+x*x
x,y,h=0,0,0.05
for i in range(100):
    k1=h*f(x,y)
    k2=h*f(x+0.5*h,y+0.5*k1)
    k3=h*f(x+0.5*h,y+0.5*k2)
    k4=h*f(x+h,y+k3)
    y=y+(k1+2*k2+2*k3+k4)/6
    x=x+h
print(x,y)
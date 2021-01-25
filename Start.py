from scipy.integrate import quad,dblquad
from numpy import exp,inf
from sympy import *
'''Discrete'''
def ExpectedValue_Disc(nums, xs):
    res,i = 0,0
    for x in range(xs,len(nums)):
        res += x * nums[i];i+=1
    res = round(res,4)
    print("Expected Value = " + str(res))
    return res
def Variance_Disc(nums,xs):
    var, i = 0, 0
    for x in range(xs, len(nums)):
        var += x * x * nums[i];
        i += 1
    EX2 = round(ExpectedValue_Disc(nums, xs) **2,4)
    res = round(var - EX2,4)
    print("Variance = E(x**2) - (E(x))**2 = " +str(var)+" - " +str(EX2) +" = "+ str(res))
    return res
def ExpectedValue_randomVariable_Disc(nums, xs,rVar):
    res,i = 0,0
    for x in range(xs,len(nums)):
        res += eval(rVar) * nums[i];i+=1
    res = round(res,4)
    print("E("+rVar+") = " + str(res))
    return res
def Variance_randomVariable_Disc(nums,xs,rVar):
    var, i = 0, 0
    for x in range(xs, len(nums)):
        var += eval(rVar) * eval(rVar)* nums[i];
        i += 1
    res = round(var - ExpectedValue_randomVariable_Disc(nums, xs,rVar) ** 2, 4)
    print("var("+ rVar + ") = " + str(res))
    return res

nums = [0.4,0.38,0.15,0.07]
ExpectedValue_Disc(nums,0)
Variance_Disc(nums,0)
ExpectedValue_randomVariable_Disc(nums,0,"(2*x-1)**2")
Variance_randomVariable_Disc(nums,0,"2*x-1")

#In python, never write ^, only power is **
#note in Discrete convert numbers from y to x, so it works with my program


'''Continuous'''
def ExpectedValue_Cts(body, xs, xf):
    f = lambda x : x*eval(body)
    res = round(quad(f,xs,xf)[0],4)
    print("Expected Value = " + str(res))
    return res

def Variance_Cts(body,xs,xf):
    f = lambda x: (x**2)*eval(body)
    EX2 = round(ExpectedValue_Cts(body, xs, xf)**2,4)
    var = round(quad(f,xs,xf)[0],4)
    res = round( var - EX2 ,4)
    print("Variance = E(x**2) - (E(x))**2 = " +str(var)+" - " +str(EX2) +" = "+ str(res))
    return res

def ExpectedValue_randomVariable_Cts(body,xs,xf,rVar):
    f = lambda x: eval(rVar) * eval(body)
    res = round(quad(f, xs, xf)[0], 4)
    print("E("+rVar+") = " + str(res))
    return res

def Variance_randomVariable_Cts(body,xs,xf,rVar):
    f = lambda x: (eval(rVar) ** 2) * eval(body)
    res = round(quad(f, xs, xf)[0], 4) - ExpectedValue_randomVariable_Cts(body, xs, xf,rVar) ** 2
    print("var("+ rVar + ") = " + str(res))
    return res

xs = 0
xf = inf
x = 1
rVar = "-2*x+1"
ExpectedValue_Cts("exp(-x)",xs,xf)
Variance_Cts("exp(-x)",xs,xf)
#ExpectedValue_randomVariable_Cts("exp(-x)",xs,xf,"exp(x/2)") --Can't integrate using scipy so calc by hand
ExpectedValue_randomVariable_Cts("exp(-x)",xs,xf,rVar)
Variance_randomVariable_Cts("exp(-x)",xs,xf,rVar)

def ExpectedValue_Cts_XY(body,xs,xf,ys,yf):
    f = lambda x,y: x * y *  eval(body)
    res = round(dblquad(f, xs, xf,ys,yf)[0], 4)
    print("E(XY) = " + str(res))
    return res

x, y = symbols('x y')
def Covariance (body,xs,xf,ys,yf):
    print("="*20+"Covariance"+"="*20)
    EXY = ExpectedValue_Cts_XY(body,xs,xf,ys,yf)

    F1x = str(integrate(eval(body), (y,ys,yf)))
    print("F1x: "+F1x)
    EX = ExpectedValue_Cts(F1x,xs,xf)
    print("EX = " + str(EX))

    F1y = str(integrate(eval(body), (x,xs,xf)))
    print("F1y: " + F1y)
    EY = ExpectedValue_Cts(F1y.replace('y','x'),ys,yf)
    print("EY = " + str(EY))

    cov = round(EXY - EX * EY, 4)
    print("Covariance = "+ str(cov))
    print()
    varx = Variance_Cts(F1x,xs,xf)
    vary = Variance_Cts(F1y.replace('y','x'),ys,yf)
    corr = round(cov / sqrt(varx*vary),4)
    print("Correlation = "+str(corr))
    return cov,corr
    print()

    print((F1y))



ExpectedValue_Cts_XY("x+y",0,1,0,1)
Covariance("x+y",0,1,0,1)

print()

ExpectedValue_randomVariable_Cts("2*(1-x)", 0 , 1 ,"(2*x)*(-3*x+5)")

Variance_randomVariable_Cts("2*(1-x)", 0 , 1 ,"(2*x)")
Variance_randomVariable_Cts("2*(1-x)", 0 , 1 ,"(-3*x+5)")


from math import *
from scipy.special import comb

def binomial(n_,p_,x_):
    return comb(n_,x_) *  ( p_**x_ )* (1-p_)**(n_-x_)
def binomial_range(n_,p_,a_,b_):
    res = 0
    for x_ in range(a_,b_+1):
        res+=binomial(n_,p_,x_)
        print(binomial(n_,p_,x_))
    return res
#doesn't include x --> P(Y>=2) = 1 - P(Y<2)
def binomial_one_minus(n_, p_, x_):
    return 1-binomial_range(n_,p_,0,x_-1)
def bionmial_mu_var(n_, p_):
    print("Mean = " + str(n_*p_))
    print("Var  = " + str(n_*p_*(1-p_)))


print(binomial_one_minus(12,0.7,1))
print(bionmial_mu_var(12,0.7))
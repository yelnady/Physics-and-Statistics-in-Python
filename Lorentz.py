from math import *
import numpy as np
m_e  = 9.11e-31
m_p = 1.67e-27
q_p = 1.60217e-19
q_e = -1 * q_p
'''What's the speed of electron'''

def speed (volt,mass): #mass here if it's proton or electron
    return sqrt(2*q_p*volt/mass)

#+x --> east, +y --> top, +z --> north

def force (v_,B_,electron):
    return (q_e if electron else q_p) * np.cross(v_,B_)
def coss(x):
    return cos(radians(x))
def sinn(x):
    return sin(radians(x))

v = [0,9.37e+07,0]
theta = 60      #I put the sign in (B)
B = [0,  53000e-9*coss(theta),53000e-9*-sinn(theta)]    #B0 [y cos(theta) - z sin(theta) ]
volts = 18e3

print("{:e}".format( speed (volts , m_e)))
print(force (v,B,True))

#--------------------------------------------------------------------------------------------------------------------------------------
c = 3e8
def gamma (speed):
    return 1/sqrt(1-(speed/c)**2)

def gamma(volt,electron): #I'm using proton as a q (speed so mag)
    return ((q_p*volt)/((m_e if electron else m_p) * c**2) ) +1

def v_over_c (gamma_):
    return sqrt(1-1/(gamma_)**2)

def check_relativistica(MeV): #enter number with as 25e6, if you've KE just enter it
     res = (MeV/ 0.511e6)*100

#this function calculates the speed non relativistically and checks if it's OK or should use another one
def speed_non(volt,electron):
    res = sqrt(2 * q_p * volt / (m_e if electron else m_p))
    print("The speed is "+"{:e}".format( res )+ " and (v/c)% is "+ str(round((res/c)*100,4)))
    return res

def speed_relativistic(volt,electron):
    gamma_ = gamma(volt,electron)
    print("gamma = " + str(gamma_))
    vc = v_over_c(gamma_)
    print("v/c = "+"{:e}".format( vc))
    res = vc*c ; print("v = "+"{:e}".format(res))
    return "{:e}".format(res)

speed_non(75e3,True)
speed_relativistic(75e3,True)

def radius_non(v_perp,B,electron):
    return ((m_e if electron else m_p)*v_perp/ (q_p*B))

def radius_relativistic(v_perp,B,electron):
    return (gamma*(m_e if electron else m_p)*v_perp/ (q_p*B))

def Time_periodic_non(B,electron):
    return 2*np.pi*(m_e if electron else m_p) / (q_p * B)

def Time_periodic_relativistic(B,gamma,electron):
    return 2*np.pi*gamma*(m_e if electron else m_p) / (q_p * B)


def B_given_I_divided (n,I,start,rf): #r here is the one on RHS, n is number of division, I is the actual one
    res = 0
    I/=n ; i=start
    while (i<=start+n):
        res += (4*pi*1e-7)*I/ ( 2*pi*(rf*1e-3 - i*1e-3))
        print(rf*1e-3 - i*1e-3)
        i+=1

    return res

print(B_given_I_divided(10,10,-4.5,9))
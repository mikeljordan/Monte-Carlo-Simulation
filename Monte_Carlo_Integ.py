#Monte Carlo Process
#For cobble and non-cobble domain of integration
#function to compute the integrale and and the error range by Monte
#Carlo method
#To compute the tripple integral of f(x,y,z) = (1/(1+x^2))(1/(1+y^2))(1/(1+z^2))
#in the domain = [0,1]x[0,1]x[0,1]
from __future__ import division
import random as Rand
import numpy as np 

#function tocompute the product of element of a list or vector
def Prod(x):
        r = x[0]
        for k in xrange(1,len(x)):
                r*= x[k]
        return r

def Monte_carlo(f,Integ_x,Integ_y):
        n = len(Integ_x)
        # the dimension of the domain of integration
        Vol = Prod(np.array(Inter_y)-np.array(Inter_x))
        #the volume of the domain of Integration
        N = int(Vol/0.000001)
        #the number of randum point to generate
        print  "The Number of point taken is \n N = ",N
        #the list of list which will store the random point
        Y = [[]]
        for k in xrange(n-1):
                Y += [[]]
        #generation of random point in the domain of integration
        for i in xrange(n):
                for k in xrange(N):
                        Y[i].append(Rand.uniform(Inter_x[i],Inter_y[i]))
        r = 0
        V = np.array(Y)
        er  = 0
        for k in xrange(N):
                r += f(V[:,k])
                er += (f(V[:,k]))**2
        Integral = r*Vol/N
        error = Vol*np.sqrt((er/N-(r/N)**2)/N)
        #computation of the integral and the error upper bound
        return Integral,error

#definition of a sample function to test the efficiency of our program
def f(x):
        return (1/(1+ x[0]**2))*(1/(1+ x[1]**2))*(1/(1+ x[2]**2))
        
if __name__ == '__main__':
        #we change the format of printing of number
        format(long)
        #we define the domain of integration
        Inter_x = [0,0,0]
        Inter_y = [1,1,1]
        #we compute the integral and the error upper bound
        #Monte_carlo
        I,Error = Monte_carlo(f,Inter_x,Inter_y)
        Exact_integral = ((np.pi)/4)**3
        #We print the result
        print "\nApproximated value of the Integral: \n",I
        print "\nUpper bound of error: :",Error
        print "Exact value of Integral is in the range: [",I-Error,",",I+Error,"]\n"
        print "\nExact value of integral: ",Exact_integral
        print "\nAbsolute value of Exact error: ",np.abs(Exact_integral-I)

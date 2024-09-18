from bisection import*

def f(x):
    y = x**2 +10*x -39
    return y

a = float(input('tebakan Awal a = '))
b = float(input('tebakan Awal b = '))
tol = float(input('Toleransi = '))

x = bisection(f,a,b,tol)
print ("Akar Persamaan x  = {:}".format(x))

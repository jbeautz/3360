def RSA(x,e,n):
    return (x**e)%n

def gcdExtended(a, b):
    if a == 0 :
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y


# Driver code
a, b = 20,11
gcd, x, y = gcdExtended(a, b)
print(x,"*",a,"+",y,"*",b," = ",gcd)

#print(RSA(x,e,n))
##https://mathsci2.appstate.edu/~cookwj/sage/algebra/Euclidean_algorithm-poly.html

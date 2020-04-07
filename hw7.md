<font color = black>  

Jack Beautz  
jpb375  

#MATH 3360 Homework 7  

###Exercise 10A-7
$$\phi(n) = n - (p + q) + 1$$
So,
$$(p+q) = n-\phi(n)+1$$
Understanding quadratics reveals
$$(p-q)^2 = (p+q)^2 - 4n$$
$$(p-q)^2 = (n - (p + q) + 1)^2 - 4n$$
$$(p-q) = \sqrt{(n - (p + q) + 1)^2 - 4n}$$
Take the square root of this value.
By definition,
$$q = {(p+q)-(p-q)\over 2}$$  
$p$ can be solved for by subbing pack into the first equation.  



###Exercise CS 1.2  
The code has a minimum distance of $\omega(01-00)=\omega(01)=1$.  
In general a code can detect up to $d(C)-1$ errors. But in this case
it can detect up to $0$ errors.  

###Exercise CS 1.3
The minimum distance in $C$ is found between $y=\{000000\}$ and $x=\{100100\}$ where $\omega(x-y) = \omega(\{100100\}) = 2$.  
In general a code can detect up to $d(C)-1$ errors and can correct up to $\lfloor {d(C)-1\over 2}\rfloor$ errors.  
Therefore $C$ can detect up to 1 error and correct no errors.  

###Exercise CS 1.6  
The Sphere Packing Bound Theorem gives the following inequality which holds true for a code which can correct $t$ errors.  
$$M\sum_{i=0}^t {n\choose i}(q-1)^i \leq q^n$$
Plugging in the values from this problem we find
$$8\sum_{i=0}^1 {5\choose i}(2-1)^i \leq 2^5$$
$$8(5(1)+1) \leq 32$$
$$48 \leq 32$$
This is not true. Thus bob can not construct the code as described.  

##Exercise 1.8  
1. d(x, y) ≥ 0, with equality if and only if x = y  
If $x=y$, then there are no nonzero values in their difference. Thus $\omega(x-y)=0$. Hence, $d(x,y)=0$.  
If $d(x,y) = 0$, then $\omega(x-y)=0$. Hence, every value in $x-y$ is zero. Suppose this was possible with $y\neq x$. Then, there must exist at least one bit in the message which has a difference greater than 0. But then there is a nonzero value in the difference. Hence, $x=y$.  

2. d(x, y) = d(y, x)  
This implies $\omega(x-y) = \omega(y-x)$. Note that $\omega(x-y)$ simply counts the number of different bits between $x$ and $y$ because in binary $0-1=1-0=1$ and $1-1=0-0=0$. Therefore the nonequal bits in $x$ and $y$ are counted the same in $\omega(x-y)$ and $\omega(y-x)$.  

3. d(x, y) ≤ d(x, z) + d(z, y)  
Consider the $i$th bit of each message: $x_i,y_i,z_i$.  Suppose $x_i=y_i$, then $d(x_i,y_i)=0$. But then either $d(x_i,z_i)=d(y_i,z_i)=1$ or $d(y_i,z_i)=d(x_i,z_i)=0$. Thus, $d(x_i,y_i)\leq d(x_i,z_i)+d(y_i,z_i)$.  If $x_i\neq y_i$, then $d(x_i,y_i)=1$. In this case either $d(x_i,z_i)=1$ or $d(y_i,z_i)=0$. Thus, $d(x_i,y_i)\leq d(x_i,z_i)+d(y_i,z_i)$.  
Because this holds at the $i$th bit, we can construct messages by individually adding on bits which must hold to the above criteria. This is equivalent to adding to both sides of the inequality. Thus any message must satisfy the criteria.

***THE END***

<font color = white>  

Jack Beautz  
jpb375  

#MATH 3360 Homework 7  

###Exercise 10A-7
$$\phi(n) = n - (p + q) + 1$$
Then, $(p-q)$ is the square root of $(p+q)^2 - 4n$.  
Finally, $q$ is half the difference between $(p+q)$ and $(p-q)$  

###Exercise CS 1.2  
The code has a minimum distance of $\omega(01-00)=\omega(01)=1$.  
In general a code can detect up to $d(C)-1$ errors. But in this case
it can detect up to $0$ errors.  

###Exercise CS 1.3
The minimum distance in $C$ is found between $y=\{000000\}$ and $x=\{100100\}$ where $\omega(x-y) = \omega(\{100100\}) = 2$.  
In general a code can detect up to $d(C)-1$ errors and can correct up to $\lfloor {d(C)-1\over 2}\rfloor$ errors.  
Therefore $C$ can detect up to 1 error and correct no errors.  

###Exercise CS 1.6  
Notice that to do this and correct a single error, the strings of length five must all
differ in at least three places. Suppose we could write down eight strings of length five that
all differed in at least three places. Then, they could have at most two places the same. Now,
there must be at least four strings that have the same first digit (since you only have 0 and 1
to choose from and there are a total of 8 strings). Of those four, there must be at least two
that have the same second digit (for the same reason as above). So, we have two strings that
are the same in the first two places (let’s just suppose for simplicity that they both start with
00). It follows that they must be different in the last three positions. Now, consider one of
the other strings (remember, there were at least 4) that starts with 0. It must differ from the
two strings starting with 00 in at least three places. So, of the last 4 positions, it must differ
from each of the 00 strings in at least three positions. But since the 00 strings differ in the
last three positions, this is impossible.

***THE END***

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
To correct a single error using the letters, bob must have messages which all differ in at least three places.  
Assume we have 8 messages of length 5 which all differ in at least three places. Then, each two can have at most two places the same. Without loss of generality let there be four messages with the same first digit 1. In the messages beginning with 1, two of them must have 1 as the second digit. Among these four messages they must differ in the last three spots.  

Consider one of the other four messages, beginning with 0. It must differ in the last three spots from the messages beginning with 11. But since the two 11 strings differ in the last three spots this string must begin with something other than 0. Thus it is impossible.  



***THE END***

<font color = white>

Jack Beautz  
jpb375
#MATH 3360 Homework 1

###Exercise 2A-1
Prove that $1 + 2 + 3 + . . .+ n = n(n + 1)/2$ for all $n \geq 1$.

Base Case: $n = 1$  
$$1 = 1(1+1)/2 = 1$$
The induction hypothesis holds at the base case.  

Step Case: $n = m$  
$$1 + 2 + 3 + . . .+ m = m(m + 1)/2$$
Consider the $m + 1$ step.
$$1 + 2 + 3 + . . .+ m + m + 1= (m+1)(m + 2)/2$$
Plug in the assumption $1 + 2 + 3 + . . .+ m = m(m + 1)/2$
$$m(m + 1)/2 + m  + 1 = (m+1)(m + 2)/2$$
$$m(m + 1) + 2m  + 2 = (m+1)(m + 2)$$
$$m^2 + 3m + 2 = m^2 + 3m + 2$$

Hence, the induction hypothesis holds at the step and base case. Therefore the statement must be true.

###Exercise 2A-3
Prove that $1 + 2 + 2^2 + ... + 2^{n−1} = 2^n − 1$ for all $n>1$.  

Base Case: $n=2$.
$$1 + 2 = 2^2 -1 = 3$$
The induction hypothesis holds at the base case.

Step Case: $n=m$.  
$$1 + 2 + 2^2 + ... + 2^{m−1} = 2^m − 1$$
Consider the $m+1$ step.  
$$1 + 2 + 2^2 + ... + 2^{m} = 2^{m+1} − 1$$
Plugging in the assumption that $1 + 2 + 2^2 + ... + 2^{m−1} = 2^m − 1$.
$$2^m − 1 + 2^m = 2^{m+1} -1$$
$$2^{m+1} -1 = 2^{m+1} -1$$

Hence, the induction hypothesis holds at the step and base case. Therefore the statement must be true.

###Exercise 3C-35(ii)
21063 and 43137

$$43137 = 2\times 21063 + 1011$$
$$21063 = 20\times 1011 + 843$$
$$1011 = 1\times 843 + 168$$
$$843 = 168 * 5 + 3$$
$$168 = 56 \times 3 + 0$$

Hence, by Euclid's Algorithm (with Division),  $gcd(21063,43137) = 3$.

###Exercise 3D-39(ii)








***THE END***

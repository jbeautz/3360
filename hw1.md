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
242 and 1870

By Bezout's Identity, there exists integer $\alpha, \beta$ such that $(242,1870) = 242\alpha + 1870\beta$.

$$\pmatrix{1&0\\0&1}\pmatrix{\alpha\\\beta} = \pmatrix{242\\1870}$$
$$\pmatrix{1&0\\-7&1}\pmatrix{\alpha\\\beta} = \pmatrix{242\\176}$$
$$\pmatrix{8&-1\\-7&1}\pmatrix{\alpha\\\beta} = \pmatrix{66\\176}$$
$$\pmatrix{8&-1\\-23&3}\pmatrix{\alpha\\\beta} = \pmatrix{66\\44}$$
$$\pmatrix{31&-4\\-23&3}\pmatrix{\alpha\\\beta} = \pmatrix{22\\44}$$
$$\pmatrix{31&-4\\-85&11}\pmatrix{\alpha\\\beta} = \pmatrix{22\\0}$$

Hence, $(242, 1870) = 22$ by Euclid's Algorithm.  
$$31\times 242 - 4\times 1870 = 22$$
$$\alpha = -4$$
$$\beta = 31$$

###Exercise 3E-57
######(i) 114x + 270y = 0  
Use Euclid's Algorithm.
$$270 = 2\times 114 + 42$$
$$114 = 2\times 42 + 30$$
$$42 = 1\times 30 + 12$$
$$30 = 2\times 12 + 6$$
$$12 = 2\times 6 + 0$$
Hence, (270, 114) = 6.  

$$a' = {114\over 6} = 19$$
$$b' = {270\over 6} = 45$$

Hence, $\forall k\in \mathbb{Z}$
$$x = 45k$$
$$y = -19k$$

######(ii) 114x + 270y = 24.
From the previous exercise we have
$$x_0 = -19$$
$$y_0 = 45$$

Use Extended Euclidian Algorithm to find $\alpha, \beta$.  
$$\pmatrix{1&0\\0&1}\pmatrix{\alpha\\\beta} = \pmatrix{114\\270}$$
$$\pmatrix{1&0\\-2&1}\pmatrix{\alpha\\\beta} = \pmatrix{114\\42}$$
$$\pmatrix{5&-2\\-2&1}\pmatrix{\alpha\\\beta} = \pmatrix{30\\42}$$
$$\pmatrix{5&-2\\-7&3}\pmatrix{\alpha\\\beta} = \pmatrix{30\\12}$$
$$\pmatrix{19&-8\\-7&3}\pmatrix{\alpha\\\beta} = \pmatrix{6\\12}$$
$$\pmatrix{19&-8\\45&-19}\pmatrix{\alpha\\\beta} = \pmatrix{6\\0}$$



Therefore,
$$\alpha = 19$$
$$\beta = -8$$

$$114(19) + 270(-8) = 6$$
Multiply by $4$
$$114(76) + 270(-32) = 24$$

Hence, for $k\in \mathbb{Z}$
$$x = 76 - 45k$$
$$y = -32 + 19k$$
Is a solution to the equation.


###Exercise 3E-58(i)
$66x + 45y = 0$

First find $(66, 45)$.
$$66 = 1\times 45 + 21$$
$$45 = 2\times 21 + 3$$
$$21 = 7\times 3 + 0$$

Hence, $3 = (66, 45)$.

$$a' = 22$$
$$b' = 15$$

Therefore $\forall k \in \mathbb{Z}$
$$x = 15k$$
$$y = -22k$$
Is a solution to the equation.

###Exercise 3E-60(i)
$242x + 1870y = 66$

From Exercise Exercise 3D-39(ii) we know $(242, 1870) = 22$, $\alpha = -4$, and $\beta = 31$.

$$242(31) + 1870(-4) = 22$$
$$242(93) + 1870(-12) = 66$$

Dividing, $a$ and $b$ by $(a, b)$ we find $a',b'$.
$$a' = 11$$
$$b' = 85$$

Therefore we have $\forall k\in \mathbb{Z}$,
$$x = 93 - 85k$$
$$y = -12 + 11k$$
Is a solution to the equation.

The smallest $x>0$ exists for $k = 1$.
$$x_0 = 93 - 85 = 8$$
$$y_0 = -12 + 11 = -1$$

###Exercise 3E-62
######(i) 133x + 203y = 38,
Check if $(133, 203)|38$

Use Euclidian Algorithm to find GCD.
$$203 = 1\times 133 + 70$$
$$133 = 1\times 70 + 63$$
$$70 = 1\times 63 + 7$$
$$63 = 9\times 7 + 0$$
Hence, $(133, 203) = 7$.

$7$ does not divide $38$ so there are no integer solutions.

######(ii) 133x + 203y = 40,
As shown in part (i), $7 = (133, 203)$.

$7$ does not divide 40 so there are no integer solutions.

######(iii) 133x + 203y = 42,
As shown in part (i), $7 = (133, 203)$.

$7$ does divide 42 so there are infinitely many integer solutions.

$$a' = {133\over 7} = 19$$
$$b' = {203\over 7} = 29$$

Use Extended Euclidian Algorithm to find $\alpha, \beta$.

$$\pmatrix{1&0\\0&1}\pmatrix{\alpha\\\beta} = \pmatrix{133\\203}$$
$$\pmatrix{1&0\\-1&1}\pmatrix{\alpha\\\beta} = \pmatrix{133\\70}$$
$$\pmatrix{2&-1\\-1&1}\pmatrix{\alpha\\\beta} = \pmatrix{63\\70}$$
$$\pmatrix{2&-1\\-3&2}\pmatrix{\alpha\\\beta} = \pmatrix{63\\7}$$
$$\pmatrix{29&-19\\-3&2}\pmatrix{\alpha\\\beta} = \pmatrix{0\\7}$$

Hence,
$$\alpha = -3$$
$$\beta = 2$$

$$133(-3) + 203(2) = 7$$
$$133(-18) + 203(12) = 42$$

Therefore $\forall k\in \mathbb{Z}$,
$$x = -18 + 29k$$
$$y = 12  - 19k$$


######(iv) 133x + 203y = 44.
As shown in part (i), $7 = (133, 203)$.

$7$ does not divide 44 so there are no integer solutions.








***THE END***

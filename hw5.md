<font color = black>

Jack Beautz  
jpb375  

#MATH 3360 Homework 5

###Exercise 12A-16
$$x\cong 1 (mod 2)$$
$$x\cong 2 (mod 3)$$
$(2,3) = 1$ and $1|(2-1)$ so there is a solution.  

Observe $2(-1) + 3(1) = 1$ by Bezout.    

Hence, $x = 1(3)(1) + 2(2)(-1)$ using CRT.
$$x \cong -1 (mod6)$$
$$x \cong 5 (mod6)$$
By guessing I find I find the solution which fits the remaining congruences.  
$$5\cong 1 (mod 2)$$
$$5\cong 2 (mod 3)$$
$$5\cong 5 (mod 6)$$
$$5\cong 5(mod 12)$$


###Exercise 12A-20
$$x\cong 1 (mod 2)$$
$$x\cong 1 (mod 3)$$
$$x\cong 1 (mod 4)$$
$$x\cong 1 (mod 5)$$
$$x\cong 1 (mod 6)$$
$$x\cong 0 (mod 7)$$

Consider the last two congruences of the system.  
$$x\cong 1 (mod 6)$$
$$x\cong 0 (mod 7)$$
$(6,7) = 1$ and $1|(1-0)$ so there is a solution.  

Observe using Bezout $7(1) + 6(-1) = 1$.

Hence by CRT, $x \cong 0(6)(-1) + 1(7)(1) (mod (6)(7))$
$$x\cong 7 (mod 42)$$
Consider the middle two congruences of the system.
$$x\cong 1 (mod 4)$$
$$x\cong 1 (mod 5)$$
$(4,5)=1$ and $1|(1-1)$ so there is a solution.  

Using Bezout's $5(1) + 4(-1) = 1$.  

Hence by CRT, $x\cong 1(5)(1) + 1(4)(-1) (mod (4)(5))$  
$$x\cong 1 (mod 20)$$


Finally, consider the first two congruences.  
$$x\cong 1 (mod 2)$$
$$x\cong 1 (mod 3)$$
$(2,3)=1$ and $1|(3-2)$ so there is a solution.  

Using Bezout $2(-1) + 3(1) = 1$.  

Hence by CRT, $x = 1(2)(-1) + 1(3)(1)$.
$$x \cong 1 (mod 6)$$

Now the system has been reduced to three congruences.  
$$x\cong 7 (mod 42)$$
$$x\cong 1 (mod 20)$$
$$x\cong 1 (mod 6)$$

Now, I will solve the first two congruences.  
$$x\cong 7 (mod 42)$$
$$x\cong 1 (mod 20)$$
$(42, 20) = 2$ and $2|(42-20)$ so there is a solution.  
Let $m' = 21$ and $n' = 10$.  

By Bezout $21(1) + 10(-2) = 1$.  

Hence, by CRT $x = 7(10)(-2) + 1(21)(1)$
$$x\cong  -119 (mod 420)$$
$$x\cong 301 (mod 420)$$

Notice that this satisfies $x\cong 1 (mod 6)$.  

Hence, $x=301 (mod 420)$.

The smallest positive integer is 301.  

###Exercise 12A-28
For there to be a solution to the system,
$$(b-a)|d$$
where $d=(m,n)$.  
Note $d=2 = (6,4)$.  
Now we need all pairs $(a_1,a_2) from $a_1\in [0,4]$ and $a_2\in [0,6]$ such that $a_1-a_2$ is a multiple of 2.  

$(0,2),(1,3),(2,0),(4,0),(3,1),(5,1),(4,2),(5,3),(0,0),(1,1),(2,2),(3,3)$

There are 12.  


###Exercise 12B-35
####(i)
11,13,15 are pairwise coprime.  

By the CRT there is a unique solution modulo $(11)(13)(15)$

The solution to the first two congruences is $e_1\cong 0 (mod 195)$.
$(11,195)=1$ so now we need EEA.

$$\pmatrix{1&0\\0&1}\pmatrix{\alpha\\\beta}=\pmatrix{195\\11}$$
$$\pmatrix{1&-17\\0&1}\pmatrix{\alpha\\\beta}=\pmatrix{8\\11}$$
$$\pmatrix{1&-17\\-1&18}\pmatrix{\alpha\\\beta}=\pmatrix{8\\3}$$
$$\pmatrix{3&-53\\-1&18}\pmatrix{\alpha\\\beta}=\pmatrix{2\\3}$$
$$\pmatrix{3&-53\\-4&71}\pmatrix{\alpha\\\beta}=\pmatrix{2\\1}$$

$$195(-4) + 11(71) = 1$$

Hence, $e_1\cong 0(11)(71) + 1(195)(-4) (mod 2145)$
$$e_1\cong 1365 (mod 2145)$$

The solution to the first and last congruences is $e_2\cong 0 (mod 165)$

$(13,165) = 1$ so now we need EEA.  

$$\pmatrix{1&0\\0&1}\pmatrix{\alpha\\\beta}=\pmatrix{165\\13}$$
$$\pmatrix{1&-12\\0&1}\pmatrix{\alpha\\\beta}=\pmatrix{9\\13}$$
$$\pmatrix{1&-12\\-1&13}\pmatrix{\alpha\\\beta}=\pmatrix{9\\4}$$
$$\pmatrix{3&-38\\-1&13}\pmatrix{\alpha\\\beta}=\pmatrix{1\\4}$$
$$165(3) + 13(-38) = 1$$

Hence, $e_2 \cong 0(13)(-38) + 1(165)(3) (mod 2145)$.  
$$e_2 = 495 (mod 2145)$$

The solution to the second and last congruences is $e_3\cong 0 (mod 143)$$

$(143, 15) = 1$ so we need EEA.  
$$\pmatrix{1&0\\0&1}\pmatrix{\alpha\\\beta}=\pmatrix{143\\15}$$
$$\pmatrix{1&-9\\0&1}\pmatrix{\alpha\\\beta}=\pmatrix{8\\15}$$
$$\pmatrix{1&-9\\-1&10}\pmatrix{\alpha\\\beta}=\pmatrix{8\\7}$$
$$\pmatrix{2&-19\\-1&10}\pmatrix{\alpha\\\beta}=\pmatrix{1\\7}$$
$$143(2) + 15(-19) = 1$$

Hence, $e_3 \cong 0(15)(-19) + 1(143)(2) (mod 2145)$.  
$$e_3 \cong 286 (mod 2145)$$

####(ii)
Use the coefficients from (i)

$$x \cong  3e_1 + 5e_2 + 8e_3 (mod 2145)$$
$$x \cong 3(1365) + 5(495) + 8(286) (mod 2145)$$
$$x \cong 8858 (mod 2145)$$
Therefore the smallest positive value is
$$x_0 = 278$$

####(iii)
Use coefficients from (ii)

$$x \cong  9e_1 + 2e_2 - 7e_3 (mod 2145)$$
$$x \cong 9(1365) + 2(495) + -7(286) (mod 2145)$$
$$x \cong 11273 (mod 2145)$$

In general $x_n = 548 + 2145n$.  

###Exercise 12D-47


Addition:  
|       | (0,0) | (0,1) | (1,0) | (1,1) |
| -     |   -   |   -   |   -   |   -   |
| (0,0) | (0,0) | (0,1) | (1,0) | (1,1) |
| (0,1) | (0,1) | (0,0) | (1,1) | (1,0) |
| (1,0) | (1,0) | (1,1) | (0,0) | (0,1) |
| (1,1) | (1,1) | (1,0) | (0,1) | (0,0) |

Multiplication:  
|       | (0,0) | (0,1) | (1,0) | (1,1) |
| -     |   -   |   -   |   -   |   -   |
| (0,0) | (0,0) | (0,0) | (0,0) | (0,0) |
| (0,1) | (0,0) | (0,1) | (0,0) | (0,1) |
| (1,0) | (0,0) | (0,0) | (1,0) | (1,0) |
| (1,1) | (0,0) | (0,1) | (1,0) | (1,1) |


###Exercise 12D-49

$\mathbb{Z}_10$
$$\{0,1,2,3,4,5,6,7,8,9\}$$
$\mathbb{Z}_2\times \mathbb{Z}_5$
$$\{(0,0),(1,0),(0,1),(1,1),(0,2),(1,2),(0,3),(1,3),(0,4),(1,4)\}$$
$$\psi: \mathbb Z_{10}\to \mathbb{Z}_{2}\times \mathbb{Z}_5$$
$$\psi([x]_ {10}) = ([x]_ 2, [x]_ 5)$$
$\psi(0)=(0,0)$  
$\psi(1)=(1,1)$  
$\psi(2)=(0,2)$  
$\psi(3)=(1,3)$  
$\psi(4)=(0,4)$  
$\psi(5)=(1,0)$  
$\psi(6)=(0,1)$  
$\psi(7)=(1,2)$  
$\psi(8)=(0,3)$  
$\psi(9)=(1,4)$  



**THE END**

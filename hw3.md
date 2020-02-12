<font color = white>  

Jack Beautz  
jpb375  

#MATH 3360 Homework 3

###Exercise 5E-40
$3^{1728}\cong 1 (mod 1729)$  
First observe that $1729 = 19\times 91$ and $(19, 91)=1$. Hence, it is sufficient to show that $3^{1728} \cong 1 (mod 19)$ and $3^{1728} \cong 1 (mod 91)$.  

First check for $m=91$.
$${3^4}^{432} \cong 1 (mod 91)$$
$$(-10)^{432} \cong 1 (mod 91)$$
$$(100)^{216} \cong 1 (mod 91)$$
$$9^{216} \cong 1 (mod 91)$$
$$(9^2)^{108} \cong 1 (mod 91)$$
$$(-10)^{108} \cong 1 (mod 91)$$
$$100^{54} \cong 1 (mod 91)$$
$$9^{54} \cong 1 (mod 91)$$
$$81^{27} \cong 1 (mod 91)$$
$$(-10)(100)^{13} \cong 1 (mod 91)$$
$$(-10)(9)^{13} \cong 1 (mod 91)$$
$$(-90)81^6 \cong 1 (mod 91)$$
$$(-10)^6 \cong 1 (mod 91)$$
$$(100)^3 \cong 1 (mod 91)$$
$$9^3 \cong 1 (mod 91)$$
$$1 \cong 1 (mod 91)$$


Next, $m=19$.
$${3^4}^{432} \cong 1 (mod 19)$$
$${5}^432 \cong 1 (mod 19)$$
$${5^{3}}^144 \cong 1 (mod 19)$$
$$11^{144} \cong 1 (mod 19)$$
$$121^{72} \cong 1 (mod 19)$$
$$7^{72} \cong 1 (mod 19)$$
$$49^{36} \cong 1 (mod 19)$$
$$11^{36} \cong 1 (mod 19)$$
$$121^{18} \cong 1 (mod 19)$$
$$7^{18}\cong 1 (mod 19)$$
$$49^9 \cong 1 (mod 19)$$
$$11^9 \cong 1 (mod 19)$$
$$(11)(121)^4 \cong 1 (mod 19)$$
$$(11)(49)^2 \cong 1 (mod 19)$$
$$11(121) \cong 1 (mod 19)$$
$$77 \cong 1 (mod 19)$$
$$1 \cong 1 (mod 19)$$

Hence, $3^{1728}\cong 1 (mod 1729)$.  

###Exercise 5E-42
Find all numbers a ≤ 36 so that 16a ≡ 0 (mod 36).  

Let $a,b\in\mathbb{Z}$ such that
$$16 a = 36b$$
The fundamental theorem of arithmetic guarantees there exists a unique prime factorization of $16$ and $36$.
$$16 = 2^4$$
$$36 = 2^2\times 3^2$$

Hence, $[16,36] = 2^4\times 3^2 = 144$  
Therefore $a = 9$ satisfies.

Multiplying both sides of the equation by integers less than 4 give the remaining $a$.

$$a = 9\alpha$$
For $\alpha \in \mathbb{Z}$ and $\alpha \leq 4$.

###Exercise 5E-43  
Prove If $ra \cong rb (mod m)$, then $a \cong b (mod
{m\over(r,m)} )$.

Write the congruence as an equation with the integer $k$.
$$ra = rb + km$$
$$a = b + {km\over r}$$
$$a = b + k'{m\over (r,m)}$$
Where $k'$ is an integer.  
Hence, $a \cong b (mod{m\over(r,m)})$

###Exercise 5F-44
(i) 12x ≡ 5 (mod 29)  
$$(12, 29) = 1$$
1 divides 5 and $(12, 29) = 1$ so there is a solution. We can find it using Bezout's identity and EEA.  
$$\pmatrix{1&0\\0&1}\pmatrix{\alpha\\\beta} = \pmatrix{12\\29}$$
$$\pmatrix{1&0\\-2&1}\pmatrix{\alpha\\\beta} = \pmatrix{12\\5}$$

Hence, $-12(-2) - 5 = 29(-1)$.  
The smallest non-negative $x$ will be $29 -2 = 27$.

**x = 27**


(ii) 12x ≡ 5 (mod 38)  
$$(12, 38) = 2$$
2 does not divide 5 so there are no solutions.  

(iii) 12x ≡ 5 (mod 47)  
$$(12, 47) = 1$$
1 divides 5 and $(12, 47) = 1$ so there is a solution. We can find it using Bezout and EEA.  
$$\pmatrix{1&0\\0&1}\pmatrix{\alpha\\\beta} = \pmatrix{12\\47}$$
$$\pmatrix{1&0\\-3&1}\pmatrix{\alpha\\\beta} = \pmatrix{12\\11}$$
$$\pmatrix{4&-1\\-3&1}\pmatrix{\alpha\\\beta} = \pmatrix{1\\11}$$
$$\pmatrix{4&-1\\-47&12}\pmatrix{\alpha\\\beta} = \pmatrix{1\\0}$$
Hence, $12(4) - 47 = 1$ and $12(20) - 47(5) = 5$.  

**x = 20**  

(iv) 12x ≡ 5 (mod 56)  
$$(12, 56) = 4$$
4 does not divide 5 so there are no solutions.  

(v) 12x ≡ 5 (mod 65)  
$$(12, 65) = 1$$
1 divides 5 and $(12, 65) = 1$ so there is a solution. We can find it using Bezout and EEA.  
$$\pmatrix{1&0\\0&1}\pmatrix{\alpha\\\beta} = \pmatrix{12\\65}$$
$$\pmatrix{1&0\\-5&1}\pmatrix{\alpha\\\beta} = \pmatrix{12\\5}$$
Hence, $12(-5) + 65 = 5$. So $x = -5\cong 60$ mod (65).  

**x = 60**

###Exercise 5F-50
Solve 7x ≡ 13 (mod 218).  
$$(7, 218) = 1$$
1 divides 13 so there is a solution.  
$$\pmatrix{1&0\\0&1}\pmatrix{\alpha\\\beta} = \pmatrix{7\\218}$$
$$\pmatrix{1&0\\-31&1}\pmatrix{\alpha\\\beta} = \pmatrix{7\\1}$$
Hence, $7(-31) + 218 = 1$ and $7(-403) + 218(13) = 13$.  
So, $x \cong 33 (mod 218)$.


###Exercise 6C-5
Write down the addition and multiplication tables for arithmetic modulo 4.

Addition:  
|   | 0 | 1 | 2 | 3 |
| - | - | - | - | - |
| 0 | 0 | 1 | 2 | 3 |
| 1 | 1 | 2 | 3 | 0 |
| 2 | 2 | 3 | 0 | 1 |
| 3 | 3 | 0 | 1 | 2 |

Multiplication:  
|   | 0 | 1 | 2 | 3 |
| - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 2 | 3 |
| 2 | 0 | 2 | 0 | 2 |
| 3 | 0 | 3 | 2 | 1 |

###Exercise 6C-6
Write down the addition and multiplication tables for arithmetic modulo 5.

Addition:  
|   | 0 | 1 | 2 | 3 | 4 |
| - | - | - | - | - | - |
| 0 | 0 | 1 | 2 | 3 | 4 |
| 1 | 1 | 2 | 3 | 4 | 0 |
| 2 | 2 | 3 | 4 | 0 | 1 |
| 3 | 3 | 4 | 0 | 1 | 2 |
| 4 | 4 | 0 | 1 | 2 | 3 |

Multiplication:  
|   | 0 | 1 | 2 | 3 | 4 |
| - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 2 | 3 | 4 |
| 2 | 0 | 2 | 4 | 1 | 3 |
| 3 | 0 | 3 | 1 | 4 | 2 |
| 4 | 0 | 4 | 3 | 2 | 1 |


###Exercise 6C-8  
(i) $[6]_ {10} [x]_ {10} = [4]_ {10}$  
$$[6]_ {10} [4]_ {10} = 4_ {10}$$
$$[(6)(4)]_ {10} = 4_ {10}$$
$$[24]_ {10} = [2(10) + 4]_ {10} = [4]_ {10}$$
$$x = [4]_ {10}$$  

(ii) $[5]_ {7} [x]_ {7} = [3]_ {7}$  
$$[10]_ 7 = [3]_ 7$$
$$[2]_ 7 [5]_ 7 = [7 + 3]_ 7 = [3]_ 7$$
$$x = [2]_ 7$$

(iii) $[4]_ 7 [x]_ 7 = [2]_ 7$  
$$[4]_ 7 [4]_ 7 = [14 + 2]_ 7 = [2]_ 7$$
$$x = [4]_ 7$$

(iv) $[4]_ {17} [x]_ {17} = [2]_ {17}$  
$$[4]_ {17} [9]_ {17} = [17(2) + 2]_ {17} = [2]_ {17}$$
$$x = [9]_ {17}$$

(v) $[13]_ {19} [x]_ {19} = [16]_ {19}$  
$$[13]_ {19} [10]_ {19} = [(19)(6) + 16]_ {19} = [16]_ {19}$$


###Exercise 6D-22
$$[0] = [0]$$
$$[2] = [2]$$
$$[2^2] = [4]$$
$$[2^3] = [8]$$
$$[2^4] = [16] = [3]$$
$$[2^5] = [2\times 3] = [6]$$
$$[2^6] = [2\times 6] = [12]$$
$$[2^7] = [2\times 12] = [11]$$
$$[2^8] = [2\times 11] = [9]$$
$$[2^9] = [2\times 9] = [5]$$
$$[2^{10}] = [2\times 5] = [10]$$
$$[2^{11}] = [2\times 10] = [7]$$
$$[2^{12}] = [2\times 7] = [1]$$

Because all 13 classes of $\mathbb{Z}_{13}$ are equivalent to the classes of $\{0,2,...,2^{12}\}$, the set is a CSR.  

###Exercise 6D-32
Find all primitive roots b modulo 11 with 1 ≤ b ≤ 11.  

Consider the prime classes in mod 11. $b=2, 3, 5, 7$. $0,1$ will not work because all powers are the same.  

Now, try each option for $b$.

$$[0] = [0]$$
$$[2] = [2]$$
$$[2^2] = [4]$$
$$[2^3] = [8]$$
$$[2^4] = [16] = [5]$$
$$[2^5] = [2\times 5] = [10]$$
$$[2^6] = [2\times 10] = [9]$$
$$[2^7] = [2\times 9] = [7]$$
$$[2^8] = [2\times 7] = [3]$$
$$[2^9] = [2\times 3] = [6]$$
$$[2^{10}] = [2\times 6] = [1]$$

There are 11 distinct classes formed by the powers so 2 is a primitive root.

$$[0] = [0]$$
$$[3] = [3]$$
$$[3^2] = [9]$$
$$[3^3] = [5]$$
$$[3^4] = [3\times 5] = [4]$$
$$[3^5] = [3\times 4] = [1]$$

All later values of $[3^k]$ will cycle back through earlier classes. Hence 3 is not a primitive root.


$$[0] = [0]$$
$$[4] = [4]$$
$$[4^2] = [5]$$
$$[4^3] = [4\times 5] = [9]$$
$$[4^4] = [4\times 9] = [3]$$
$$[4^5] = [4\times 3] = [1]$$

All later values of $[4^k]$ will cycle back through earlier classes. Hence 4 is not a primitive root.


$$[0] = [0]$$
$$[5] = [5]$$
$$[5^2] = [3]$$
$$[5^3] = [5\times 3] = [4]$$
$$[5^4] = [5\times 4] = [9]$$
$$[5^5] = [5\times 9] = [1]$$

All later values of $[5^k]$ will cycle back through earlier classes. Hence 5 is not a primitive root.

$$[0] = [0]$$
$$[6] = [6]$$
$$[6^2] = [3]$$
$$[6^3] = [6\times 3] = [7]$$
$$[6^4] = [6\times 7] = [9]$$
$$[6^5] = [6\times 9] = [10]$$
$$[6^6] = [6\times 10] = [5]$$
$$[6^7] = [6\times 5] = [8]$$
$$[6^8] = [6\times 8] = [4]$$
$$[6^9] = [6\times 4] = [2]$$
$$[6^{10}] = [6\times 2] = [1]$$

There are 11 distinct classes formed by the powers so 6 is a primitive root.

$$[0] = [0]$$
$$[7] = [7]$$
$$[7^2] = [5]$$
$$[7^3] = [7\times 5] = [2]$$
$$[7^4] = [7\times 2] = [3]$$
$$[7^5] = [7\times 3] = [10]$$
$$[7^6] = [7\times 10] = [4]$$
$$[7^7] = [7\times 4] = [6]$$
$$[7^8] = [7\times 6] = [9]$$
$$[7^9] = [7\times 9] = [8]$$
$$[7^{10}] = [7\times 8] = [1]$$

There are 11 distinct classes formed by the powers so 7 is a primitive root.

$$[0] = [0]$$
$$[8] = [8]$$
$$[8^2] = [9]$$
$$[8^3] = [8\times 9] = [6]$$
$$[8^4] = [8\times 6] = [4]$$
$$[8^5] = [8\times 4] = [10]$$
$$[8^6] = [8\times 10] = [3]$$
$$[8^7] = [8\times 3] = [2]$$
$$[8^8] = [8\times 2] = [5]$$
$$[8^9] = [8\times 5] = [7]$$
$$[8^{10}] = [8\times 7] = [1]$$

There are 11 distinct classes formed by the powers so 8 is a primitive root.

$$[0] = [0]$$
$$[9] = [9]$$
$$[9^2] = [4]$$
$$[9^3] = [9\times 4] = [3]$$
$$[9^4] = [9\times 3] = [5]$$
$$[9^5] = [9\times 5] = [1]$$

All later values of $[9^k]$ will cycle back through earlier classes. Hence 9 is not a primitive root.

$$[0] = [0]$$
$$[10] = [10]$$
$$[10^2] = [1]$$

All later values of $[10^k]$ will cycle back through earlier classes. Hence 10 is not a primitive root.

**Therefore the primitive roots of 11 are $b=2,6,7,8$.**


###Exercise 6D-37
(i) Consider the equation in $\mathbb{Z}_m$.
$$[b][a_i] = [a_j]$$
Solve for $a_i$. $b,m$ are coprime and $b|a_j$ so we know there is exactly one solution $[a_i]\in \mathbb{Z}_m$ which will be mapped to $[a_j]$.  
Now we need to show each $a_j$ corresponds to a different $[a_i]$ such that $[b][a_i] = [a_j]\neq [a_k]$ when $j\neq k$.  
Assume $[b][a_i] = [a_j] = [a_k]$.
$$(ba_i - a_k)|m$$
and
$$(ba_i - a_j)|m$$
But $a_j, a_k < m$ so this is only possible if $j=k$. Hence, each $[ba_i]$ equals a distinct $[a_j]$. Because there is $m$ elements in both sets, there must be a bijection.  Thus $\{ba_1,..., ba_m\}$ is a CSR.


(ii)
Solve for $a_i$. Let $d = (b,m)$ such that there must be $d>1$ solutions to the equation in $\mathbb{Z}_m$.  
If there $d$ different classes equivalent to $[ba_i]$, there is no isomorphism between $\{ba_1,...,b_m\}$ and $\{a_1,...,a_m\}$. $\{ba_1,...,b_m\}$ is not a CSR.  

###Exercise 6E-46
The following numbers in $\mathbb{Z}_20$ are coprime with 20 and therefore have inverses.  
$$1,3,7,9,11,13,17,19$$

$$[1]\times [1] = [1\times 1] = [1]$$
$[1]$ is the inverse of $[1]$.  

$$[3]\times [7] = [21] = [1]$$
$[7]$ is the inverse of $[3]$.  

$$[7]\times [3] = [21] = [1]$$
$[3]$ is the inverse of $[7]$.  

$$[9]\times [9] = [81] = [1]$$
$[9]$ is the inverse of $[9]$.

$$[11]\times [11] = [121] = [1]$$
$[11]$ is the inverse of $[11]$.

$$[13]\times [17] = [221] = [1]$$
$[17]$ is the inverse of $[13]$.  

$$[17]\times [13] = [221] = [1]$$
$[13]$ is the inverse of $[17]$.  

$$[19]\times [19] = [361] = [1]$$
$[19]$ is the inverse of $[19]$.  


###6E-49
(i) If p > 2 is prime, show that {1, 2, . . . , p − 1} is a complete set of units modulo p.  

Because $p$ is prime, all numbers in $\mathbb{Z}_m$ except 0 are coprime with $p$.  Hence, all numbers except 0 have an inverse.  
There must be $p-1$ inverses because there must be one for each element in $\mathbb{Z}_m$ except 0.  
If 0 is one of the inverses then $0\times a_i = 1$. $0\neq 1$ so this is not possible. Hence, choose the set of $p-1$ elements of $\mathbb{Z}_m$ which does not include 0. This is the CSU above.  

(ii) Show that {1, 3, −1, −3} is a complete set of units modulo 10.  

The following numbers are coprime with 10.  
$$1,3,7,9$$
Hence there are 4 inverses.
$$[1]\times [1] = [1]$$
$$[3]\times [-3] = [-9] = [1]$$
$$7\times [3] = [21] = 1$$
$$9\times [-1] = [-9] = 1$$

Hence, the above set is a CSU.  

(iii) Find a complete set of units modulo 24.  
The following numbers are coprime with 24.  
$$1,5,7,11,13,17,19,23$$
Each of these must have an inverse.  
$$[1]\times [1] = [1]$$
Hence, [1] is the inverse of [1] in $\mathbb{Z}_24$.  

$$[5]\times [5] = [25] = [1]$$
Hence, [5] is the inverse of [5] in $\mathbb{Z}_24$.  

$$[7]\times [7] = [49] = [1]$$
Hence, [7] is the inverse of [7] in $\mathbb{Z}_24$.  

$$[11]\times [11] = [121] = [1]$$
Hence, [11] is the inverse of [11] in $\mathbb{Z}_24$.  

$$[13]\times [13] = [169] = [1]$$
Hence, [13] is the inverse of [13] in $\mathbb{Z}_24$.  

$$[17]\times [17] = [289] = [1]$$
Hence, [17] is the inverse of [17] in $\mathbb{Z}_24$.  

$$[19]\times [19] = [361] = [1]$$
Hence, [19] is the inverse of [19] in $\mathbb{Z}_24$.  

$$[23]\times [23] = [529] = [1]$$
Hence, [23] is the inverse of [23] in $\mathbb{Z}_24$.

Thus, the complete set of units is $\{1,3,7,11,13,19,23\}$.

##6E-50  
Exercise 49 showed $\{1,...,p-1\}$ is a complete set of units for $\mathbb{Z}_p$ for $p\in\mathbb{P}$.  
$S = \{1,...,p-1\}$ must be a complete set of units.  
Consider the complete set of units for $\mathbb{Z}_p$,
$$S' = \{1,-1,2,-2,...,{p-1\over 2},-{p-1\over 2}\}$$
The positive elements of $S'$ are exactly the same as the first ${p-1\over 2}$ elements of $S$.  
Next I will show the last ${p-1\over 2}$ elements of $S$ are congruent to the negative elements of $S'$ modulo $p$.  
$$[-1] = [p-1]$$
$$[-2] = [p-2]$$
$$[-i] = [p-1]$$
$$...$$
$$[-{p-1\over 2}] = [p -{p-1\over 2}]$$
The last element here is the first unit in the second half of $S$. Thus, if $S$ is a CSU, $S'$ must be as well.  



***THE END***

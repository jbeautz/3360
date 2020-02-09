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

19,38,57,76, 95, 114, 133
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
Hence, $a \cong b (mod{m\over(r,m)})$

###Exercise 5F-44








***THE END***

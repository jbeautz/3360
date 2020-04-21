<font color = white>  

John Beautz  
jpb375  

#MATH 3360 Homework 9  

###Exercise 14A-5
(i) By the Root Theorem:  
In $\mathbb Q[x]$
$$f(3) = 3^4 + 3^3 + 3 + 4 \neq 0$$
Thus, 3 is not a root, and $x-3$ does not divide the function.  

In $\mathbb Z[x]$  
$$f(3) = 3^4 + 3^3 + 3 + 4 \neq 0$$
Thus, 3 is not a root, and $x-3$ does not divide the funtion.  

(ii) In $\mathbb Z_m[x]$
$$f(3) = [3^4 + 3^3 + 3 + 4]_ m$$
$$f(3) = [115]_ m = 0$$
Thus, $x-3$ divides in $\mathbb Z_m[x]$ if $m|115$. The prime factorization of 115 is $5\times 23$. So, $m\in\{5,23,115\}$.  

###Exercise 14A-6
$$[x^p]_ p = [x]_ p$$
By Fermat's Theorem;
So $x^p = x$ on $\mathbb{Z_p[x]}$  

In $\mathbb Z_3$  
$x^3 = x$ because $3$ is prime. So $x^3+3=x$  
By the root theorem, $x$ divides $x^5+x^3+x^2-9$ if $0$ is a root of the polynomial in $\mathbb Z_3[x]$.  
$$[(-3)^5 + (-3)^3 + (-3)^2 -9 ]_ 3= 0$$
Thus, $x^3 + 3$ divides for $m=3$.  

In $\mathbb Z_2$  
$x^3 + 3 = x+1 = x^5+x^3+x^2-9$ for $x = 0$ and $x=1$ so they divide on the ring.

###Exercise 14A-11
Let $f_n(x)$ be a polynomial on the commutative ring $\mathbb Z_m$ where $m$ is the product of the first $n$ prime numbers.

Note $f_n(x)=\prod_{i=0}^{n-1} (x-i)$ is a polynomial with $n$ distinct roots with coefficents in $\mathbb Z_m$.  

##Exercise 14A-13
$x^2 - 1$ has two roots because it is of degree 2.  

$x=1$ is a root because $1\in \mathbb Z_p$ and $1^2-1=0$.  
There can only be one other root. Lets assume its $x=p-1$.
$$(p-1)(p-1) - 1 = p^2 - 2p + 1 -1$$
In $\mathbb Z_p$, multiples of $p$ are equivalent to $0$ (mod p).  Thus
$$(p-1)(p-1) - 1 = 0$$

Let $a\in \mathbb Z_p$ such that $1<a<p-1$.  
Let $b\in \mathbb Z_p$ be the inverse modulo $p$ of $a$.  
Suppose $a = b$.  
$$a^2 = 1$$
Then, $a$ is a root of the polynomial $x^2-1$ in $\mathbb Z_p$. This is a contradiction because $a\neq 1$ and $a\neq p-1$. Thus, $a\neq b$.  

$$(p-1)!\cong (p-1) (mod p)$$
We know $\mathbb{Z}_p$ is a field so each element has an inverse modulo $p$. These inverse must be distinct for $x\neq p-1$ and $x\neq 1$ as shown above. The factorial will multiply every element in the field, so every pair of distinct inverses will be multiplied. We can rearrange the multiplication so it becomes obvious that inverses are adjacent and all values less than $p-1$ will cancel each other out.  
$$(p-1)! = (p-1)(a_1)(b_1)(a_2)(b_2)...(1) (mod p)$$
$$(p-1)! = (p-1)(1)(1)...(1) (mod p)$$
$$(p-1)! = (p-1) (mod p)$$

Thus, Wilson's Theorem is proved.  

###Exercise 14B-15
$$x^3 + 2x^2 + 3x + 2 = (x^2 − x + 4)(x)+(2x  + 2)$$
$$x^2 - x + 4 = (2x+2)(x) + (2x^2 + 4)$$
$$2x + 2 = (2x^2 + 4)(0)+(2x + 2)$$
$$2x^2+4 = (2x+2)(x) + (x + 1)$$
$$(2x+2) = 2(x+1) + 0$$
So, $x+1$ is the GCD of the polynomials in $\mathbb Z_3[x]$.  

###Exercise 14B-20
$$\pmatrix{1& 0&    x^3 + x^2 + x + 2\\0& 1&    x^3 + 2x^2 + 2}$$

$$\pmatrix{1& 0&    x^3 + x^2 + x + 2\\2& 1&    x^2 + 2x}$$

$$\pmatrix{1+x& 2x&    2x^2 + x + 2\\2  & 1 &    x^2 + 2x}$$

$$\pmatrix{x& 2x+1&    2\\2& 1   &    x^2 + 2x}$$

$$\pmatrix{x    & 2x+1         &    2\\x^3+2& 2x^3+x^2+1   &    2x}$$

$$\pmatrix{x        & 2x+1       &    2\\x^3+x^2+2& 2x^3+x+1   &    0}$$

$$\pmatrix{2x        & x+2       &    1\\ x^3+x^2+2& 2x^3+x+1   &    0}$$

So from the top row of the matrix,
$$(2x)(x^3+x^2+x+2)+(x+2)(x^3+2x^2+2)=1$$

###Exercise 14B-26
$$\pmatrix{1 & 0 &    x^2 - 3x + 2\\0 & 1 &    x^2 + x  + 1   }$$

$$\pmatrix{1 & -1 &    -4x + 1\\4 & 4  &    4x^2 + 4x  + 4  }$$

$$\pmatrix{1   & -1   &    -4x + 1\\4+x & 4-x  &     5x  + 4   }$$

$$\pmatrix{1   & -1     & -4x + 1\\5+x & 5-x    &  x  + 5}$$

$$\pmatrix{1     & -1       & -4x + 1\\21+4x & 19-4x    &  21}$$

$$\pmatrix{4x^2+21x+5 & -4x^2+19x-5    &  x+5\\21+4x      & 19-4x          &  21}$$

$$\pmatrix{4x^2+21x+5 & -4x^2+19x-5    &  x+5\\21+4x      & 19-4x          &  21}$$

$$\pmatrix{21(4x^2+21x+5) & 21(-4x^2+19x-5)    &  21x+105\\21+4x          & 19-4x              &  21}$$

$$\pmatrix{21(4x^2+21x+5)-4x^2-21x & 21(-4x^2+19x-5)+4x^2-19    &  105\\21+4x          & 19-4x                               &  21}$$

$$\pmatrix{21(4x^2+21x+5)-4x^2-21x & 21(-4x^2+19x-5)+4x^2-19    &  0\\1+{4\over 21}x          & {19\over 21}-{4\over 21}x                               &  1}$$

Thus, accoring to the bottom row:
$$r(x)= {19\over 21}-{4\over 21}x$$
$$s(x)= 1+{4\over 21}x$$
$$d(x) = 1$$


###Exercise 14C-44
Note: $x^p = x (mod p)$, so $x^p-x = 0\in \mathbb F_p$ by Fermat.  
$x-i$ is irreducible in any modular field.
$$\prod_{i=0}^{p-1} (x-i) = 0$$
$x\in \mathbb F_p$ so $1\leq x\leq p$. Hence for $(x-i)=0$ for some $i\in \mathbb F_p$.  
Thus, for any $x$ in the field, one of the irreducible elements of the factorization must be 0, because there is a distinct one for each element of the field.  
$\prod_{i=0}^{p-1} (x-i) = 0$ has degree $p$, same as $x^p-x$, so it must be a complete factorization in $\mathbb F_p$.  


###Exercise 14C-46
By the root theorem, the polynomial is irreducible if it never
$$x$$
$$x+1$$

$$x^2+x+1$$

$$x^3+x+1$$
$$x^3+x^2+1$$

$$x^4+x^3+x^2+x+1$$
$$x^4+x^3+1$$
$$x^4+x+1$$
A polynomial $p(x)$ is irreducible if it does not have linear factors. Therefore, it suffices to show that p(0)=p(1)=1. Using this, we add higher degrees and test for divisibility of lower degree polynomials.  

###Exercise 14C-47(iii)  
$$x^7 + x^6 + x^4 + 1$$
-1 is a root so, by the root theorem, $x+1$ is a root.  

Using polynomial long division, we find
$$x^6+x^3+x^2+x$$
Is the other factor.  

Splitting this we have
$$x^7 + x^6 + x^4 + 1=(x+1)(x^2+x+1)(x^4+x^3+1)$$

###Exercise 14C-48(ii)  
$$x^{10}-1=(x^5+1)^2$$
By difference of squares in $\mathbb F_2$.

$1$ is a root so $x+1$ must be a factor.  
$x^5+1 = (x+1)(x^4+x^3+x^2+x+1)$$
So,
$$x^{10}-1 = (x+1)^2(x^4+x^3+x^2+x+1)^2$$












***THE END***

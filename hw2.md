<font color = "white">  

Jack Beautz  
jpb375  

#MATH 3360 Homework 2

###Exercise 4A-3
#####If $a$ and $b$ are coprime then no prime number divides both $a$ and $b$

$a,b$ are coprime, so $(a, b) = 1$.
Assume there exists a shared prime divisor $p\in \mathbb{P}$ such that $p|a$ and $p|b$.

$(a, b) = 1$ so $p\leq 1$. But this implies $p=1$ since primes must be nonzero and positive.

By convention, $1$ has no prime divisors. Hence $a,b$ have no shared prime divisors.

---
#####If no prime number divides both $a$ and $b$ then $a$ and $b$ are coprime.


The fundamental theorem of arithmetic states if $n>1$, then it would have a prime factorization and therefore $a, b$ would share a prime factor.

There is no number $n>1$ such that $n|a$ and $n|b$.
Hence, the only common divisor is $1$.
Therefore, $a,b$ are coprime by definition.

---
Since, the statement holds in both directions, the statement must be true.   

$a$ and $b$ are coprime if and only if no prime number divides both $a$ and $b$.

###Excercise 4B-10
Prove that if p is a prime number, then $\sqrt{p}$ is irrational.

Assume $\sqrt{p}$ is rational.  

If $\sqrt{p}\in\mathbb{Q}$, then $\sqrt p = {a\over b}$ for some $a,b\in \mathbb{Z}$.  
Rearranging this expression we find  
$$b^2 p = a^2$$

The fundamental theorem of arithmetic guarantees a prime factorization of all integers greater than 1. Therefore, $a,b$ both have prime factorizations.

Let $p^d, p^e$ be in the prime factorization of $a,b$ respectively.  

Hence, the expression from before becomes
$$2e + 1 = 2d$$

But, the LHS will always be odd and the RHS will always be even. Hence, this equation will never hold true. The assumption is false.

###Exercise 4B-12  
(i)

Let $a$ be a cube such that $a = r^3$. The fundamental theorem of arithmetic requires all integers to have a unique prime factorization. Suppose there exists a prime factor $p^q$ of $a$ such that $q \neq 3c$. Let $p^b$ be a prime factor of $r$. Plugging in we find $p^{3c}\neq 3b$, and therefore $q = 3c \neq 3(b)$ for any $c,b$. However this is a contradiction. Hence, if $q$ is a cube the exponent of each prime factor of a is a multiple of 3.  

Let the exponent of each prime factor of $a$ be a multiple of 3.
$$a = p_1^{3m_1}...p_r^{3m_r}$$
Then, by the laws of exponents, taking the cube of both sides
$$\sqrt[3]{a} = p_1^{m_1}...p_r^{m_r}$$
Note that $p_1,...,p_r\in\mathbb{P}$ and $m_1...m_r\in\mathbb{Z}$. Hence, the cubic root of $a$ is an integer. Hence, $a$ is a cube.


(ii)

If $\sqrt[3]{a}\in\mathbb{Q}$, then $\sqrt[3]{a} = {m\over n}$ for some $m,n\in \mathbb{Z}$.  
Rearranging this expression we find  
$$n^3 a = m^3$$

The fundamental theorem of arithmetic guarantees a prime factorization of all integers greater than 1. Therefore, $m,n$ both have prime factorizations.

But cubing both sides revealed the prime factorizations of $m,n$ to be $(p_1^3 

Hence, the expression from before becomes
$$3e + 1 = 3d$$

But, it was already established that if $a$ is not a cube, $a$ must not have all exponents which are multiples of 3. Hence, the cubic root is irrational.







***THE END***

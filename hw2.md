<font color = "black">  

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

The fundamental theorem of arithmetic guarantees a prime factorization of all integers greater than 1. Therefore, $m,n,a$ all have prime factorizations.

Let $p$ be a prime factor of $m, n$ such that $p^r|m$ and $p^s|n$. Let $q$ be the exponent of $p$ in the prime factorization of $a$.

Hence, the expression from before becomes
$$3s + q = 3r$$
$$q = 3r - 3s$$
$$q = 3(r-s)$$

Hence, for all prime factors the exponent is a multiple of 3. However part (i) showed that if every prime factor takes a multiple of 3 as its exponent, $a$ is a cube.  
Therefore, the cubic root of $a$ is only rational if $a$ is a cube.  

###Exercise 4B-27  
If $(a, b)|c$ then there exists an integer $j$ such that
$$j(a,b)=c$$
If $a|bc$ then there exists an integer $k$ such that
$$ka  = bc$$

Multiply both sides of this equation by $c$
$$kac = bc^2$$
$${kaj(a,b)\over b} = c^2$$
Let $l = {kj(a,b)\over b}$. $l$ must be an integer because we know $j(a,b) = c$ and $a|bc$.  
Hence, $la = c$ and $a|c^2$.

###Exercise 4B-37  
The exponent of each prime in the factorization of the lcm is the maximum of the exponent of that prime in $a$ and the exponent of that prime in $b$.  
$$[a,b] = 6^5 7^6 8^4 9^5 10^6$$

###Exercise 5A-5
(i)
$$13\times 153 = 1989$$
Therefore $1900 = 1 mod 13$ and $2003 = 1 mod 13$.
Therefore there exists no $b\in (1900,2000)$ congruent to $1 mod 13$.  

(ii)
$$1776 mod 25 \cong 1 mod 25$$
$25\times 71 = 1775$ and $25\times 72 = 2000$ so there is not value $b\in (1900,2000)$ congruent to $1776 mod 25$.

(iii)
$$1914 mod 27 \cong 3 mod 27$$
There exists only one $b$ in the range.
$$b = 1998$$

###Exercise 5A-6
$a = 8d + 5$ and $a = 7e + 3$.  
$${8d + 5} = {7e + 3}$$
$${8d + 2} = {7e}$$
$$d = e = -2$$
Hence, $a = -11$.

###Exercise 5A-7  
Show that if m > 4 is not prime, then (m − 1)! ≡ 0 (mod m)

$(m-1)! = mk$ for some integer $k$.

Proof by Induction:  
Base Case: $m = 6$.
$$(6-1)! = (5)(4)(3)(2) \cong 0 mod 6$$
$3\times 2 = 6$ so 5! is a multiple of 6. Hence, the induction hypothesis holds for the base case.

Induction Step: $m = n$.
$$k(n-1)! = n$$
for some k.
Assume hypothesis holds true for $m<n$.
Let $n = p_1...p_r$ be the prime factorization of $n$. We know from the fundamental theorem of arithmetic this factorization exists and $p_i<n$ for all $i$ since $n$ is not prime.  
Now consider the prime factorization of $(n-1)!$. This will contain all primes $p_j<n$. Hence, (n-1)!|n$. Therefore $k$ exists and the induction hypothesis holds.

Because the base case and step case are valid in induction. The hypothesis must be true.

###Exercise 5B-15
$$7^{16} \cong 1 mod 17$$
$$7^{16} = {7^2}^{16}$$
$${7^2}^{16}\cong -2^{16} mod 17$$
$$-2^{16} mod 17 \cong {(-2)^4}^4 mod 17$$
$${(-2)^4}^4 mod 17 \cong (-1)^4 mod 17$$
$$(-1)^4 mod 17 \cong 1 mod 17$$
Hence, $7^{16} \cong 1 mod 17$.  

$$7^{546} \cong {7^2}{7^{16}}^{34} mod 17$$
$${7^2}{7^{16}}^34 mod 17 \cong  {7^2}{1^34} mod 17$$
$${7^2} mod 17 \cong 49 mod 17$$
$17\times 2 = 34$ Hence, the residue is $7^2-34 = 15$.  

###Exercise 5B-16
(i)
$$5^{18} mod 11\cong {5^3}^6 mod 11$$
$$125^6 mod 11\cong 4^6 mod 11$$
$${4^3}^2 mod 11\cong {64}^2 mod 11$$
$$-2^2 mod 11\cong -4 mod 11$$
$$-4 mod 11 \cong 7 mod 11$$

Hence, the least non negative residue is 7.

(iii)  
$$4^{47} mod 12\cong 64(4^{44}) mod 12$$
$$64(4^{4})^{11} mod 12\cong 64(4)^{11} mod 12$$
$$(4^4)4^{10} mod 12\cong (4)^11 mod 12$$
$$4^3(4^4)^2 mod 12\cong 4(4^4) mod 12$$
$$16 mod 12 \cong 4$$

###Exercise 5B-17
Show that 1 is the least nonnegative residue of a^6 (mod 7) for each number a,
1 ≤ a ≤ 6.

1 is the least non negative value possible so it is sufficient to check this and the fact that no $a^6$ is a multiple of 7. The sixth rooth of 7 is irrational so it can never be modulo 0 for an integer $a$.

$$a^6 - 1 = 7d$$
$$a^6 = 7d + 1$$

For $a=1$ we have equality for $d=0$.  
For $a=2$ we have equality for $d=9$.  
For $a=3$ we have equality for $d=10$.  
For $a=4$ we have equality for $d=585$.
For $a=5$ we have equality for $d=2232$.  
For $a=6$ we have equality for $d=6665$.  

Hence, 1 is the least non negative residue for all integer $a\in[1,6]$.


***THE END***

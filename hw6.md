<font color = white>  

John Beautz  
jpb375  

#MATH 3360 Homework 6

###Exercise 11A-9
Consider the powers of $(1-i)$.  
$$(1-i)^0 = 1$$
$$(1-i)^1 = (1-i)$$
$$(1-i)^2 = (-2i)$$
$$(1-i)^3= (1-i)(-2i) = (-2i - 2)$$
$$(1-i)^4 = (1-i)(1+i)(-2) = -4\cong 2 mod 3$$
$$(1-i)^5 =(1-i)(2) = (2 - 2i)$$
$$(1-i)^6 =(2)(1-i)^2 = 2i$$
$$(1-i)^7 =(1-i)(2i) = 2+2i$$
$$(1-i)^8 =2(1+i)(1-i) = 1$$

Thus, 8 is the least positive power $a$ resulting in $(1-i)^a=0$.  

$\mathbb F_9$ is a group so every element has a unique multiplicative inverse. But there are only 9 elements. Thus the 8 powers of $(1-i)$ considered above must be the set of all units.  

Consider the order of the unit $u = (1-i)^a$. We know $a\geq 8$ because we show greater powers above. Because $u^8=0$, we know $u^8b =0$ because we can factor out the 8 power so that $(u^b)(0)=0$. Thus we can find the order of each unit $u^b$ for $b\leq 7$ by multiplying $b$ by 8. So 8 divides the order of each unit.  

###Exercise 11B-10
Let G be a group with operation ∗. If G is finite, then a non-empty
subset H of G is a subgroup of G if and only if H is closed under ∗.

$H$ is a subgroup of $G$ if it satisfies  
(i) $e\in H$  
(ii) $H$ is closed under multiplication  
(iii) if $a\in H$, $a'\in H$.

First, $H$ of $G$ is a subgroup of $G$ if $H$ is closed under ∗.  
**Proof**: This implies that for finite $G$, (i) and (iii) must be satisfied if (ii) is satisfied.
Assume (iii) is satisfied. Then, let $a\in H$ exists such that $a a' = e$ for some $a'\not\in H$.
Assume (iii) is satisfied. $H$ is closed under * so $e$ must be in $H$. Thus, (i) is satisfied.  
Assume (i) is satisfied. Let $a,b,c\in H$ such that $a'\not\in H$.  
$$e = a * b * c$$
$$a' * e = a' * a * b * c$$
$$a' = b * c$$
But, $b, c\in H$ and $H$ is closed under multiplication. So, $a'\in H$.  
Thus, if (i) and (iii) are satisfied, $H$ is a proper subgroup.  

Next, $H$ is closed under ∗ if $H$ of $G$ is a subgroup.  
**Proof**: $H$ is a subgroup so by definition it must be closed under * .


###Exercise 11B-11
(a)
$$[7]^1 = [7]$$
$$[7]^2 = [11]$$
$$[7]^3 = [1]$$
$$[7]^4 = [7]$$

Thus, the cyclic group is $\{[7], [7^2], [7^3]\}$.  

(b)  
$$[12]^1 = [12]$$
$$[12]^2 = [11]$$
$$[12]^3 = [18]$$
$$[12]^4 = [7]$$
$$[12]^5 = [8]$$
$$[12]^6 = [1]$$
$$[12]^7 = [12]$$

Thus, the cyclic group is $\{[12^1],[12^2],[12^3],[12^4],[12^5],[12^6]\}$.  

$(c)$  
$$[8]^1 = [8]$$
$$[8]^2 = [7]$$
$$[8]^3 = [18]$$
$$[8]^4 = [11]$$
$$[8]^6 = [12]$$
$$[8]^7 = [1]$$
$$[8]^8 = [8]$$

Thus, the cyclic group is $\{[8]^1,[8]^2,[8]^3,[8]^4,[8]^5,[8]^6,[8]^7$.  


###Exercise 11B-13  
$$\{1,5,9,13\}$$

The above subgroup is closed under multiplication and contains the units of each member of the subgroup.  

###Exercise 11C-15
$U_19 = \{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18\}$$
Thus, $|U_19|=18$.  
(a)  
$\langle [7]\rangle = \{7,11,1\}$  
$$[1]=\{7,11,1\}$$
$$[2]=\{14,3,2\}$$
$$[3]=\{2,14,3\}$$
$$[4]=\{9,6,4\}$$
$$[5]=\{16,17,5\}$$
$$[6]=\{4,9,6\}$$
$$[7]=\{11,1,7\}$$
$$[8]=\{18,12,8\}$$
$$[9]=\{6,4,9\}$$
$$[10]=\{13,15,10\}$$
Now for every $x\in G$, $x\in C$ for some coset $C$. Thus the set of cosets is
$\{\{14,3,2\},\{9,6,4\},\{16,17,5\},\{18,12,8\},\{13,15,10\}\}$
All cosets are of cardinality 3.  
$3|18$ so Lagrange's theorem is satisfied.  

(b)  
$\langle [12]\rangle = \{12, 11, 18, 7, 8, 1\}$  
$$[1]=\{12,11,18,7,8,1\}$$
$$[2]=\{5,3,17,14,16,2\}$$
$$[3]=\{17,14,16,2,5,3\}$$
$$[4]=\{10,6,15,9,17,4\}$$
Now for every $x\in G$, $x\in C$ for some coset $C$. Thus the set of cosets is
$\{\{5,3,17,14,16,2\},\{10,6,15,9,17,4\}\}$.  
All cosets are of cardinality 6.  
$6|18$ so Lagrange's theorem is satisfied.  


$(c)$  
$\langle [5]\rangle = \{5,6,11,17,9,7,16,4,1\}$  
$$[1]=\{5,6,11,17,9,7,16,4,1\}$$
$$[2]=\{10,12,3,15,18,14,13,8,2\}$$
Now for every $x\in G$, $x\in C$ for some coset $C$. Thus the set of cosets is
$\{\{10,12,3,15,18,14,13,8,2\}\}$.  
All cosets are of cardinality 9.  
$9|18$ so Lagrange's theorem is satisfied.  

###Exercise 11F-31
$f:R\to S$ is a ring homomorphism. Thus, for $a,b\in R$ and $e$ the neutral element of $R$ and $e'$ the neutral element of $S$.  
(i) $f(e) = e'$  
(ii) $f(a)* f(b) = f(a*b)$  
This leaves only mapping of inverse elements property for $f$ to be a group homomorphism.  
$$f(a') = f(a)'$$
Where $a * a' = e$.  
$U(R),U(S)$ contain the inverses of every element in their respective sets because they are groups.  
Suppose $a,a'\in R$ such that $f(a')\neq f(a)'$.  
Then,
$$f(a') * f(a) \neq f(a)' * f(a)$$
Using (ii) we combine the LHS
$$f(a' * a) \neq f(a)' * f(a)$$
$$f(e) \neq f(a)' * f(a)$$
Using (i) the neutral element maps to the other neutral element.  
$$e' \neq e'$$
Thus, we have arrived at a contradiction.  
So $f(a') = f(a)'$ must be true.  

$f:U(R)\to U(S)$ is a group homomorphism.  

###Exercise 11F-33
(a)
$L_{[2]}:\mathbb{Z}_{10}\to\mathbb{Z}_{10}$
$$Ker(L_{[2]}) = \{0,5\}$$
Because $[2\times 0]_ {10} = [2\times 5]_ {10} = [0]_ {10}$.  

(b)$L_{[3]}:\mathbb{Z}_{11}\to\mathbb{Z}_{11}$  
$$Ker(L_{[3]}) = \{0\}$$
Because $[3\times 0]_ {11} = [0]_ {11}$.  

$(c)$
$L_{[4]}:\mathbb{Z}_{12}\to\mathbb{Z}_{12}$  
$$Ker(L_{[4]}) = \{0,3,6,9\}$$
Because $[4\times 0]_ {12} = [4\times 3]_ {12}= [4\times 6]_ {12}=[4\times 9]_ {12}=[0]_ {12}$.


###Exercise 9A-2
$U_9 = \{1,2,4,5,7,8\}$  
$[1^1] = [1]$ so $O(1)=1$.  
$[2^6] = [1]$ so $O(2)=6$.  
$[4^3] = [1]$ so $O(4)=3$.  
$[5^5] = [1]$ so $O(5)=5$.  
$[7^3] = [1]$ so $O(7)=3$.  
$[8^2] = [1]$ so $O(8)=2$.  

###Exercise 9A-4
$\mathbb Z_{11}^{\times}$
$|G|=10$ so its either 1,2,5,10 by Lagrange.  
$[2^{10}]= [1]$ so $O(2)=10$.  
$[3^5] = [1]$ so $O(3)=5$.  
$[4^5] = [1]$ so $O(4)=5$.  
$[5^5] = [1]$ so $O(5)=5$.  
$[6^{10}] =[1]$ so $O(6)=10$.  
$[7^{10}] =[1]$ so $O(7)=10$.  
$[8^{10}] =[1]$ so $O(8)=10$.  
$[9^5] =[1]$ so $O(9)=5$.  
$[10^2] = [1]$ so $O(10)=2$.  

###Exercise 9A-13
By Proposition 3 in text,
$$O(3^26) = {162\over (162,26)}$$
$$O(3^26) = {162\over 2}$$
$$O(3^26) = {81}$$
Similarly,
$$O(3^27) = {162\over (162,27)}$$
$$O(3^27) = {162\over 27}$$
$$O(3^27) = 6$$




###Exercise 9B-19
$$2^9 (mod11)\cong 2(2^4)^2 (mod 11)$$
$$2(5)^2 (mod 11)\cong 6 (mod 11)$$

$$[6\times 2] = [12] = [1]$$
So $2^9$ is the inverse of $2$ mod 11.  

###Exercise 9B-20
The order must divide 22. So $O(3)\in \{1,2,11,22\}$.  

$$[3^1] = [3]$$
$$[3^2] = [9]$$
$$[3^{11}] = [1]$$
So $O(3) = 11$.  

###Exercise 9B-27
Induction:  
Base Case: $n=1$  
$$1 = 1^5/5 + 1^3/3 + 7/15$$

Step Case: If $p$ is prime and $a$ is not divisible by $p$, then the order of a modulo
$p$ divides $p − 1$.
In this case we need $a = {n^5\over 5} + {n^3\over 3} + {7n\over 15}$ to divide 1 evenly. 1 is prime so if $1\not| a$, the order of $[a]_ p |(p-1)$. Let $k=O(a)$. But $a^k = 0 mod (1)$ for all $k$ because there is no other option in $\mathbb{Z}_1$. Hence, the order does not divide $p-1$ and $a$ must divide $p$. Thus, $a$ is an integer for any input $n$.  


###Exercise 9B-36
$O(2) = 9$ in $\mathbb Z_{511}$.  
$$2^9 \cong 1 (mod 511)$$
$$(2^3)^3\cong 1 (mod 511)$$
$$(8)^3 \cong 1 (mod 511)$$
$$512 \cong 1 (mod 511)$$
$$1\cong 1 (mod 511)$$

Proposition 5 in the text states if 511 is prime and 2 is not divisible by 511, then the order of a modulo
p, which is 9, must divide 510.  
511 is an odd number so 2 is not divisible by 511. Assuming 511 is prime, 9|510.
But $510/9= 170/3$ which is not an integer. Hence, 511 is composite.  

###Exercise 9C-49
$$[5]_ {18} \times [11]_ {18} = [55]_ {18} = [1]_ {18}$$
$$[5^2] = [25] = [7]$$
$$[5^3] = [35] = [17]$$
$$[5^4] = [85] = [13]$$
$$[5^5] = [65] = [11]$$

Hence, $[5^5]$ is the inverse of [5] in $\mathbb Z_{18}$

###Exercise 9C-50
$$a^f \cong a (mod m)$$
If $f\cong 1 (mod \phi(m))$, then $1 + k\phi(m) = f$
$$a^{1 + k\phi(m)} \cong a (mod m)$$
$$(a)a^{k\phi(m)} \cong a (mod m)$$
$$a^{k\phi(m)} \cong 1 (mod m)$$
$$(a^{\phi(m)})^k \cong 1 (mod m)$$
We know $k|(|G|)$ because of Lagrange's theorem. It follows that $a^{|G|} = 1$.  
By definition, $|G| = \phi(m)$ so
$$(a^{\phi(m)})^k \cong 1 (mod m)$$
$$(1)^k \cong 1 (mod m)$$
$$1 \cong 1 (mod m)$$





**THE END**

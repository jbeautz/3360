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




**THE END**

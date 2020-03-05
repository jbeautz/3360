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
(i) $H$ is closed under multiplication  
(ii) if $a\in H$, $a'\in H$.

Hence, if (ii) is always true for subsets of finite groups, the above statement holds.  

Suppose there exists $a\in H$ such that $a' \in G-H$. $G$ is finite so the subset $G-H$ must be finite as well.  

$H$ is a finite group so each element should have a finite order. Consider $a\in H$ such that $O(a) = n$. Then

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




**THE END**

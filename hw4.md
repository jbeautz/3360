<font color = "black">  

Jack Beautz  
jpb375  

#MATH 3360 Homework 4

###Exercise 7A-15
$\mathbb Z_6$  
$(0,6)\neq 1$ so there is no inverse.  
1 is the inverse of 1.  
$(2,6)\neq 1$ so there is no inverse.  
$(3,6)\neq 1$ so there is no inverse.  
$(4,6)\neq 1$ so there is no inverse.
5 is the inverse of 5.  

$\mathbb Z_7$  
$(0,7)\neq 1$ so there is no inverse.  
1 is the inverse of 1.  
4 is the inverse of 2.  
5 is the inverse of 3.  
2 is the inverse of 4.  
3 is the inverse of 5.  
6 is the inverse of 6.  

$\mathbb Z_8$  
$(0,8)\neq 1$ so there is no inverse.  
1 is the inverse of 1.  
$(2,8)\neq 1$ so there is no inverse.  
3 is the inverse of 3.  
$(4,8)\neq 1$ so there is no inverse.  
5 is the inverse of 5.  
$(6,8)\neq 1$ so there is no inverse.  
7 is the inverse of 7.  

###Exercise 7C-23  
$a$ is a zero divisor such that for some $b\in R$, $ab=0$.  
Let $x = by$ for any $y\in R$.  
$$ax = 0$$
$$a(by)=0$$
$(R,\cdot)$ is a monoid so it has associativity.  
$$(ab)y=0$$
$$0y=0$$
Rings also must have the absorption property. Hence,
$$0=0$$

$y$ can be any element in $R$. Therefore, the equation has multiple solutions.  

###Exercise 7C-30  
$$2\times 9=0$$
$$3\times 6=0$$
$$4\times 9=0$$
$$6\times 3=0$$
$$8\times 9=0$$
$$9\times 2=0$$
$$10\times 9=0$$
$$12\times 9=0$$
$$14\times 9=0$$
$$15\times 6=0$$
$$16\times 9=0$$


###Exercise 7C-32  
The prime factorization of $365$ is $5\times73$.  
$[53]$  
$53$ is coprime with $365$ so there is an inverse.  
$$[53\times 62] = [3286]= [1]$$

$[73]$  
$(73,365) = 73$ so there is no inverse.   

$[93]$  
$93$ is coprime with $365$ so there is an inverse.  
$$[93\times 157]=[14601]=[1]$$

$[113]$  
$113$ is coprime with $365$ so there is an inverse.  
$$[113\times 42]=[4746]=[1]$$

###Exercise 7C-35(ii)
$$0+0i$$
$$0+i$$
$$0+2i$$
$$1+0i$$
$$1+i$$
$$1+2i$$
$$2+0i$$
$$2+i$$
$$2+2i$$

###Exercise 7C-35(ii)
$$(0+i)(0+2i) = 1$$
$$(0+2i)(0+i) = 1$$
$$(1+0i)(1+0i) = 1$$
$$(1+i)(2+i) = 1$$
$$(1+2i)(2+2i) = 1$$
$$(2+0i)(2+0i)=1$$
$$(2+i)(1+2i)=1$$
$$(2+2i)(1+2i)=1$$

###Exercise 7C-36
$$0+0i$$
$$0+1i$$
$$1+0i$$
$$1+i$$

$$(0+1i)(0+1i) = 1$$
$$(1+0i)(1+0i) = 1$$
Note: $0+0i$ and $1+i$ do not have inverses in $\mathbb{Z}_2$.  

###Exercise 7D-40
$$g(f): R\to T$$
There are two properties which need to be satisfied.  
(i)$g(f(e))=e'$ where $e$ is the neutral element of $R$ and $e'$ is the neutral element of $T$.  
(ii)$g(f(a*b))=g(f(a))* g(f(b))$ $\forall a,b\in R$.  

First prove (i).  
$f$ is a homomorphisms so $f(e) = e''$ where $e''$ is the neutral element in $S$. $g$ is a homomorphism so we know $g(e'') = e'$. Therefore, $e' = g(e'') = g(f(e))$.  

Next prove (ii).  
$f$ is a homomorphism so $f(a*b)=f(a)* f(b)$. $g$ is a homomorphism so $g(f(a)* f(b)) = g(f(a))* g(f(b))$.  

Therefore the composite function $g(f(r))$ is a homomorphism.  

###Exercise 7D-42
Using the same two properties from the above question.  
(i)$g(f(e))=e'$ where $e$ is the neutral element of $R$ and $e'$ is the neutral element of $T$.  
(ii)$g(f(a*b))=g(f(a))* g(f(b))$ $\forall a,b\in R$.  

First prove (i).  
$1$ is the neutral element of $R$. $f(1) = \pmatrix{1&0\\0&1}$.  
This is the identity matrix. Thus any matrix multiplied by this matrix in either direction is the same matrix.  

Next prove (ii).  
$$f(a*b) = \pmatrix{a*b&0\\0&a*b}$$
$$f(a)* f(b) = \pmatrix{a&0\\0&a}\pmatrix{b&0\\0&b}$$
$$f(a)* f(b) = \pmatrix{a*b&0\\0&a*b}$$
Thus,
$$f(a*b) = f(a)* f(b)$$

The function $f$ is a homomorphism.  












***THE END***

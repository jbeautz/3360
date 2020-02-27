<font color = white>

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

Hence, by CRT $x = 7(21)(1) + 1(10)(-2)$
$$x\cong 127 (mod 210)$$

Finally we have a system of two congruences.  
$$x\cong 127 (mod 210)$$
$$x\cong 1 (mod 6)$$
$(210, 6) = 6$ and $6|(210-6)$ so there is a solution.  
Let $m' = 35$ and $n' = 1$.  

By Bezout $35(0) + 1(1) = 1$.  

Hence, by CRT $x = 1(35)(0) + 127(1)(1)$.  
$$x\cong 127 mod (210)$$
By Bezout $35(0) + 1(1) = 1$.  

Hence, by CRT $x = 1(35)(0) + 127(1)(1)$.  
$$x\cong 1 mod (210)$$
Using the EEA
$$\pmatrix{1&0\\0&1}\pmatrix{\alpha\\\beta} = \pmatrix{127\\35}$$
$$\pmatrix{1&-3\\0&1}\pmatrix{\alpha\\\beta} = \pmatrix{22\\35}$$
$$\pmatrix{1&-3\\-1&4}\pmatrix{\alpha\\\beta} = \pmatrix{22\\13}$$
$$\pmatrix{2&-7\\-1&4}\pmatrix{\alpha\\\beta} = \pmatrix{9\\13}$$
$$\pmatrix{2&-7\\-3&11}\pmatrix{\alpha\\\beta} = \pmatrix{9\\4}$$
$$\pmatrix{8&-29\\-3&11}\pmatrix{\alpha\\\beta} = \pmatrix{1\\4}$$

Hence







**THE END**

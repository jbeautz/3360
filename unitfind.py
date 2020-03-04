x = 301
Need = False
while (Need==False & x <1000):
    x = x+1
    Need = ((x-1)%2==0)&((x-1)%3==0)&((x-1)%4==0)&((x-1)%5==0)&((x-1)%6==0)&(x%7==0)
    print(Need)
    print(x)


print(x)

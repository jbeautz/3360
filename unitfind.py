i = 0
n=113

while (n*i-1)%365 != 0:
    i=i+1
    print(i)

print("Found it:", i)
print(i, "times ", n, "equals ", i*n)

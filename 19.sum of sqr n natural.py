def sumsqr(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i)
    return sum
print(sumsqr(4))
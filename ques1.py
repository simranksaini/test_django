def power(base, exp):
    if(exp == 0):
        return(1)
    if(exp == 1):
        return(base)
    if(exp != 1):
        return(base*power(base, exp-1))

def series(x, n):
    if(x==0):
        return
    sum = 0.0;
    for i in range(1,n+1):
        sum+=1.0/power(x,i)
    print(sum)

base=3
exp=2
series(base, exp)

def series(n):
    for i in range(1,n+1):
        if(i%2==0):
            print(i*i-1, end=",")
        elif(i%2!=0):
            print(i*i+1, end=",")

series(9)

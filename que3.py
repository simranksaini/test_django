def equation(x,y,a,b):
    ans = ((x+(1/y))**a)*((x-(1/y))**b)
    return ans

x=3
y=4
a=2
b=1
numerator = equation(x,y,a,b)
denominator = equation(y,x,a,b)
answer=numerator/denominator
print(answer)

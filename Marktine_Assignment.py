x=int(input())
y=int(input())
def intermediate_stations(x,y):
    n=x-y+1
    r=y
    num=1
    den=1
    while r>=1:
        den*=r
        r=r-1
    for i in range(y):
        num*=n
        n=n-1
    
    result=num/den
    return result
if(x-y+1>=y):
    output=intermediate_stations(x,y)
    print(output)
else:
    print("Not Possible")
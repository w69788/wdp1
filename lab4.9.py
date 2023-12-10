n=int(input("podaj który wyraz ciągu chcesz otrzymać"))
n=n+1
def ciong(n):
    if n<=0:
        return("????")
    elif n==1:
        return(0)
    elif n==2:
        return(1)
    else:
        return ciong(n-1)+ciong(n-2)
print(ciong(n))

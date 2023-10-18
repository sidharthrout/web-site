n=int(input("Enter The number of total coin"))
l=[3,4,5,6]
d={}
c=0
for i in range(n+1):
    if 0.25*i+0.5*(n-i) in l:
        d[c]=[0.25*i+0.5*(n-i),i,n-i]
        c+=1
print(d)


1. Pascal's triangle
n=int(input())
for i in range(1,n+1):
    for j in range(0,n-i+1):
        print(' ',end='')
    a=1
    for j in range(1,i+1):
        print(' ',a,sep='',end='')
        a=a*(i-j)//j
    print()

2.spiral matrix
def spiral(a,b,c):
    d=0
    e=0
    while (d<a and e<b):
        for i in range(e,b):
            print(c[d][i],end=" ")
        d+=1
        for i in range(d,a):
            print(c[i][b-1],end=" ")
        b -= 1
        if (d<a):
            for i in range(b-1,(e-1),-1):
                print(c[a-1][i],end=" ")
            a-=1
        if (e<b):
            for i in range(a-1,d-1,-1):
                print(c[i][e],end=" ")
            e +=1
a=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]

spiral(4,4,a)
#



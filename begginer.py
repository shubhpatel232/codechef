#begginer

#1 atm

x,y=input().split()
x=int(x)
y=float(y)
if x%5==0 and x+0.5<=y:
    y=y-x-0.5
    print("%.2f"%y)
else:
    print("%.2f"%y)


#2 enormous input test

n,k=input().split()
n=int(n)
k=int(k)
a=[]
for i in range(n):
    b=int(input())
    if b%k==0:
        a.append(b)
print(len(a))
    

#3 add two numbers

a = int(input())
for i in range(a):
	x,y=input().split()
	x=int(x)
	y=int(y)
	ans = x + y
	print(ans)

#4 number mirror

n=int(input())
print(n)


#5 sum of digits

t=int(input())
sum=0
for i in range(t):
    a=int(input())
    for j in str(a):
        sum=sum+int(j)
    print(sum)
    sum=0

#6 find remainder

T=int(input())
for i in range(T):
    A,B=input().split()
    A=int(A)
    B=int(B)
    c=A%B
    print(c)

#7 first and last digit

T=int(input())
for i in range(T):
    N=input()
    a=len(N)
    sum=int(N[0])+int(N[a-1])
    print(sum)

#8 small factorials

T=int(input())
for i in range(T):
    n=int(input())
    mul=n
    while n-1>0:
        mul=mul*(n-1)
        n=n-1
    print(mul)

#9 turbo sort

t=int(input())
l=[]
for i in range(t):
    a=int(input())
    l.append(a)
for i in sorted(l):
    print(i)

#10 lucky four

T=int(input())
for i in range(T):
    a=input()
    count=0
    for j in a:
        if j=='4':
            count=count+1
    print(count)
    


#11 reverse the number

T=int(input())
for i in range(T):
    N=input()
    print(int(N[::-1]))


#12 findin square root

import math
T=int(input())
for i in range(T):
    N=int(input())
    a=math.sqrt(N)
    print(int(a))


#13 second largest

T=int(input())
for i in range(T):
    A,B,C=input().split()
    A=int(A)
    B=int(B)
    C=int(C)
    if A>B and A<C or A<B and A>C:
        print(A)
    elif B>A and B<C or B<A and B>C:
        print(B)
    else:
        print(C)


#14 helping chef

T=int(input())
for i in range(T):
    a=int(input())
    if a<10:
        print("Thanks for helping Chef!")
    else:
        print(-1)

#15 chef and opreators

T=int(input())
for i in range(T):
    A,B=input().split()
    A=int(A)
    B=int(B)
    if A>B:
        print(">")
    elif A<B:
        print("<")
    else:
        print("=")

#16 chef and remissness

T=int(input())
for i in range(T):
    A,B=input().split()
    A=int(A)
    B=int(B)
    print(max(A,B),A+B)


#17 valid triangle

T=int(input())
for i in range(T):
    A,B,C=map(int,input().split())
    if A+B+C==180:
        print("YES")
    else:
        print("NO")


#18 decrement or increment

N=int(input())
if N%4==0:
    N+=1
else:
    N-=1
print(N)




            



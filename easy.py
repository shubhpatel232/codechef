# EASY


#1 life the universe and everything

while True:
    a=int(input())
    if a==42:
        break
    else:
        print(a)

#2 ciel and a-b problem

A,B=input().split()
A=int(A)
B=int(B)
C=A-B
if int(C%10)==9:
    C=C-1
else:
    C=C+1
print(C)

#3 racing horses

T=int(input())
for i in range(T):
    N=int(input())
    a=list(map(int,input().split()))
    a.sort()
    diff=max(a)
    for i in range(N-1):
        if diff>(a[i+1]-a[i]):
            diff=a[i+1]-a[i]
    print(diff)


#4 uncle johny

T=int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    k=int(input())
    pos=A[k-1]
    A.sort()
    print(A.index(pos)+1)

#5 chef and notebooks

T=int(input())
for i in range(T):
    X,Y,K,N=map(int,input().split())
    val=0
    for i in range(N):
        P,C=map(int,input().split())
        if K>=C and X-Y-P<=0:
            val=1
    if val==1:
        print("LuckyChef")
    else:
        print("UnluckyChef")


#6 count substrings

T=int(input())
for i in  range(T):
    n=int(input())
    l=input()
    l2=[]
    for i in l:
        if i=='1':
            l2.append(i)
    a=len(l2)
    b=a*(a+1)//2
    print(b)


#7 jewels and stones

T=int(input())
for i in range(T):
    J=input()
    S=input()
    count=0
    for i in S:
        if i in J:
            count+=1
    print(count)


#8 chef and feedback

T=int(input())
for i in range(T):
    a=input()
    if "010" in a or "101" in a:
        print("Good")
    else:
        print("Bad")

#9 splitting candies

T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    if K==0:
        print(0,N)
    else:
        students=N//K
        teacher=N%K
        print(students,teacher)

#10 counting pretty numbers

T=int(input())
for i in range(T):
    L,R=map(int,input().split())
    count=0
    for i in range(L,R+1):
        if str(i).endswith('2') or str(i).endswith('3') or str(i).endswith('9'):
            count+=1
    print(count)

#11 copy paste

T=int(input())
for i in range(T):
    N=int(input())
    a=list(map(int,input().split()))
    b=set(a)
    print(len(b))

#12 processing a string

T=int(input())
for i in range(T):
    a=input()
    l=[]
    for i in a:
        if i.isnumeric():
            l.append(int(i))
    print(sum(l))

# July Challenge 2021 Division 3


#1 maximum production

T=int(input())
for i in range(T):
    d,x,y,z=map(int,input().split())
    f=7*x
    s=d*y+(7-d)*z
    if f>s:
        print(f)
    else:
        print(s)


#2 relativity

T=int(input())
for i in range(T):
    g,c=map(int,input().split())
    print(int((c*c)/(2*g)))

#3 XxOoRr


import math
T = int(input())
for i in range(T):
    N,M = map(int, input().split())
    l = list(map(int, input().split()))
    p = 0
    s = 0
    while (l.count(0) != len(l)) :
        li = [i for i in range(len(l)) if (int(l[i]/(math.pow(2,p))))%2 != 0]
        if li != []:
            s = s + int(len(li) / M) + (len(li) % M > 0)
            for k in li:
                l[k] = l[k]^(int(math.pow(2, p)))
        p += 1
    print(s)
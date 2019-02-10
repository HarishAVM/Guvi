h,a=map(str,input().split())
c=[]
d=[]
for i in range(0,len(h)):
    m=h.count(h[i])
    n=a.count(a[i])
    c.append(m)
    d.append(n)
if(c==d):
    print("yes")
else:
    print("no")

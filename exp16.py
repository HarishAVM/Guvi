h,a=raw_input("").split()
h=int(h)
a=int(a)
for i in range(h+1,a):
   if i > 1:
       for r in range(2,i):
           if (i % r) == 0:
               break
       else:
           print(i)

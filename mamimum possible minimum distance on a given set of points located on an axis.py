import copy
def rec(x,k,l,c):
 i=0
 if(k>0):
  for i in range(len(x)):
   l.append(x[i])
   c=rec(x[i+1:],k-1,l,c)
   l.pop()
  return c
 else:
  t=[]
  for m in range(0,len(l)):
   for n in l[m+1:]:
    t.append(abs(l[m]-n))
  c=max(c,min(t))
  return c
def main():
 x=[1, 2, 7, 5, 11, 12]; k=3; a=0
 for i in range(len(x)-k+1):
  l=[]
  l.append(x[i])
  a=rec(x[i+1:],k-1,l,a)
 print("ans:",a)
main()

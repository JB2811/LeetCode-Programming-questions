from itertools import permutations
def is_valid_permutation(p,l):
 for i in l:
  if "<" in i:
   i=i.split("<")
   if(p.index(i[0])>p.index(i[1])):
    continue
   else:
    return False
  else:
   i=i.split(">")
   if(p.index(i[0])<p.index(i[1])):
    continue
   else:
    return False
 return True 
def LineOrdering(l):
 pe=[]
 for i in l:
  if "<" in i:
   i=i.split("<")
  else:
   i=i.split(">")
  for j in i:
   if j not in pe:
    pe.append(j)
 p=permutations(pe)
 a=[]
 for i in p:
  if(is_valid_permutation(list(i),l)):
   a.append(i)
 return len(a)
print(LineOrdering(["J>B","B<S","D>J"]))

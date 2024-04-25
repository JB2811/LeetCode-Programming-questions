def findmax(p,v,cp,nc,j,c):
 if(v[j]==0):
  v[j]=1
  p+=j
  for k in nc[j]:
   if(k not in nc[c] and v[k]==0):
    p+=findmax(0,v,cp,nc,k,c)
  return p
 else:
  return 0
def CityTraffic(s):
 cp={};nc={}
 s=s.split(" ")
 for i in s:
  t=i.split(":")
  cp.update({int(t[0]):int(t[0])})
  if("," in t[1]):
   x=[int(j) for j in t[1][1:len(t[1])-1].split(",")]
  else:
   x=[int(t[1][1:2])]
  nc.update({int(t[0]):x})
 mt={}
 for i in cp.keys():
  m=0
  for j in nc[i]:
   v=[0]*(max(cp.keys())+1)
   v[i]=1
   m=max(m,findmax(0,v,cp,nc,j,i))
   mt.update({i:m})
 return mt
print(CityTraffic("1:[5] 4:[5] 3:[5,12] 5:[1,4,3,2] 2:[5,18] 18:[2] 12:[3]"))
print(CityTraffic("1:[5] 4:[5] 3:[5] 5:[1,4,3,2] 2:[5,15,7] 7:[2,8] 8:[7,38] 15:[2] 38:[8]"))


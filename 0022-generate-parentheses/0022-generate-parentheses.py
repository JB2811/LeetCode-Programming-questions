class Solution:
 p=[]
 def tryall(self,i:int,s:str,lc:int,rc:int) -> None:
  if(lc>rc):
   pass
  elif(rc==0 and lc==0):
   self.p.append(s)
  else:
   if(lc>0):
    self.tryall(i+1,s+"(",lc-1,rc)
   if(rc>0):
    self.tryall(i+1,s+")",lc,rc-1)
    
 def generateParenthesis(self, n: int) -> List[str]:
  self.p=[]
  self.tryall(1,"(",lc=(n-1),rc=(n))
  return self.p
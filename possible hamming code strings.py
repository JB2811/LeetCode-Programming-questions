import copy
def calc(s,i,k):
 d=list(s)
 if(k>1 and i<len(s)):
  d[i]=str((int(d[i])+1)%2)
  for j in range(i+1,len(d)):
   d="".join(d)
   calc(d,j,k-1)
 elif(k==1):
  d[i]=str((int(d[i])+1)%2)
  print("".join(d))
def main():
 s=input("\nEnter bit string: ")
 k=int(input("\nEnter hamming distance: "))
 for i in range(0,len(s)):
  calc(s,i,k)
main()

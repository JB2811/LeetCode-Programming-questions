class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        l=list(word)
        n=len(l)
        c=0
        for i in range(n,4,-1):
            for j in range(0,n-i+1):
                f=1
#                print(l[j:j+i])
                for k in ['a','e','i','o','u']:
                    if(k in l[j:j+i]):
                        continue
                    else:
                        f=0
                        break
                if(f and (set(l[j:j+i])==set(['a','e','i','o','u']))):
 #                   print(c)
                    c+=1
        return c
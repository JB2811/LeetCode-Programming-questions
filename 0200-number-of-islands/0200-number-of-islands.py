class Solution:
    def isisland(self,a,check,i,j,n,m):
     r=1
     if(check[i][j]):    
        check[i][j]=0
        if(i-1>=0 and a[i-1][j] and check[i-1][j]):
            r=r&self.isisland(a,check,i-1,j,n,m)
        if(j-1>=0 and a[i][j-1] and check[i][j-1]):
            r=r&self.isisland(a,check,i,j-1,n,m)
        if(j+1<m and a[i][j+1] and check[i][j+1]):
            r=r&self.isisland(a,check,i,j+1,n,m)
        if(i+1<n and a[i+1][j] and check[i+1][j]):
            r=r&self.isisland(a,check,i+1,j,n,m)
        return r
     return 0

    def numIslands(self,a):
        n=len(a)
        m=len(a[0])
        check=[1]*(n)
        r=0
        for i in range(0,n):
            check[i]=[1]*(m)
            for j in range(0,m):
                a[i][j]=int(a[i][j])
                
        for i in range(0,n):
            for j in range(0,m):
                if(a[i][j] and check[i][j]):
                    r+=self.isisland(a,check,i,j,n,m)
        return r
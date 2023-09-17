#include<cstdlib>
class Solution {
public:
    int d[1000000000];
    int E[1000000000][100000000];
    void intialisesinglesource(int n)
    { for(int i=1;i<n;i++)
      { d[i]=10000000;}
      d[0]=0;}
    void relax(int u,int v,int w)
    { if(d[v]>max(d[u],w))
      { d[v]=max(d[u],w);}}
    int bellman(vector<vector<int>>& h)
    { int n=h.size();
      int m=h[0].size();
      int v=n*m;
      intialisesinglesource(v);
      int i,j;
      int q=0;
      for(i=0;i<n;i++)
      { for(j=0;j<m;j++)
        { if(j-1>=0)
          { E[q][q-1]=int(abs(h[i][j]-h[i][j-1]));}
          if(i-1>=0 && q-m>=0)
          { E[q][q-m]=int(abs(h[i][j]-h[i-1][j]));}
          if(j+1<m)
          { E[q][q+1]=int(abs(h[i][j]-h[i][j+1]));}
          if(i+1<n && q+m<v)
          { E[q][q+m]=int(abs(h[i][j]-h[i+1][j]));}
          q++;}}
      for(q=0;q<v;q++)
      {for(i=0;i<v;i++)
      { if(i-1>=0 && i%m!=0)
        { relax(i,i-1,E[i][i-1]);}
        if(i-m>=0)
        { relax(i,i-m,E[i][i-m]);}
        if(i+m<v)
        { relax(i,i+m,E[i][i+m]);}
        if((i+1)%m!=0)
        { relax(i,i+1,E[i][i+1]);}}}
      return d[v-1];}
    int minimumEffortPath(vector<vector<int>>& h) 
    { int a=bellman(h);
      return a;}};
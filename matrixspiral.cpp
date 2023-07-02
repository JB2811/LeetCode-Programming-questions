#include<iostream>
using namespace std;
int main()
{ int i,j,w,r,c,k,n,a[10][10];
  cout<<"r: ";
  cin>>r;
  cout<<"c: ";
  cin>>c;
  for(i=1;i<=r;i++)
  { for(j=1;j<=c;j++)
    { cin>>a[i][j];}}
  n=r*c;
  i=1; j=1; k=0; w=0;
  cout<<"\n";
  while(n>0)
  { if(j<c)
    { cout<<a[i][j]<<" ";
      j++;
      n--;}
    else if(j==c && i<=r)
    { cout<<a[i][j]<<" ";
      i++;
      n--;}
    else if(i>r)
    { i=r;
      w++;
      k++;
      j=c-1;
      while(n>0 && j>0)
      { if(j>k )
        { cout<<a[i][j]<<" ";
          j--;
          n--;}
        else if(j==k && i>w)
        { cout<<a[i][j]<<" ";
          i--;
          n--;}
        else
        { j=0;}}
      j=k+1;
      i=w+1;
      c--;
      r--;}}}

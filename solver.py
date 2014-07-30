T=[]
S=[0]*20,'QTRXadbhEIFJUVZYeijf',0
I='FBRLUD'

G=[(~i%8,i/8-4)for i in map(ord,'ouf|/[bPcU`Dkqbx-Y:(+=P4cyrh=I;-(:R6')]
R=range

def M(o,s,p):
 z=~p/2%-3;k=1
 for i,j in G[p::6]:i*=k;j*=k;o[i],o[j]=o[j]-z,o[i]+z;s[i],s[j]=s[j],s[i];k=-k

N=lambda p:sum([i<<i for i in R(4)for j in R(i)if p[j]<p[i]])

def H(i,t,s,n=0,d=()):
 if i>4:n=N(s[2-i::2]+s[7+i::2])*84+N(s[i&1::2])*6+divmod(N(s[8:]),24)[i&1]
 elif i>3:
  for j in s:l='UZifVYje'.find(j);t[l]=i;d+=(l-4,)[l<4:];n-=~i<<i;i+=l<4
  n+=N([t[j]^t[d[3]]for j in d])
 elif i>1:
  for j in s:n+=n+[j<'K',j in'QRab'][i&1]
 for j in t[13*i:][:11]:n+=j%(2+i)-n*~i
 return n

def P(i,m,t,s,l=''):
 for j in~-i,i:
  if T[j][H(j,t,s)]<m:return
 if~m<0:print l;return t,s
 for p in R(6):
  u=t[:];v=s[:]
  for n in 1,2,3:
   M(u,v,p);r=p<n%2*i or P(i,m+1,u,v,l+I[p]+`n`)
   if r>1:return r

s=raw_input().split()
o=[-(p[-1]in'UD')or p[0]in'RL'or p[1]in'UD'for p in s]
s=[chr(64+sum(1<<I.find(a)for a in x))for x in s]

for i in R(7):
 m=0;C={};T+=C,;x=[S]
 for j,k,d in x:
  h=H(i,j,k)
  for p in R(C.get(h,6)):
   C[h]=d;u=j[:];v=list(k)
   for n in i,0,i:M(u,v,p);x+=[(u[:],v[:],d-1)]*(p|1>n)
 if~i&1:
  while[]>d:d=P(i,m,o,s);m-=1
  o,s=d
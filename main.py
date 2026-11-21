import os,json,urllib.request as R
ORT=((-1,0),(1,0),(0,-1),(0,1));DIA=((-1,-1),(-1,1),(1,-1),(1,1));KOF=((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1))
V={'P':100,'N':320,'B':330,'R':500,'Q':900,'K':0}
def parse(fen):
 p=fen.split()
 return''.join('.'*int(c)if c.isdigit()else c for c in p[0]if c!='/'),p[1]=='w'
def atk(b,sq,w):
 r,f=divmod(sq,8)
 p='P'if w else'p';s=8 if w else-8
 if(r<7 if w else r>0)and((f>0 and b[sq+s-1]==p)or(f<7 and b[sq+s+1]==p)):return 1
 n,k,l1,l2=('N','K','RQ','BQ')if w else('n','k','rq','bq')
 for ds,p in((KOF,n),(ORT+DIA,k)):
  for dr,df in ds:
   r2,f2=r+dr,f+df
   if(r2|f2)&~7==0 and b[r2*8+f2]==p:return 1
 for ds,pcs in((ORT,l1),(DIA,l2)):
  for dr,df in ds:
   r2,f2=r+dr,f+df
   while(r2|f2)&~7==0:
    x=b[r2*8+f2]
    if x!='.':
     if x in pcs:return 1
     break
    r2+=dr;f2+=df
 return 0
def chk(st,own):
 w=st[1]
 return atk(st[0],st[0].index('K'if w==own else'k'),w!=own)
def gen(st,cap=False):
 b,w=st;res=[]
 def push(i,t):
  y=b[t]
  if y=='.':
   if not cap:res.append((i,t,''))
  elif y.isupper()!=w:res.append((i,t,''))
  return y
 for i,x in enumerate(b):
  if x=='.'or x.isupper()!=w:continue
  r,f=divmod(i,8);u=x.upper()
  if u=='P':
   d=-8 if w else 8;last=1 if w else 6;t=i+d
   if b[t]=='.':
    if r==last:res.append((i,t,'q'))
    elif not cap:
     res.append((i,t,''))
     if r==(6 if w else 1)and b[i+2*d]=='.':res.append((i,i+2*d,''))
   for df in(-1,1):
    if 0<=f+df<8:
     t=i+d+df;y=b[t]
     if y!='.'and y.isupper()!=w:
      res.append((i,t,'q'if r==last else''))
  elif u in'NK':
   for dr,df in(KOF if u=='N'else ORT+DIA):
    r2,f2=r+dr,f+df
    if(r2|f2)&~7==0:push(i,r2*8+f2)
  else:
   for dr,df in(ORT if u=='R'else DIA if u=='B'else ORT+DIA):
    r2,f2=r+dr,f+df
    while(r2|f2)&~7==0:
     if push(i,r2*8+f2)!='.':break
     r2+=dr;f2+=df
 return res
def mk(st,m):
 b,w=st;f,t,pr=m;x=b[f];n=b[:f]+'.'+b[f+1:]
 y=(pr.upper()if x.isupper()else pr)if pr else x
 n=n[:t]+y+n[t+1:]
 return n,not w
def ev(st):
 b,w=st[0],st[1];sc=0
 for i,x in enumerate(b):
  if x=='.':continue
  u=x.upper();sg=1 if x.isupper()else-1;v=V[u]
  if u=='P':
   a=6-i//8 if sg>0 else i//8-1;v+=a*a*5//2
  sc+=sg*v
 return sc if w else-sc
nodes=0;BUDGET=70000;TT={}
def qs(st,a,b,ply):
 global nodes;nodes+=1
 if nodes>BUDGET:raise IndexError
 c=chk(st,1)
 if ply>12 and not c:return ev(st)
 if c:ms=gen(st)
 else:
  v=ev(st)
  if v>=b:return v
  if v>a:a=v
  ms=gen(st,1)
 nm=0
 for m in ms:
  ns=mk(st,m)
  if chk(ns,0):continue
  nm+=1;sc=-qs(ns,-b,-a,ply+1)
  if sc>=b:return sc
  if sc>a:a=sc
 return-100000+ply if c and not nm else a
def search(st,depth,a,b,ply):
 global nodes;nodes+=1
 if nodes>BUDGET:raise IndexError
 if depth<=0:return qs(st,a,b,ply)
 c=chk(st,1)
 if c:depth+=1
 ms=gen(st)
 ms.sort(key=lambda m:V.get(st[0][m[1]].upper(),0)+(900 if m[2]else 0),reverse=True)
 tm=TT.get(st)
 if tm in ms:ms.remove(tm);ms.insert(0,tm)
 best=-200000;nm=0;bmv=None
 for m in ms:
  ns=mk(st,m)
  if chk(ns,0):continue
  nm+=1;sc=-search(ns,depth-1,-b,-a,ply+1)
  if sc>best:best=sc;bmv=m
  if sc>a:
   a=sc
   if a>=b:break
 if bmv:TT[st]=bmv
 return-100000+ply if not nm and c else 0 if not nm else best
def bestmove(fen):
 global nodes;nodes=0
 st=parse(fen);ms=gen(st);bm=None;bv=-200001
 for m in ms:
  ns=mk(st,m)
  if not chk(ns,0)and-ev(ns)>bv:bv=-ev(ns);bm=m
 for d in range(40):
  try:
   a=-200000;bb=None
   for m in ms:
    ns=mk(st,m)
    if chk(ns,0):continue
    sc=-search(ns,d,-200000,-a,1)
    if sc>a:a=sc;bb=m
   if bb:bm=bb;ms.remove(bm);ms.insert(0,bm)
  except IndexError:break
 return bm
def main():
 U=os.getenv('MAKEFUN_ENV_URL')
 def post(p,o):
  return json.loads(R.urlopen(R.Request(U+p,json.dumps(o).encode(),{'Content-Type':'application/json'})).read())
 while 1:
  g=post('/game',{})
  if g.get('status')=='done':return
  while g.get('status')=='your_move':
   bm=bestmove(g['fen']);i=g['game']
   g=post('/move',{'game':i,'move':chr(97+bm[0]%8)+str(8-bm[0]//8)+chr(97+bm[1]%8)+str(8-bm[1]//8)+bm[2]})if bm else post('/resign',{'game':i})
main()

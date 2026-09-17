import sys,base64 as B,lzma as L,hashlib as H,struct as S,zlib as Z,collections as C
G=b"C4"
def ld(d):
 h=d[:80];o=80;c=[]
 while o<len(d):
  n=S.unpack('>I',d[o:o+4])[0];c.append([d[o+4:o+8],d[o+8],d[o+9],n,d[o+10:o+10+n]]);o+=14+n
 return h,c
def D(p,s,o):return b''.join(p[j::s] for j in range(s)[::1-2*o])
def I(q,s,o):
 n=len(q);out=bytearray(n);i=0
 for j in range(s)[::1-2*o]:
  for k in range(j,n,s):out[k]=q[i];i+=1
 return bytes(out)
def U(p):return bytes((b-i)&255 for i,b in enumerate(p))
def A(p):return bytes((b+i)&255 for i,b in enumerate(p))
def R(p):return p[::-1]
def Ld(p):
 out=bytearray(len(p));v=0
 for i,b in enumerate(p):out[i]=(b-v)&255;v=b
 return bytes(out)
def E(p):
 out=bytearray(len(p));a=0
 for i,b in enumerate(p):a=(a+b)&255;out[i]=a
 return bytes(out)
X=lambda p:p
TR={0:(X,X),1:(U,A),2:(A,U),3:(R,R),4:(Ld,E),5:(E,Ld)}
for i,s in enumerate((2,3,4,7)):
 TR[6+i]=(lambda p,s=s:D(p,s,0),lambda q,s=s:I(q,s,0))
 TR[10+i]=(lambda p,s=s:D(p,s,1),lambda q,s=s:I(q,s,1))
 TR[14+i]=(lambda p,s=s:I(p,s,0),lambda q,s=s:D(q,s,0))
 TR[18+i]=(lambda p,s=s:I(p,s,1),lambda q,s=s:D(q,s,1))
def u(y):
 y^=y>>18;y^=(y<<15)&0xefc60000;t=y
 for _ in range(6):t=y^((t<<7)&0x9d2c5680)
 y=t;t=y
 for _ in range(6):t=y^(t>>11)
 return t&0xffffffff
def T(y):
 y^=y>>11;y^=(y<<7)&0x9d2c5680;y^=(y<<15)&0xefc60000;y^=y>>18
 return y&0xffffffff
def mt(st,c):
 mt=list(st)+[0]*(624-len(st));out=[T(mt[i]) for i in range(624)]
 while len(out)<c:
  for i in range(624):
   y=(mt[i]&0x80000000)|(mt[(i+1)%624]&0x7fffffff)
   mt[i]=(mt[(i+397)%624]^(y>>1)^(0x9908b0df if y&1 else 0))&0xffffffff
  for i in range(624):
   if len(out)>=c:break
   out.append(T(mt[i]))
 return out
def mr(Q):
 if len(Q)<2800 or len(Q)%4:return None
 w=len(Q)//4;v=[S.unpack('<I',Q[i:i+4])[0] for i in range(0,2496,4)];st=[u(x) for x in v];p=mt(st,w)
 if all(p[i]==S.unpack('<I',Q[i*4:i*4+4])[0] for i in range(w)):return b''.join(S.pack('<I',x) for x in st)
def hr(Q):
 if len(Q)<64 or len(Q)%32:return None
 a=Q[:32]
 for j in range(1,len(Q)//32):
  b=Q[j*32:j*32+32]
  if H.sha256(a).digest()!=b:return None
  a=b
 return Q[:32]
P=251
def F(x):
 if len(x)>=2*P and x[P:]==x[:-P]:return x[:P]
def ky(ck,g):
 kt={}
 for (t,n),ix in g.items():
  a=[i for i in ix if ck[i][2]&7==1]
  if not a:continue
  b=[i for i in ix if ck[i][2]&7!=1]
  for i in a:
   for j in b:
    if ck[i][1]!=ck[j][1]:continue
    k=F(bytes(x^y for x,y in zip(ck[i][4],ck[j][4])))
    if k is not None:kt[t,n]=k;break
   if (t,n) in kt:break
 for (t,n),ix in g.items():
  if (t,n) in kt or t!=b"LOGS":continue
  a=[i for i in ix if ck[i][2]&7==1]
  if not a:continue
  h=[C.Counter() for _ in range(P)]
  for i in a:
   for q,x in enumerate(ck[i][4]):h[q%P][x]+=1
  k=bytearray(P)
  for r in range(P):
   Hh=h[r];best=None
   for c in range(256):
    s=0
    for v,f in Hh.items():
     x=v^c
     if 32<=x<127 or x in(9,10,13):s+=f
    if best is None or s>best[0]:best=s,c
   k[r]=best[1]
  kt[t,n]=bytes(k)
 return kt
def compress(i,o):
 raw=open(i,'rb').read();m=1
 try:
  d=B.b64decode(raw)
  if B.b64encode(d)!=raw:m=0;d=raw
 except:m=0;d=raw
 h,ck=ld(d);N=len(ck);g=C.defaultdict(list)
 for q,(t,e0,e1,n,p) in enumerate(ck):g[t,n].append(q)
 kt=ky(ck,g);meta=bytearray();st=bytearray()
 for t,e0,e1,n,p in ck:
  k=e1&7;K=kt.get((t,n)) if k==1 else None
  src=bytes(p[q]^K[q%P] for q in range(n)) if K else p
  cs=TR if k==3 else range(10);best=None
  for code in cs:
   Q=TR[code][0](src);r=hr(Q)
   if r is not None:best=(-1,1,code,r);break
   if t==b"MTST":
    r=mr(Q)
    if r is not None:best=(-1,2,code,r);break
   s=len(Z.compress(Q,1))
   if best is None or s<best[0]:best=(s,0,code,Q)
  method,code,data=best[1],best[2],best[3];xf=1 if K else 0
  meta+=t+bytes([e0,e1,method|(xf<<7),code])+S.pack('>I',n)
  if xf:st+=K
  st+=data
 mc=L.compress(bytes(meta),preset=9|L.PRESET_EXTREME);sc=L.compress(bytes(st),preset=9|L.PRESET_EXTREME)
 open(o,'wb').write(G+bytes([m])+h+S.pack('>I',N)+S.pack('>I',len(mc))+mc+S.pack('>I',len(sc))+sc)
def decompress(i,o):
 d=open(i,'rb').read();m=d[2];h=d[3:83];z=83
 N=S.unpack('>I',d[z:z+4])[0];z+=4
 ml=S.unpack('>I',d[z:z+4])[0];z+=4;meta=L.decompress(d[z:z+ml]);z+=ml
 sl=S.unpack('>I',d[z:z+4])[0];z+=4;st=L.decompress(d[z:z+sl]);z+=sl
 mp=sp=0;out=bytearray(h)
 for _ in range(N):
  t=meta[mp:mp+4];e0=meta[mp+4];e1=meta[mp+5];mf=meta[mp+6];code=meta[mp+7];n=S.unpack('>I',meta[mp+8:mp+12])[0];mp+=12
  method=mf&127;xf=mf>>7
  if xf:K=st[sp:sp+P];sp+=P
  if method==0:Q=st[sp:sp+n];sp+=n
  elif method==1:
   a=st[sp:sp+32];sp+=32;Q=bytearray(a)
   while len(Q)<n:a=H.sha256(a).digest();Q+=a
   Q=bytes(Q[:n])
  else:
   q=[S.unpack('<I',st[sp+4*j:sp+4*j+4])[0] for j in range(624)];sp+=2496
   Q=b''.join(S.pack('<I',x) for x in mt(q,n//4))[:n]
  src=TR[code][1](Q);p=bytes(src[j]^K[j%P] for j in range(n)) if xf else src
  out+=S.pack('>I',n)+t+bytes([e0,e1])+p+S.pack('>I',Z.crc32(t+bytes([e0,e1])+p)&0xffffffff)
 open(o,'wb').write(B.b64encode(out) if m else out)
if __name__=="__main__":_,op,i,o=sys.argv;(compress if op=="--compress" else decompress)(i,o)
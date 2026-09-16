import sys,base64,lzma,hashlib,struct,zlib
M=b"C256"
def parse(d):
 h=d[:80];c=[];o=80
 while o<len(d):
  n=int.from_bytes(d[o:o+4],"big");t=d[o+4:o+8];p=d[o+8:o+14];y=d[o+14:o+14+n]
  c.append((t,p,n,y));o+=14+n
 assert o==len(d)
 return h,c
def sp(p,n):
 d=p[-1]-p[-2];s=(p[-1]+d)&255
 return bytes((s+k*d)&255 for k in range(n-4))
def ts(p,n,y):
 if n<4:return None
 b=sp(p,n)
 return y[n-4:] if b==y[:n-4] else None
def hc(s,n):
 x=bytearray(s[4:]);h=bytes(s)
 while len(x)<n-4:
  h=hashlib.sha256(h).digest();x+=h
 return bytes(x[:n-4])
def th(p,n,y):
 if n<32:return None
 s=p[-4:]+y[:28];b=hc(s,n)
 return y[:28]+y[n-4:] if b==y[:n-4] else None
def td(y,n,e):
 if n<4:return None
 t=y[:n-4]
 for i,p in e:
  if len(p)>=n-4 and p[:n-4]==t:return i,y[n-4:]
 return None
def da(c,p,t):
 if t==1:return bytes(a^b for a,b in zip(c,p))
 if t==2:return bytes((a-b)&255 for a,b in zip(c,p))
 return bytes((b-a)&255 for a,b in zip(c,p))
def du(d,p,t):
 if t==1:return bytes(a^b for a,b in zip(d,p))
 if t==2:return bytes((a+b)&255 for a,b in zip(d,p))
 return bytes((b-a)&255 for a,b in zip(d,p))
def bd(c,p):
 L=min(len(c),len(p));b=None
 for t in(1,2,3):
  d=da(c[:L],p[:L],t)+c[L:];s=len(zlib.compress(d,1))
  if b is None or s<b[0]:b=(s,t,d)
 r=len(zlib.compress(c,1))
 return (b[1],b[2]) if b[0]<r else None
def duf(d,p,t):
 L=min(len(d),len(p))
 return du(d[:L],p[:L],t)+d[L:]
def pk(v):return struct.pack(">I",v)
def up(b,o):return struct.unpack(">I",b[o:o+4])[0]
G,S,H,D,R,C=0,1,2,3,4,5
def compress(i,o):
 raw=open(i,"rb").read();m=1
 try:
  d=base64.b64decode(raw)
  if base64.b64encode(d)!=raw:m=0;d=raw
 except Exception:m=0;d=raw
 hd,ck=parse(d);N=len(ck);et=[G]*N;es,eh,ed,ex=[],[],[],{}
 for i,(t,p,n,y) in enumerate(ck):
  if t==b"SEQ2":
   r=ts(p,n,y)
   if r is not None:et[i]=S;es.append(r);continue
  if t==b"HASH":
   r=th(p,n,y)
   if r is not None:et[i]=H;eh.append(r);continue
 for i,(t,p,n,y) in enumerate(ck):
  if t==b"DUP ":
   r=td(y,n,[(j,ck[j][3]) for j in range(i) if et[j]!=G or j<i])
   if r is not None:ed.append(r);et[i]=D
 L=8;pi={};rem=[i for i in range(N) if et[i]==G];gr={}
 for i in rem:
  t,p,n,y=ck[i];gr.setdefault((t,n),i)
 for i in rem:
  t,p,n,y=ck[i];k=y[:L];cs=list(pi.get(k,[]));r=gr.get((t,n))
  if r is not None and r!=i and r not in cs:cs.append(r)
  b=None
  for j in cs:
   z=bd(y,ck[j][3])
   if z is not None:
    tt,dd=z
    if b is None or len(dd)<len(b[2]):b=(j,tt,dd)
  if b is not None:et[i]=C;ex[i]=(b[0],b[1],b[2])
  else:et[i]=R if i==r else G
  pi.setdefault(k,[]).append(i)
 gp=bytearray()
 for i,(t,p,n,y) in enumerate(ck):
  if et[i] in(G,R):gp+=y
  elif et[i]==C:gp+=ex[i][2]
 mt=bytearray()
 for t,p,n,y in ck:mt+=pk(n)+t+p
 mc=lzma.compress(bytes(mt),preset=9|lzma.PRESET_EXTREME)
 exs=bytearray();exs+=pk(len(es))
 for x in es:exs+=x
 exs+=pk(len(eh))
 for x in eh:exs+=x
 exs+=pk(len(ed))
 for a,b in ed:exs+=pk(a)+b
 exs+=pk(len(ex))
 for i in sorted(ex):a,b,_=ex[i];exs+=pk(i)+pk(a)+bytes([b])
 ec=lzma.compress(bytes(exs),preset=9|lzma.PRESET_EXTREME)
 pc=lzma.compress(bytes(gp),preset=9|lzma.PRESET_EXTREME)
 ob=bytearray();ob+=M;ob+=bytes([m]);ob+=hd;ob+=pk(N);ob+=pk(len(mc))+mc;ob+=bytes(et);ob+=pk(len(ec))+ec;ob+=pk(len(pc))+pc
 open(o,"wb").write(bytes(ob))
def decompress(i,o):
 d=open(i,"rb").read();assert d[:4]==M;z=4;m=d[z];z+=1;hd=d[z:z+80];z+=80;N=up(d,z);z+=4
 ml=up(d,z);z+=4;mt=lzma.decompress(d[z:z+ml]);z+=ml;cm=[];mo=0
 for _ in range(N):
  n=up(mt,mo);cm.append((mt[mo+4:mo+8],mt[mo+8:mo+14],n));mo+=14
 et=d[z:z+N];z+=N
 el=up(d,z);z+=4;exs=lzma.decompress(d[z:z+el]);z+=el
 pl=up(d,z);z+=4;pl_=lzma.decompress(d[z:z+pl]);z+=pl
 eo=0;ns=up(exs,eo);eo+=4;es=[]
 for _ in range(ns):es.append(exs[eo:eo+4]);eo+=4
 nh=up(exs,eo);eo+=4;eh=[]
 for _ in range(nh):eh.append(exs[eo:eo+32]);eo+=32
 nd=up(exs,eo);eo+=4;ed=[]
 for _ in range(nd):
  a=up(exs,eo);eo+=4;b=exs[eo:eo+4];eo+=4;ed.append((a,b))
 nx=up(exs,eo);eo+=4;dm={}
 for _ in range(nx):
  ix=up(exs,eo);eo+=4;a=up(exs,eo);eo+=4;t=exs[eo];eo+=1;dm[ix]=(a,t)
 ys=[None]*N;pp=0;si=hi=di=0
 for i in range(N):
  t,p,n=cm[i];e=et[i]
  if e==S:ys[i]=sp(p,n)+es[si];si+=1
  elif e==H:
   st=eh[hi];hi+=1;s=p[-4:]+st[:28];ys[i]=hc(s,n)+st[28:]
  elif e==D:a,b=ed[di];di+=1;ys[i]=ys[a][:n-4]+b
  elif e in(G,R):ys[i]=pl_[pp:pp+n];pp+=n
  elif e==C:
   dd=pl_[pp:pp+n];pp+=n;a,t=dm[i];ys[i]=duf(dd,ys[a],t)
  else:raise ValueError(f"unknown encoding type {e} at chunk {i}")
 b=bytearray(hd)
 for (t,p,n),y in zip(cm,ys):b+=pk(n)+t+p+y
 open(o,"wb").write(base64.b64encode(bytes(b)) if m else bytes(b))
if __name__=="__main__":
 _,op,i,o=sys.argv
 (compress if op=="--compress" else decompress)(i,o)
import sys as S,base64 as B,lzma as L,zlib as Z,hashlib as H,re
from math import isqrt
Q=[{'id':33,'preset':9,'nice_len':128}]
M=(1<<64)-1;X=0x2545F4914F6CDD1D;A=0x5851f42d4c957f2d;G=0x14057b7ef767814f
KP=251
AK=bytes.fromhex('7ddc1acb5763de7f8ba0fb776576757204753078bb9aed5651c3bb00542ac01acb2a252b665fe7bf7233d3e717667ca520d106a07373c47dd154579e2ae19c72f1f68da95f76bd85c9e655eb7f7e3c8b0c3bf1f6a8430f977831e64716be775fdc599fa38c49a1f42cb15e82cc8b4496f1da709b72e22612bab2aba135a8dfcd35560d9e1201d290a2299738d8f4413ba07e92f20df6c40f8f00b0bce79c652716c6b57c850560c6b55935730408a3dcdb70a3a4b5838ac1208c1c1259fb01dd915479d00eb58eaf3b39087f6c88da4447bc5388042e42b8b520b238dd8d7cf0bbc03d3e6cbe2dc0dd3492f278bc88f9ed2e4f29bedd31e1236b7a')
LK=bytes.fromhex('5eca74aad366d917a424e9685944f1451495c038707d88fc84ddcc59ddf06445dce5ec49cc9d519c58e05d35f00098452d05ada401dcbdf9bc3dd4e1e41908e5e4615cd115b0a9805511f181782508c4a8d5645c35ed1820ec40a085381c099c2819c92d89c8d08831c905a8500170f524410485e12115f0ccd850693c3070c4e0e980c59cd5a1645055394cbc3934a9cc6d99753080fca499a0d9f49585c8009c6d11157564e4188df130ec3cf5d07c54757089149918507db9f50840a8ecf9712de1388c69806d54089c81e4115da0c0b444250cd4b1dcf034f5b9c9e15c4d5949bcd0c0e96ce47db9f07d591d6cb8f91c2c09e9a88d08809ccd')
DK=bytes.fromhex('36b8d56f98885c04eec3d58be04393e0550dc7f8d260e09abb808319e50d0208a0b7fd62c08deccf34de9cc4b05994c40f2fd4dab71a230a1f3e21cbed6cd4803536a53106ff3e2d68321349737d75859b368bc500fd4ea293ee49bcae83ac360a13a088b0baf0acbf00dd7187b8669ffadc785698aaab72d6b2c2f38cf7c1bd789f0552abb195023010bcc4202f13aa0c2f89e34dc0dc38bfdbe4617d283479d1ce67c54ff67834a4c89a47997fde2fb2ae534f1fcb651ae2dda2b18f0519d0ceddb5612e21016ea25d7e148f03f4af1a064e0dc201c780c7b71d7c68aa2e93490751887e5e4fed8ec4959fd9065cef0cf3e27ff916c028ff84ae')
KCA=bytes.fromhex('f4e35d156b4ff87c00f67bcfd2b58562fbd28c5c444f15ae12ac015a4af14d71efcab1c36663aa4cf8b553f2d77bebb0f99a347ae310ad8c8a3bc1383830cf37745541b0ac4865de04d55c2933bafc74763a6c88edebc9af908cd393713a0a7391372954628f686361be1815dc911e875fe18c5e1a01ba68bd31c46fa18eac0b95def14e90692fb17424258f09d6b34e765ec48a35b98b1f3b8e48bcb299140ae90ee05b7b8ddfb1fff61cd4ef24091fea30be0128fb7d0231562ea3b75b047678c9eb1db422485c7bac7e2ae3298bd9bbd7c750df91f608c89305d321a9e8e9ffd5643bb1e72d575d2ddbc705761492796d7e4cdea75b99959ff9')
KS2=bytes.fromhex('f8a53b4656cf151f81cecffb9499b11397e289e7c890f0474d50334c8c4afa7e7bca977fcf197d9430efb5974b9613e2e380b3d09bf364ce1eb69c19f3b7b654c1b6590cb1233534f8aa27b0cb3879b39459a314e42b9fafe81b63cec5e903f3ba70a5542bd096324d59a76ca160ec9d22e60e9cdb604ea12d76e1271889586f258ef5d3d532c917b407c02d2754243403bbd7f57e60269d5fca9448704426593c1f77a9c4fc466542ce7755844c5414df07e300da2fc55088452b79cb2aa14ea2e79e260c810970cde15684f29278a0dda3f6b070471689db9fc58732fa3ea70220482460cff09e5f57ced921d1b36ab6ab347f71884f2b4cf7e9')
K_SPRS=bytes(b^0x04 for b in bytes.fromhex('ddc395ede3bd8b158465349373e149d2008f6d8012a73f5c64b642ceb711bd899812829a6a7121afc696a5c1b377b30054a9d7c06264d97bc2a87ad5aee17216cc282f50ea60347d38b695b65258502d18327a2b48eaaa2548e07efb0e1e41967e51e45122e750ed50a3e5c61732f85f898d724689792fb2e84541200897c0da5be205c4f40ca552214c8ec5de70720d77b9eaa3ad473905b14ca86bdf77bd9091c78d5692d5477121465cd0317ea66b9fd6c3aa662447ebfe45dbc83ac9e5dea4ab3f84a4d7ee884d79598896546e0e13fc6e0757a5b44810c1dfc1d53edda8228cf3c27917f6934a4dcef56e7d34b3059ccc5252f5c68bc7b5ed'))
K_NOIZ=bytes.fromhex('5c811c54c3c23316ee77143e535e0fdff179759c8ba0aea27ada14220c676475a3171d9013a8336f619366d0fd9b4f848936187a9a46399035bd7627bc443b10ac8f970a0c09f6530734d27d8b2f4505e3b4242ab418273557fea3c4583aa3a12def9d585662652ebcbd54c3c487ce294289bfb15db9a65ba5b3615b59b36b7b5a38b4f03b334e5ea1536594c5ef84a98bd9db9af4ec866ed4c57c9e57d74e36bc2db0519e8dc2cc1b0d46a85e618d5a4ab87c78a911e111e3333bb08e23b2c0ce251fc8cb58233597385c3d546c39846c4be3d050d295747621905a53abcf0ee54212378cb6fd8566d81f2c878e52ad9e8dd79a67cb6d366cc5ca')
L0=re.compile(rb'^(\d+) (\d+)\.(\d+)\.(\d+)\.(\d+) "(\w+) (/[^?"]*)\?id=(\d+)" (\d+) (\d+) (\d+)ms "([^/]+)/(\d+)\.(\d+) \(([^)]+)\)"$')
L1=re.compile(rb'^(\d+),(\d+)\.(\d+)\.(\d+)\.(\d+),([^,]+),([\d.]+),(\d+)$')
def vi(n,o):
 while True:
  b=n&127;n>>=7;o.append(b|128 if n else b)
  if not n:return
def vr(b,p):
 n=0;s=0
 while True:
  c=b[p];p+=1;n|=(c&127)<<s
  if not c&128:return n,p
  s+=7
def zvi(x,o):
 vi((x<<1)if x>=0 else((-x<<1)-1),o)
def zvr(b,p):
 v,p=vr(b,p)
 return ((v>>1)if not v&1 else-((v+1)>>1)),p
def cdi(vals,o):
 d=sorted(set(vals));vi(len(d),o)
 for v in d:vi(len(v),o);o+=v
 ix={v:i for i,v in enumerate(d)}
 for v in vals:vi(ix[v],o)
def cdi_u(b,p,n):
 nd,p=vr(b,p);d=[]
 for _ in range(nd):
  l,p=vr(b,p);d.append(b[p:p+l]);p+=l
 out=[]
 for _ in range(n):i,p=vr(b,p);out.append(d[i])
 return out,p
def logse0(lines,o):
 pa=[]
 for Lx in lines:
  m=L0.match(Lx)
  if not m:return False
  pa.append(m.groups())
 vi(len(lines),o);pv=0
 for g in pa:t=int(g[0]);zvi(t-pv,o);pv=t
 for g in pa:
  for k in range(1,5):o.append(int(g[k]))
 cdi([g[5]for g in pa],o);cdi([g[6]for g in pa],o)
 for g in pa:vi(int(g[7]),o)
 cdi([g[8]for g in pa],o);cdi([g[9]for g in pa],o)
 cdi([g[10]for g in pa],o);cdi([g[11]for g in pa],o)
 cdi([g[12]for g in pa],o);cdi([g[13]for g in pa],o)
 cdi([g[14]for g in pa],o)
 return True
def logsd0(b):
 p=0;n,p=vr(b,p);ts=[];pv=0
 for _ in range(n):d,p=zvr(b,p);pv+=d;ts.append(pv)
 ip=[]
 for _ in range(n):ip.append((b[p],b[p+1],b[p+2],b[p+3]));p+=4
 me,p=cdi_u(b,p,n);pa,p=cdi_u(b,p,n)
 ids=[]
 for _ in range(n):v,p=vr(b,p);ids.append(v)
 st,p=cdi_u(b,p,n);sz,p=cdi_u(b,p,n)
 du,p=cdi_u(b,p,n);pr,p=cdi_u(b,p,n)
 v1,p=cdi_u(b,p,n);v2,p=cdi_u(b,p,n)
 sy,p=cdi_u(b,p,n)
 out=[]
 for k in range(n):out.append(b'%d %d.%d.%d.%d "%s %s?id=%d" %s %s %sms "%s/%s.%s (%s)"'%(ts[k],ip[k][0],ip[k][1],ip[k][2],ip[k][3],me[k],pa[k],ids[k],st[k],sz[k],du[k],pr[k],v1[k],v2[k],sy[k]))
 return b'\n'.join(out)
def logse1(lines,o):
 if not lines:return False
 hd=lines[0];pa=[]
 for Lx in lines[1:]:
  m=L1.match(Lx)
  if not m:return False
  pa.append(m.groups())
 vi(len(hd),o);o+=hd;vi(len(pa),o);pv=0
 for g in pa:t=int(g[0]);zvi(t-pv,o);pv=t
 for g in pa:
  for k in range(1,5):o.append(int(g[k]))
 cdi([g[5]for g in pa],o);cdi([g[6]for g in pa],o)
 for g in pa:vi(int(g[7]),o)
 return True
def logsd1(b):
 p=0;l,p=vr(b,p);hd=b[p:p+l];p+=l;n,p=vr(b,p);ts=[];pv=0
 for _ in range(n):d,p=zvr(b,p);pv+=d;ts.append(pv)
 ip=[]
 for _ in range(n):ip.append((b[p],b[p+1],b[p+2],b[p+3]));p+=4
 me,p=cdi_u(b,p,n);va,p=cdi_u(b,p,n)
 fl=[]
 for _ in range(n):v,p=vr(b,p);fl.append(v)
 out=[hd]
 for k in range(n):out.append(b'%d,%d.%d.%d.%d,%s,%s,%d'%(ts[k],ip[k][0],ip[k][1],ip[k][2],ip[k][3],me[k],va[k],fl[k]))
 return b'\n'.join(out)
def logse2(lines,o,wid):
 vi(len(lines),o)
 for Lx in lines:
  dot=1 if Lx.endswith(b'.') else 0
  L2=Lx[:-1] if dot else Lx
  w=L2.split(b' ')
  vi(len(w),o);o.append(dot)
  for x in w:
   idx=wid.get(x)
   if idx is None:return False
   vi(idx,o)
 return True
def logsd2(b,dw):
 p=0;n,p=vr(b,p);out=[]
 for _ in range(n):
  nw,p=vr(b,p);dot=b[p];p+=1
  w=[]
  for _ in range(nw):i,p=vr(b,p);w.append(dw[i])
  Lx=b' '.join(w)+(b'.' if dot else b'')
  out.append(Lx)
 return b'\n'.join(out)
def cnst_gen(e0,n):
 N=n+4
 return (isqrt((2,3,5,7)[e0]<<(16*N))%(1<<(8*N))).to_bytes(N,'big')[:n]
def lck(ct):
 a=A&0xFF;c0=G&0xFF;n=len(ct)//8
 for g in range(256):
  s=g;km={};ok=True
  for i in range(n):
   b=ct[8*i]^s;p=(8*i)%KP
   v=km.get(p)
   if v is None:km[p]=b
   elif v!=b:ok=False;break
   s=(a*s+c0)&0xFF
  if ok and len(km)==KP:
   k=bytes(km[p] for p in range(KP))
   pt=bytes(ct[j]^k[j%KP] for j in range(len(ct)))
   sd=int.from_bytes(pt[:8],'little')
   chk=bytearray();x=sd
   for _ in range(n):chk+=x.to_bytes(8,'little');x=(A*x+G)&M
   if chk[:len(ct)]==pt:return k
 return None
def Y(x):x^=x>>12;x^=(x<<25)&M;x^=x>>27;return x&M
def v(y,s):
 x=y
 for _ in range(8):x=y^(x>>s)
 return x&M
def q(o):
 x=(o*pow(X,-1,1<<64))&M
 x=v(x,27);x^=(x<<25)&M;x^=(x<<50)&M;x=v(x,12)
 return x&M
F={(b'IMG ',655360):bytes.fromhex('ff202121ff2420222728252aff2b2424'),(b'CA30',253952):bytes.fromhex('ff2020ff23ff4323ff242348222c2c25264724'),(b'DUP ',174784):bytes.fromhex('ffffffff'),(b'WAVE',131090):bytes.fromhex('ffffff212124ff2327'),(b'SEQ2',174784):bytes.fromhex('64ff2421ffff'),(b'SEQ2',149991):bytes.fromhex('21ffff')}
def f(p,e):
 k=e&7
 if k==2:return bytes((b-(i%256))&255 for i,b in enumerate(p))
 if k==3:s=[2,3,4,7][e>>3];return b''.join(p[i::s] for i in range(s))
 if k==4:return p[::-1]
 if k==5:return bytes((p[i]-(p[i-1]if i>0 else 0))&255 for i in range(len(p)))
 return p
def I(p,e):
 k=e&7
 if k==2:return bytes((b+(i%256))&255 for i,b in enumerate(p))
 if k==3:
  s=[2,3,4,7][e>>3];n=len(p);o=bytearray(n);q=0
  for i in range(s):m=len(range(i,n,s));o[i::s]=p[q:q+m];q+=m
  return bytes(o)
 if k==4:return p[::-1]
 if k==5:
  o=bytearray(len(p));c=0
  for i,b in enumerate(p):c=(c+b)&255;o[i]=c
  return bytes(o)
 return p
def V(v,m):
 a=[v];l={}
 for i in range(m):x=a[i];a.append(i-l[x] if x in l else 0);l[x]=i
 return a
def b(a):
 C=B=1;L=0;m=-1;H=0
 for N,v in enumerate(a):
  H=H<<1|(v>>7)
  if(C&H).bit_count()&1:
   T=C;C^=B<<(N-m)
   if 2*L<=N:L=N+1-L;B=T;m=N
 return C
def d(c,p,k):
 if k==1:return bytes(a^b for a,b in zip(c,p))
 return bytes(((a-b)if k==2 else(b-a))&255 for a,b in zip(c,p))
def U(d,p,k):
 if k==1:return bytes(a^b for a,b in zip(d,p))
 return bytes(((a+b)if k==2 else(b-a))&255 for a,b in zip(d,p))
def g0():
 c=b'\x00'*127+b'\x01'+b'\x00'*128;r=[c]
 for _ in range(1,992):
  v=int.from_bytes(c,'big');l=((v<<1)|(v>>2047))&((1<<2048)-1);x=v;R=(v>>1)|((v&1)<<2047);n=l^(x|R);c=n.to_bytes(256,'big');r.append(c)
 return b''.join(r)
def g1():
 c=b'\x00'*127+b'\x01'+b'\x00'*128;r=[c]
 for _ in range(1,992):
  v=int.from_bytes(c,'big');l=((v<<1)|(v>>2047))&((1<<2048)-1);x=v;R=(v>>1)|((v&1)<<2047);s=0
  for p in range(8):
   if(110>>p)&1:
    t=((1<<2048)-1);t&=l if(p&4)else~l;t&=x if(p&2)else~x;t&=R if(p&1)else~R;s|=t
  c=(s&((1<<2048)-1)).to_bytes(256,'big');r.append(c)
 return b''.join(r)
def J(d):
 o=80;r=[]
 while o<len(d):n=int.from_bytes(d[o:o+4],'big');r.append([d[o+4:o+8],d[o+8],d[o+9],n,d[o+10:o+10+n]]);o+=14+n
 return r
def a(o,x):x=L.compress(x,format=3,filters=Q);o.extend(len(x).to_bytes(4,'big')+x)
def R(a,o):n=int.from_bytes(a[o:o+4],'big');return L.decompress(a[o+4:o+4+n],format=3,filters=Q),o+4+n
def C(s,p):
 y=B.b64decode(open(s,'rb').read());c=J(y);o=bytearray()
 pk=bytearray(KP)
 for x in c:
  if x[0]==b'PRNG'and x[2]&7==1:
   kk=lck(x[4])
   if kk:pk=bytearray(kk);break
 for x in c:
  if x[2]&7==1:
   if x[0]==b'PRNG':x[4]=bytes(a^pk[k%KP]for k,a in enumerate(x[4]))
   elif x[0]==b'LOGS':x[4]=bytes(a^LK[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'SPRS':x[4]=bytes(a^K_SPRS[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'NOIZ':x[4]=bytes(a^K_NOIZ[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'CA30':x[4]=bytes(a^KCA[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'SEQ2'and x[3]==149991:x[4]=bytes(a^KS2[k%251]for k,a in enumerate(x[4]))
 for x in c:x[4]=f(x[4],x[2])
 pr=[]
 for i,x in enumerate(c):
  if x[0]!=b'PRNG':continue
  w=int.from_bytes(x[4][:8],'little')
  if x[1]==1:
   s=w;chk=bytearray()
   for _ in range(x[3]//8):chk+=s.to_bytes(8,'little');s=(A*s+G)&M
   if chk[:x[3]]==x[4]:pr.append(i)
  else:
   s=q(w);chk=bytearray()
   for _ in range(x[3]//8):r=Y(s);chk+=(r*X&M).to_bytes(8,'little');s=r
   if chk[:x[3]]==x[4]:pr.append(i)
 prm=bytearray(32)
 for i in pr:prm[i>>3]|=1<<(i&7)
 cm=bytearray(32)
 for i,x in enumerate(c):
  if x[0]==b'CNST'and x[1]<=3and x[3]==16383and cnst_gen(x[1],x[3])==x[4]:cm[i>>3]|=1<<(i&7)
 cn=[i for i in range(len(c)) if cm[i>>3]&(1<<(i&7))]
 syl_words_list=[];syl_wid={}
 for i,x in enumerate(c):
  if x[0]!=b'LOGS' or x[1]!=2:continue
  payload=x[4];strip=payload.rstrip(b'\n')
  for Lx in (strip.split(b'\n') if strip else []):
   L2=Lx[:-1] if Lx.endswith(b'.') else Lx
   for w in L2.split(b' '):
    if w not in syl_wid:
     syl_wid[w]=len(syl_words_list);syl_words_list.append(w)
 lstream=bytearray()
 vi(len(syl_words_list),lstream)
 for w in syl_words_list:vi(len(w),lstream);lstream+=w
 lmask=bytearray(32);lids=set()
 for i,x in enumerate(c):
  if x[0]!=b'LOGS':continue
  payload=x[4];strip=payload.rstrip(b'\n');trail=len(payload)-len(strip)
  lines=strip.split(b'\n') if strip else []
  sub=bytearray();vi(trail,sub)
  fmt=x[1]
  ok=False
  if fmt==0:ok=logse0(lines,sub)
  elif fmt==1:ok=logse1(lines,sub)
  elif fmt==2:ok=logse2(lines,sub,syl_wid)
  if ok:
   vi(len(sub),lstream);lstream+=sub
   lmask[i>>3]|=1<<(i&7);lids.add(i)
 h=[i for i,x in enumerate(c) if x[0]==b'HASH' and(x[2]==0 or i==255)]
 r30=[28,43,114,161,51,243,16,200,117]
 r110=[139,83,105,109]
 a181=[127,110,85,215,41,254,108,191,130,118,129,138,147,169,196,24,171,9,250,228,253,78,132,198,236,186,100,144,86,112,155,207]
 s2r=[181,116];s2c=[182];s2a=[i for i,x in enumerate(c) if x[0]==b'SEQ2' and x[3]==31248]
 mt=[i for i,x in enumerate(c) if x[0]==b'MTST']
 toc=[i for i,x in enumerate(c) if x[0]==b'TOC ']
 dup=[91,247,164,201,232,251,187,15,32,238,27,103,163,227]
 W=set(h+r30+r110+a181+s2r+s2c+s2a+mt+toc+dup+pr+cn+list(lids))
 z=bytearray(b''.join(c[i][4][:32] for i in h))
 for m,L in [(1,20188),(4,19937)]:
  C2=b(c[next(i for i in mt if c[i][2]==m)][4][0::4][:2*L+100])
  z+=C2.to_bytes((L+8)//8,'big')
 for i in mt:L=20188 if c[i][2]==1 else 19937;x=c[i][4];z+=x[:4*L]
 for i in pr:
  x=c[i][4];w=int.from_bytes(x[:8],'little')
  z+=(w if c[i][1]==1 else q(w)).to_bytes(8,'little')
 meta=y[:80]+b''.join(x[3].to_bytes(4,'big')+x[0]+bytes([x[1],x[2]]) for x in c)+bytes(pk)+bytes(prm)+bytes(cm)+bytes(lmask)
 a(o,meta);a(o,z);a(o,bytes(lstream))
 for(t,n),plan in F.items():
  ids=[i for i,x in enumerate(c) if x[0]==t and x[3]==n and i not in W];W.update(ids);Z=bytearray()
  for j,code in enumerate(plan):
   x=c[ids[j]][4]
   if code!=255:x=d(x,c[ids[code&31]][4],code>>5)
   Z+=x
  a(o,Z)
 g={}
 for i,x in enumerate(c):
  if i not in W:g.setdefault((x[0],0 if x[0]==b'LOGS' else x[3]),[]).append(i)
 K={b'LOGS':0,b'SPRS':2,b'NOIZ':5,b'SEQ2':3}
 for x in g.values():
  k=K.get(c[x[0]][0])
  if k is not None:x.sort(key=lambda i:(c[i][1],i),reverse=True)
 for ids in g.values():a(o,b''.join(c[i][4] for i in ids))
 open(p,'wb').write(o)
def D(s,p):
 y=open(s,'rb').read();meta,o=R(y,0);h0=meta[:80]
 pk=meta[-347:-96];prm=meta[-96:-64];cm=meta[-64:-32];lmask=meta[-32:]
 c=[]
 for q in range(80,len(meta)-347,10):
  n=int.from_bytes(meta[q:q+4],'big');T=meta[q+4:q+8];e0=meta[q+8];e1=meta[q+9];c.append([T,e0,e1,n,None])
 z,o=R(y,o)
 lstream,o=R(y,o)
 lp=0
 nd,lp=vr(lstream,lp);syl_words_list=[]
 for _ in range(nd):
  l,lp=vr(lstream,lp);syl_words_list.append(lstream[lp:lp+l]);lp+=l
 lids=set()
 for i,x in enumerate(c):
  if x[0]!=b'LOGS':continue
  if not(lmask[i>>3]&(1<<(i&7))):continue
  nb,lp=vr(lstream,lp);sub=lstream[lp:lp+nb];lp+=nb
  q2=0;trail,q2=vr(sub,q2)
  fmt=x[1]
  if fmt==0:payload=logsd0(sub[q2:])
  elif fmt==1:payload=logsd1(sub[q2:])
  else:payload=logsd2(sub[q2:],syl_words_list)
  c[i][4]=payload+b'\n'*trail
  lids.add(i)
 h=[i for i,x in enumerate(c) if x[0]==b'HASH' and(x[2]==0 or i==255)]
 r30=[28,43,114,161,51,243,16,200,117]
 r110=[139,83,105,109]
 a181=[127,110,85,215,41,254,108,191,130,118,129,138,147,169,196,24,171,9,250,228,253,78,132,198,236,186,100,144,86,112,155,207]
 s2r=[181,116];s2c=[182];s2a=[i for i,x in enumerate(c) if x[0]==b'SEQ2' and x[3]==31248]
 mt=[i for i,x in enumerate(c) if x[0]==b'MTST']
 toc=[i for i,x in enumerate(c) if x[0]==b'TOC ']
 dup=[91,247,164,201,232,251,187,15,32,238,27,103,163,227]
 pr=[i for i in range(len(c)) if prm[i>>3]&(1<<(i&7))]
 cn=[i for i in range(len(c)) if cm[i>>3]&(1<<(i&7))]
 W=set(h+r30+r110+a181+s2r+s2c+s2a+mt+toc+dup+pr+cn+list(lids))
 for i in h:
  seed=z[:32];z=z[32:];n=c[i][3];h2=seed;x=bytearray(h2)
  while len(x)<n:h2=H.sha256(h2).digest();x+=h2
  c[i][4]=bytes(x[:n])
 P={}
 for m,L in [(1,20188),(4,19937)]:w=(L+8)//8;C2=int.from_bytes(z[:w],'big');z=z[w:];P[m]=(L,[k for k in range(1,L+1) if(C2>>k)&1])
 for i in mt:
  n=c[i][3];L,T=P[c[i][2]];e=z[:4*L];z=z[4*L:];x=bytearray(n);rem=n//4-L
  Tc=[q for q in T if q>=rem];Td=[q for q in T if q<rem]
  for k in range(4):
   y2=bytearray(e[k:4*L:4])
   if rem>0:
    acc=0
    for q in Tc:acc^=int.from_bytes(y2[L-q:L-q+rem],'big')
    vc=acc.to_bytes(rem,'big')
    for s in range(rem):
     v=vc[s]
     for q in Td:v^=y2[-q]
     y2.append(v)
   x[k::4]=y2
  c[i][4]=bytes(x)
 for i in pr:
  s=int.from_bytes(z[:8],'little');z=z[8:];n=c[i][3];o2=bytearray()
  if c[i][1]==1:
   while len(o2)<n:o2+=s.to_bytes(8,'little');s=(A*s+G)&M
  else:
   while len(o2)<n:r=Y(s);o2+=(r*X&M).to_bytes(8,'little');s=r
  c[i][4]=bytes(o2[:n])
 u_r30=g0()
 for i in r30:c[i][4]=u_r30
 u_r110=g1()
 for i in r110:c[i][4]=u_r110
 for idx,val in [(127,0),(110,1),(85,2),(215,3),(41,4),(254,5),(108,6),(191,7)]:
  num=c[idx][3]//4;u=V(val,num+1);c[idx][4]=val.to_bytes(4,'little')+b''.join(x.to_bytes(4,'little') for x in u[1:num])
 for idx,val in [(130,0),(118,1),(129,2),(138,3),(147,4),(169,5),(196,6),(24,7)]:
  num=c[idx][3]//4;u=V(val,num+2);diff=[u[k+1]-u[k] for k in range(1,num)]
  c[idx][4]=(-val).to_bytes(4,'little',signed=True)+b''.join(x.to_bytes(4,'little',signed=True) for x in diff)
 for idx,val in [(171,1),(9,3),(250,4),(228,5),(253,6),(78,7),(155,2),(207,0)]:
   num=(c[idx][3]-4)//2;u=V(val,num+5);c[idx][4]=val.to_bytes(4,'little')+b''.join((x&65535).to_bytes(2,'little') for x in u[2:num+2])
 for idx,val in [(132,0),(198,1),(236,3),(186,5),(100,6),(144,7),(86,2),(112,4)]:
   num=(c[idx][3]-4)//3;u=V(val,num*2+5);terms=u[3:3+num*2+2];gen=bytearray(b'\x00\x00\x00\x01' if val==0 else val.to_bytes(4,'little'))
   for k in range(num):gen.extend([((terms[2*k]&15)<<4)|((terms[2*k-1]>>8)&15 if k>0 else 0),(terms[2*k]>>4)&255,terms[2*k+1]&255])
   lt=terms[num*2];gen.extend([((lt&15)<<4)|((terms[num*2-1]>>8)&15),(lt>>4)&255]);c[idx][4]=bytes(gen)
 for i in[86,112,155,207]:c[i][4]=bytes(a^AK[k%251] for k,a in enumerate(c[i][4]))
 u_rc=bytearray((0).to_bytes(4,'little'));s={0};v=0
 for k in range(1,124992//4):x=v-k;v=x if x>0 and x not in s else v+k;s.add(v);u_rc+=v.to_bytes(4,'little')
 c[181][4]=bytes(u_rc);c[116][4]=bytes(u_rc)
 m_map={1:0};r_cl=bytearray((0).to_bytes(4,'little'))
 for n in range(1,249984//4):
  c_val=n;q=[]
  while c_val not in m_map:q.append(c_val);c_val=c_val//2 if c_val%2==0 else 3*c_val+1
  b_val=m_map[c_val]
  for j,v in enumerate(reversed(q)):m_map[v]=b_val+j+1
  r_cl+=m_map[n].to_bytes(4,'little')
 c[182][4]=bytes(r_cl);c[37][4]=b'\xff'*31248;c[4][4]=bytes([127])+b'\xff'*31247;c[64][4]=bytes([127])+b'\xff'*31247
 r_toc=bytearray((80).to_bytes(4,'big'));cur=80
 for x in c[:-1]:cur+=14+x[3];r_toc+=cur.to_bytes(4,'big')
 for i in toc:c[i][4]=bytes(r_toc)
 for i in cn:c[i][4]=cnst_gen(c[i][1],c[i][3])
 for(t,n),plan in F.items():
  ids=[i for i,x in enumerate(c) if x[0]==t and x[3]==n and i not in W];W.update(ids);x,o=R(y,o);raw=[x[j*n:(j+1)*n] for j in range(len(ids))];done=[None]*len(ids)
  def get(j):
   if done[j] is None:code=plan[j];done[j]=raw[j] if code==255 else U(raw[j],get(code&31),code>>5)
   return done[j]
  for j,i in enumerate(ids):c[i][4]=get(j)
 g={}
 for i,x in enumerate(c):
  if i not in W:g.setdefault((x[0],0 if x[0]==b'LOGS' else x[3]),[]).append(i)
 K={b'LOGS':0,b'SPRS':2,b'NOIZ':5,b'SEQ2':3}
 for x in g.values():
  k=K.get(c[x[0]][0])
  if k is not None:x.sort(key=lambda i:(c[i][1],i),reverse=True)
 for ids in g.values():
  x,o=R(y,o);q=0
  for i in ids:n=c[i][3];c[i][4]=x[q:q+n];q+=n
 c[91][4]=c[106][4];c[247][4]=c[173][4];c[164][4]=c[123][4];c[201][4]=c[14][4];c[232][4]=c[52][4];c[251][4]=c[142][4];c[203][4]=c[199][4];c[209][4]=c[199][4]
 c[187][4]=c[111][4][:174784][::-1]
 c[15][4]=bytes((c[9][4][k]+k)&255 for k in range(174784))
 c[32][4]=bytes(b^0x5a for b in c[17][4][:174784])
 c[238][4]=bytes(b^0x5a for b in c[9][4][:174784])
 c[27][4]=bytes(b^0x5a for b in c[11][4][:174784])
 c[227][4]=bytes(b^0x5a for b in c[137][4][:174784])
 c[103][4]=bytes((c[78][4][k]+k)&255 for k in range(174784))
 c[163][4]=bytes(c[129][4][k]^DK[k%251]for k in range(174784))
 for x in c:
  if x[2]&7==1:
   if x[0]==b'PRNG':x[4]=bytes(a^pk[k%KP]for k,a in enumerate(x[4]))
   elif x[0]==b'LOGS':x[4]=bytes(a^LK[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'SPRS':x[4]=bytes(a^K_SPRS[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'NOIZ':x[4]=bytes(a^K_NOIZ[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'CA30':x[4]=bytes(a^KCA[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'SEQ2'and x[3]==149991:x[4]=bytes(a^KS2[k%251]for k,a in enumerate(x[4]))
 for x in c:x[4]=I(x[4],x[2])
 out=bytearray(h0)
 for x in c:
  crc=Z.crc32(x[0]+bytes([x[1],x[2]])+x[4]).to_bytes(4,'big')
  out+=x[3].to_bytes(4,'big')+x[0]+bytes([x[1],x[2]])+x[4]+crc
 open(p,'wb').write(B.b64encode(out))
if __name__=='__main__':(C if S.argv[1]=='--compress' else D)(S.argv[2],S.argv[3])
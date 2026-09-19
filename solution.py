import sys as S,base64 as B,lzma as L,zlib as Z,hashlib as H,re,bz2,math
from math import isqrt
Q=[{'id':33,'preset':9,'nice_len':128}]
KP=251
M=(1<<64)-1;X=0x2545F4914F6CDD1D;A=0x5851f42d4c957f2d;G=0x14057b7ef767814f
MT_N=624;MT_M=227;MT_L1=20188;MT_CW=(MT_L1+8)//8
AK=bytes.fromhex('7ddc1acb5763de7f8ba0fb776576757204753078bb9aed5651c3bb00542ac01acb2a252b665fe7bf7233d3e717667ca520d106a07373c47dd154579e2ae19c72f1f68da95f76bd85c9e655eb7f7e3c8b0c3bf1f6a8430f977831e64716be775fdc599fa38c49a1f42cb15e82cc8b4496f1da709b72e22612bab2aba135a8dfcd35560d9e1201d290a2299738d8f4413ba07e92f20df6c40f8f00b0bce79c652716c6b57c850560c6b55935730408a3dcdb70a3a4b5838ac1208c1c1259fb01dd915479d00eb58eaf3b39087f6c88da4447bc5388042e42b8b520b238dd8d7cf0bbc03d3e6cbe2dc0dd3492f278bc88f9ed2e4f29bedd31e1236b7a')
LK=bytes.fromhex('5eca74aad366d917a424e9685944f1451495c038707d88fc84ddcc59ddf06445dce5ec49cc9d519c58e05d35f00098452d05ada401dcbdf9bc3dd4e1e41908e5e4615cd115b0a9805511f181782508c4a8d5645c35ed1820ec40a085381c099c2819c92d89c8d08831c905a8500170f524410485e12115f0ccd850693c3070c4e0e980c59cd5a1645055394cbc3934a9cc6d99753080fca499a0d9f49585c8009c6d11157564e4188df130ec3cf5d07c54757089149918507db9f50840a8ecf9712de1388c69806d54089c81e4115da0c0b444250cd4b1dcf034f5b9c9e15c4d5949bcd0c0e96ce47db9f07d591d6cb8f91c2c09e9a88d08809ccd')
DK=bytes.fromhex('36b8d56f98885c04eec3d58be04393e0550dc7f8d260e09abb808319e50d0208a0b7fd62c08deccf34de9cc4b05994c40f2fd4dab71a230a1f3e21cbed6cd4803536a53106ff3e2d68321349737d75859b368bc500fd4ea293ee49bcae83ac360a13a088b0baf0acbf00dd7187b8669ffadc785698aaab72d6b2c2f38cf7c1bd789f0552abb195023010bcc4202f13aa0c2f89e34dc0dc38bfdbe4617d283479d1ce67c54ff67834a4c89a47997fde2fb2ae534f1fcb651ae2dda2b18f0519d0ceddb5612e21016ea25d7e148f03f4af1a064e0dc201c780c7b71d7c68aa2e93490751887e5e4fed8ec4959fd9065cef0cf3e27ff916c028ff84ae')
KCA=bytes.fromhex('f4e35d156b4ff87c00f67bcfd2b58562fbd28c5c444f15ae12ac015a4af14d71efcab1c36663aa4cf8b553f2d77bebb0f99a347ae310ad8c8a3bc1383830cf37745541b0ac4865de04d55c2933bafc74763a6c88edebc9af908cd393713a0a7391372954628f686361be1815dc911e875fe18c5e1a01ba68bd31c46fa18eac0b95def14e90692fb17424258f09d6b34e765ec48a35b98b1f3b8e48bcb299140ae90ee05b7b8ddfb1fff61cd4ef24091fea30be0128fb7d0231562ea3b75b047678c9eb1db422485c7bac7e2ae3298bd9bbd7c750df91f608c89305d321a9e8e9ffd5643bb1e72d575d2ddbc705761492796d7e4cdea75b99959ff9')
KS2=bytes.fromhex('f8a53b4656cf151f81cecffb9499b11397e289e7c890f0474d50334c8c4afa7e7bca977fcf197d9430efb5974b9613e2e380b3d09bf364ce1eb69c19f3b7b654c1b6590cb1233534f8aa27b0cb3879b39459a314e42b9fafe81b63cec5e903f3ba70a5542bd096324d59a76ca160ec9d22e60e9cdb604ea12d76e1271889586f258ef5d3d532c917b407c02d2754243403bbd7f57e60269d5fca9448704426593c1f77a9c4fc466542ce7755844c5414df07e300da2fc55088452b79cb2aa14ea2e79e260c810970cde15684f29278a0dda3f6b070471689db9fc58732fa3ea70220482460cff09e5f57ced921d1b36ab6ab347f71884f2b4cf7e9')
K_SPRS=bytes(b^4 for b in bytes.fromhex('ddc395ede3bd8b158465349373e149d2008f6d8012a73f5c64b642ceb711bd899812829a6a7121afc696a5c1b377b30054a9d7c06264d97bc2a87ad5aee17216cc282f50ea60347d38b695b65258502d18327a2b48eaaa2548e07efb0e1e41967e51e45122e750ed50a3e5c61732f85f898d724689792fb2e84541200897c0da5be205c4f40ca552214c8ec5de70720d77b9eaa3ad473905b14ca86bdf77bd9091c78d5692d5477121465cd0317ea66b9fd6c3aa662447ebfe45dbc83ac9e5dea4ab3f84a4d7ee884d79598896546e0e13fc6e0757a5b44810c1dfc1d53edda8228cf3c27917f6934a4dcef56e7d34b3059ccc5252f5c68bc7b5ed'))
K_NOIZ=bytes.fromhex('5c811c54c3c23316ee77143e535e0fdff179759c8ba0aea27ada14220c676475a3171d9013a8336f619366d0fd9b4f848936187a9a46399035bd7627bc443b10ac8f970a0c09f6530734d27d8b2f4505e3b4242ab418273557fea3c4583aa3a12def9d585662652ebcbd54c3c487ce294289bfb15db9a65ba5b3615b59b36b7b5a38b4f03b334e5ea1536594c5ef84a98bd9db9af4ec866ed4c57c9e57d74e36bc2db0519e8dc2cc1b0d46a85e618d5a4ab87c78a911e111e3333bb08e23b2c0ce251fc8cb58233597385c3d546c39846c4be3d050d295747621905a53abcf0ee54212378cb6fd8566d81f2c878e52ad9e8dd79a67cb6d366cc5ca')
L0=re.compile(rb'^(\d+) (\d+)\.(\d+)\.(\d+)\.(\d+) "(\w+) (/[^?"]*)\?id=(\d+)" (\d+) (\d+) (\d+)ms "([^/]+)/(\d+)\.(\d+) \(([^)]+)\)"$')
L1=re.compile(rb'^(\d+),(\d+)\.(\d+)\.(\d+)\.(\d+),([^,]+),([\d.]+),(\d+)$')
def vi(n,o):
 while 1:
  b=n&127;n>>=7;o.append(b|128 if n else b)
  if not n:return
def vr(b,p):
 n=0;s=0
 while 1:
  c=b[p];p+=1;n|=(c&127)<<s
  if not c&128:return n,p
  s+=7
def zvi(x,o):vi((x<<1)if x>=0 else((-x<<1)-1),o)
def zvr(b,p):
 v,p=vr(b,p)
 return((v>>1)if not v&1 else-((v+1)>>1)),p
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
 rec=[];exc=[]
 for k,Lx in enumerate(lines):
  m=L0.match(Lx)
  if m:rec.append((k,m.groups()))
  else:exc.append((k,Lx))
 if not rec or len(rec)*1000<len(lines)*980:return False
 vi(len(lines),o);vi(len(exc),o)
 for k,Lx in exc:vi(k,o);vi(len(Lx),o);o+=Lx
 pa=[g for _,g in rec]
 vi(len(rec),o);pv=0
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
 p=0;n,p=vr(b,p);ne,p=vr(b,p);exc={}
 for _ in range(ne):
  k,p=vr(b,p);l,p=vr(b,p);exc[k]=b[p:p+l];p+=l
 nr,p=vr(b,p);ts=[];pv=0
 for _ in range(nr):d,p=zvr(b,p);pv+=d;ts.append(pv)
 ip=[]
 for _ in range(nr):ip.append((b[p],b[p+1],b[p+2],b[p+3]));p+=4
 me,p=cdi_u(b,p,nr);pa,p=cdi_u(b,p,nr)
 ids=[]
 for _ in range(nr):v,p=vr(b,p);ids.append(v)
 st,p=cdi_u(b,p,nr);sz,p=cdi_u(b,p,nr)
 du,p=cdi_u(b,p,nr);pr,p=cdi_u(b,p,nr)
 v1,p=cdi_u(b,p,nr);v2,p=cdi_u(b,p,nr)
 sy,p=cdi_u(b,p,nr)
 out=[];r=0
 for k in range(n):
  if k in exc:out.append(exc[k])
  else:out.append(b'%d %d.%d.%d.%d "%s %s?id=%d" %s %s %sms "%s/%s.%s (%s)"'%(ts[r],ip[r][0],ip[r][1],ip[r][2],ip[r][3],me[r],pa[r],ids[r],st[r],sz[r],du[r],pr[r],v1[r],v2[r],sy[r]));r+=1
 return b'\n'.join(out)
def logse1(lines,o):
 if not lines:return False
 hd=lines[0];rec=[];exc=[]
 for k,Lx in enumerate(lines[1:],1):
  m=L1.match(Lx)
  if m:rec.append((k,m.groups()))
  else:exc.append((k,Lx))
 if not rec or len(rec)*1000<len(lines)*980:return False
 vi(len(lines),o);vi(len(hd),o);o+=hd;vi(len(exc),o)
 for k,Lx in exc:vi(k,o);vi(len(Lx),o);o+=Lx
 pa=[g for _,g in rec]
 vi(len(rec),o);pv=0
 for g in pa:t=int(g[0]);zvi(t-pv,o);pv=t
 for g in pa:
  for k in range(1,5):o.append(int(g[k]))
 cdi([g[5]for g in pa],o);cdi([g[6]for g in pa],o)
 for g in pa:vi(int(g[7]),o)
 return True
def logsd1(b):
 p=0;n,p=vr(b,p);l,p=vr(b,p);hd=b[p:p+l];p+=l;ne,p=vr(b,p);exc={}
 for _ in range(ne):
  k,p=vr(b,p);l,p=vr(b,p);exc[k]=b[p:p+l];p+=l
 nr,p=vr(b,p);ts=[];pv=0
 for _ in range(nr):d,p=zvr(b,p);pv+=d;ts.append(pv)
 ip=[]
 for _ in range(nr):ip.append((b[p],b[p+1],b[p+2],b[p+3]));p+=4
 me,p=cdi_u(b,p,nr);va,p=cdi_u(b,p,nr)
 fl=[]
 for _ in range(nr):v,p=vr(b,p);fl.append(v)
 out=[];r=0
 for k in range(n):
  if k==0:out.append(hd);continue
  if k in exc:out.append(exc[k]);continue
  out.append(b'%d,%d.%d.%d.%d,%s,%s,%d'%(ts[r],ip[r][0],ip[r][1],ip[r][2],ip[r][3],me[r],va[r],fl[r]));r+=1
 return b'\n'.join(out)
def logse2(lines,o,wid):
 rec=[];exc=[]
 for k,Lx in enumerate(lines):
  ok=True
  for w in Lx.rstrip(b'.').split(b' '):
   if w not in wid:ok=False;break
  if ok:rec.append((k,Lx))
  else:exc.append((k,Lx))
 if not rec:return False
 vi(len(lines),o);vi(len(exc),o)
 for k,Lx in exc:vi(k,o);vi(len(Lx),o);o+=Lx
 vi(len(rec),o)
 for k,Lx in rec:
  dot=1 if Lx.endswith(b'.')else 0
  L2=Lx[:-1]if dot else Lx
  w=L2.split(b' ');vi(len(w),o);o.append(dot)
  for x in w:vi(wid[x],o)
 return True
def logsd2(b,dw):
 p=0;n,p=vr(b,p);ne,p=vr(b,p);exc={}
 for _ in range(ne):
  k,p=vr(b,p);l,p=vr(b,p);exc[k]=b[p:p+l];p+=l
 nr,p=vr(b,p);recs=[]
 for _ in range(nr):
  nw,p=vr(b,p);dot=b[p];p+=1
  w=[]
  for _ in range(nw):i,p=vr(b,p);w.append(dw[i])
  recs.append(b' '.join(w)+(b'.'if dot else b''))
 out=[];r=0
 for k in range(n):
  if k in exc:out.append(exc[k])
  else:out.append(recs[r]);r+=1
 return b'\n'.join(out)
def cnst_gen(e0,n):
 N=n+4
 return(isqrt((2,3,5,7)[e0]<<(16*N))%(1<<(8*N))).to_bytes(N,'big')[:n]
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
   k=bytes(km[p]for p in range(KP))
   pt=bytes(ct[j]^k[j%KP]for j in range(len(ct)))
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
def lpred(qq,Bt):
 y=0
 while qq:
  p=qq.bit_length()-1;vv=Bt[p]
  qq^=vv[0];y^=vv[1]
 return y
def mt_tables(Bt):
 T=[]
 for wi in range(4):
  for p in range(4):
   t=[0]*256
   for vv in range(1,256):
    lb=vv&-vv
    t[vv]=t[vv-lb]^lpred(1<<(32*wi+8*p+lb.bit_length()-1),Bt)
   T.append(t)
 return T
def mt_gen(words,nw,T):
 t0,t1,t2,t3,t4,t5,t6,t7=T[0],T[1],T[2],T[3],T[4],T[5],T[6],T[7]
 t8,t9,ta,tb,tc,td,te,tf=T[8],T[9],T[10],T[11],T[12],T[13],T[14],T[15]
 while len(words)<nw:
  i=len(words)-MT_N
  a=words[i];b=words[i+1];c=words[i+MT_M];d=words[i+MT_M+1]
  words.append(t0[a&255]^t1[(a>>8)&255]^t2[(a>>16)&255]^t3[a>>24]^t4[b&255]^t5[(b>>8)&255]^t6[(b>>16)&255]^t7[b>>24]^t8[c&255]^t9[(c>>8)&255]^ta[(c>>16)&255]^tb[c>>24]^tc[d&255]^td[(d>>8)&255]^te[(d>>16)&255]^tf[d>>24])
 return words
def mt_fit_check(payload):
 nw=len(payload)//4
 if nw<MT_N+700:return None
 words=[int.from_bytes(payload[j:j+4],"big")for j in range(0,4*nw,4)]
 Bt=[None]*128
 for i in range(500):
  qq=(words[i]|words[i+1]<<32|words[i+MT_M]<<64|words[i+MT_M+1]<<96)
  y=words[i+MT_N]
  while qq:
   bb=qq.bit_length()-1;vv=Bt[bb]
   if vv is None:Bt[bb]=(qq,y);break
   qq^=vv[0];y^=vv[1]
  if not qq and y:return None
 if any(vv is None for vv in Bt):return None
 T=mt_tables(Bt)
 pred=mt_gen(words[:MT_N],nw,T)
 for i in range(MT_N,nw):
  if pred[i]!=words[i]:return None
 return Bt
def bm(a):
 C=B=1;LL=0;m=-1;Hh=0
 for N,vv in enumerate(a):
  Hh=Hh<<1|(vv>>7)
  if(C&Hh).bit_count()&1:
   T=C;C^=B<<(N-m)
   if 2*LL<=N:LL=N+1-LL;B=T;m=N
 return C
def _wht(a):
 n=len(a);h=1
 while h<n:
  st=h<<1
  for i in range(0,n,st):
   for j in range(i,i+h):
    x=a[j];y=a[j+h];a[j]=x+y;a[j+h]=x-y
  h=st
def ml_key(hp,hc):
 tot=sum(hp)
 lp=[math.log((hp[b]+0.5)/(tot+128.0))for b in range(256)]
 wlp=lp[:];_wht(wlp)
 key=bytearray(251)
 for j in range(251):
  h=hc[j][:]
  if not any(h):continue
  _wht(h)
  for b in range(256):h[b]*=wlp[b]
  _wht(h)
  best=-1e300;bk=0
  for k in range(256):
   vv=h[k]
   if vv>best:best=vv;bk=k
  key[j]=bk
 return bytes(key)
def unmask(p,k):
 n=len(p);kp=k*(n//251+1)
 return bytes(a^b for a,b in zip(p,kp))
def rel_key(cts,lag):
 votes=[None]*251
 for ct in cts:
  nb=min(len(ct),160000)
  for j in range(nb-lag):
   a=j%251
   vv=votes[a]
   if vv is None:vv=votes[a]=[0]*256
   vv[ct[j]^ct[j+lag]]+=1
 rel=[]
 for a in range(251):
  if votes[a]:
   vv=votes[a];m=max(range(256),key=lambda x:vv[x])
   rel.append((a,(a+lag)%251,m))
 Kc=[None]*251;Kc[0]=0
 changed=True
 while changed:
  changed=False
  for a,b,m in rel:
   if Kc[a]is not None and Kc[b]is None:Kc[b]=Kc[a]^m;changed=True
   elif Kc[b]is not None and Kc[a]is None:Kc[a]=Kc[b]^m;changed=True
 if any(x is None for x in Kc):return None
 return Kc
def pick_rel_key(cts,s0,hp,kml,ref):
 tot=sum(hp)+256
 logp=[math.log((hp[b]+1)/tot)for b in range(256)]
 def zc(K):return len(Z.compress(unmask(s0,K),6))
 best=zc(kml);bestk=None
 nb2=min(40000,len(ref)-5)
 lags=sorted((1,2,3,4),key=lambda Lg:-sum(1 for j in range(0,nb2,7)if ref[j]==ref[j+Lg]))
 for lag in lags[:2]:
  Kc=rel_key(cts,lag)
  if Kc is None:continue
  gbest=None
  for gc in range(256):
   pt=bytes(a^b^gc for a,b in zip(s0[:8192],Kc))
   sc=sum(logp[b]for b in pt)
   if gbest is None or sc>gbest[0]:gbest=(sc,gc)
  K=bytes(x^gbest[1]for x in Kc)
  z=zc(K)
  if z<best:best=z;bestk=K
 return bestk
F={(b'IMG ',655360):bytes.fromhex('ff202121ff2420222728252aff2b2424'),(b'CA30',253952):bytes.fromhex('ff2020ff23ff4323ff242348222c2c25264724'),(b'DUP ',174784):bytes.fromhex('ffffffff'),(b'WAVE',131090):bytes.fromhex('ffffff212124ff2327'),(b'SEQ2',174784):bytes.fromhex('64ff2421ffff'),(b'SEQ2',149991):bytes.fromhex('21ffff')}
def f(p,e):
 k=e&7
 if k==2:return bytes((b-(i%256))&255 for i,b in enumerate(p))
 if k==3:s=[2,3,4,7][e>>3];return b''.join(p[i::s]for i in range(s))
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
 for i in range(m):x=a[i];a.append(i-l[x]if x in l else 0);l[x]=i
 return a
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
def J(dd):
 o=80;r=[]
 while o<len(dd):n=int.from_bytes(dd[o:o+4],'big');r.append([dd[o+4:o+8],dd[o+8],dd[o+9],n,dd[o+10:o+10+n]]);o+=14+n
 return r
ZB={'id':33,'preset':9,'nice_len':128,'dict_size':1<<26}
Z0=dict(ZB);Z0.update({'lc':0,'lp':0,'pb':0})
Z1=dict(ZB);Z1.update({'lc':1,'lp':0,'pb':0})
ZFIL=[ZB,Z0,None,None,Z1]
def _sel_pack(x,c):
 if c==2:return Z.compress(x,9)
 if c==3:return bz2.compress(x,9)
 ff=dict(ZFIL[c]);ff['preset']=6;ff['nice_len']=64;ff['dict_size']=1<<24
 return L.compress(x,format=3,filters=[ff])
def choose_codec(blk):
 n=len(blk)
 if n<=131072:sample=blk
 else:
  w=min(262144,max(16384,n//8));sample=blk[:w]+blk[n//2:n//2+w]+blk[n-w:]
 best,bc=None,0
 for c in range(5):
  try:sz=len(_sel_pack(sample,c))
  except Exception:continue
  if best is None or sz<best:best,bc=sz,c
 return bc
def pack(x,c):
 if c==2:return Z.compress(x,9)
 if c==3:return bz2.compress(x,9)
 return L.compress(x,format=3,filters=[ZFIL[c]])
def unpack(y,c):
 if c==2:return Z.decompress(y)
 if c==3:return bz2.decompress(y)
 return L.decompress(y,format=3,filters=[ZFIL[c]])
XT_NAMES=('raw','lane2','lane4','x1','x2','d1','d2','mpack')
def x_lane(b,w):return b''.join(b[i::w]for i in range(w))
def x_unlane(b,w):
 n=len(b);out=bytearray(n);q=0
 for i in range(w):
  m=len(range(i,n,w));out[i::w]=b[q:q+m];q+=m
 return bytes(out)
def x_xor(b,Lp):
 Ai=int.from_bytes(b,'big')
 return((Ai^(Ai<<(8*Lp)))>>(8*Lp)).to_bytes(len(b),'big')
def x_uxor(b,Lp):
 n=len(b);out=bytearray(b)
 for i in range(Lp,n):out[i]=b[i]^out[i-Lp]
 return bytes(out)
def x_delta(b,Lp):return b[:Lp]+bytes((b[i]-b[i-Lp])&255 for i in range(Lp,len(b)))
def x_undelta(b,Lp):
 n=len(b);out=bytearray(b)
 for i in range(Lp,n):out[i]=(b[i]+out[i-Lp])&255
 return bytes(out)
def xfwd(b,k):
 nm=XT_NAMES[k]
 if nm=='raw':return b
 if nm=='mpack':
  if not b or min(b)<0 or max(b)>1:return b
  out=bytearray(len(b));out[0]=2
  for i,vv in enumerate(b):
   if vv:out[1+(i>>3)]|=1<<(i&7)
  return bytes(out)
 if nm.startswith('lane'):return x_lane(b,int(nm[4:]))
 if nm.startswith('x'):return x_xor(b,int(nm[1:]))
 return x_delta(b,int(nm[1:]))
def xbwd(b,k):
 nm=XT_NAMES[k]
 if nm=='raw':return b
 if nm=='mpack':
  if not b or b[0]!=2:return b
  n=len(b);out=bytearray(n)
  for i in range(n):
   if b[1+(i>>3)]>>(i&7)&1:out[i]=1
  return bytes(out)
 if nm.startswith('lane'):return x_unlane(b,int(nm[4:]))
 if nm.startswith('x'):return x_uxor(b,int(nm[1:]))
 return x_undelta(b,int(nm[1:]))
XZ=[{'id':33,'preset':6,'nice_len':64,'dict_size':1<<24}]
def xscore(b):return len(Z.compress(b,6))
def xpick(blk):
 n=len(blk)
 if n<4096:return 0
 w=min(16384,max(4096,n//8))
 if 4*w<n:small=blk[:w]+blk[n//3:n//3+w]+blk[2*n//3:2*n//3+w]+blk[n-w:]
 else:small=blk
 scored=sorted((xscore(xfwd(small,k)),k)for k in range(len(XT_NAMES)))
 top=[k for _,k in scored[:4]]
 best,bk=None,top[0]
 for k in top:
  try:sc=len(L.compress(xfwd(blk,k),format=3,filters=XZ))
  except Exception:sc=1<<30
  if best is None or sc<best:best,bk=sc,k
 return bk
SKIP={b'PRNG',b'LOGS',b'SPRS',b'NOIZ',b'CA30',b'A181',b'MTST',b'DUP ',b'SEQ2'}
def C(s,p):
 y=B.b64decode(open(s,'rb').read());c=J(y);pk=bytearray(KP)
 for x in c:
  if x[0]==b'PRNG'and x[2]&7==1:
   kk=lck(x[4])
   if kk:pk=bytearray(kk);break
 for x in c:x[4]=f(x[4],x[2])
 for x in c:
  if x[2]&7==1:
   if x[0]==b'PRNG':x[4]=bytes(a^pk[k%KP]for k,a in enumerate(x[4]))
   elif x[0]==b'LOGS':x[4]=bytes(a^LK[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'SPRS':x[4]=bytes(a^K_SPRS[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'NOIZ':x[4]=bytes(a^K_NOIZ[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'CA30':x[4]=bytes(a^KCA[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'SEQ2'and x[3]==149991:x[4]=bytes(a^KS2[k%251]for k,a in enumerate(x[4]))
 groups={}
 for i,x in enumerate(c):groups.setdefault((x[0],x[3]),[]).append(i)
 keytab=bytearray()
 for g in sorted(groups):
  if g[0]in SKIP:continue
  ids=groups[g]
  hid=[i for i in ids if c[i][2]&7==1]
  pln=[i for i in ids if c[i][2]&7!=1]
  if not hid or not pln:continue
  hp=[0]*256
  for i in pln:
   for b in c[i][4][:2048]:hp[b]+=1
  hc=[[0]*256 for _ in range(251)]
  for i in hid:
   pp=c[i][4]
   for j in range(min(len(pp),251*1024)):hc[j%251][pp[j]]+=1
  k=ml_key(hp,hc)
  if g[0]in{b'IMG ',b'WAVE',b'HASH'}:
   cts=[bytes(c[i][4])for i in hid[:2]];s0=cts[0][:49152]
   kc=pick_rel_key(cts,s0,hp,k,bytes(c[pln[0]][4]))
   if kc:k=kc
  keytab+=k
  for i in hid:c[i][4]=unmask(c[i][4],k)
 pr=[]
 for i,x in enumerate(c):
  if x[0]!=b'PRNG':continue
  w=int.from_bytes(x[4][:8],'little')
  if x[1]==1:
   ss=w;chk=bytearray()
   for _ in range(x[3]//8):chk+=ss.to_bytes(8,'little');ss=(A*ss+G)&M
   if chk[:x[3]]==x[4]:pr.append(i)
  else:
   ss=q(w);chk=bytearray()
   for _ in range(x[3]//8):r=Y(ss);chk+=(r*X&M).to_bytes(8,'little');ss=r
   if chk[:x[3]]==x[4]:pr.append(i)
 prm=bytearray(32)
 for i in pr:prm[i>>3]|=1<<(i&7)
 cm=bytearray(32)
 for i,x in enumerate(c):
  if x[0]==b'CNST'and x[1]<=3and x[3]==16383and cnst_gen(x[1],x[3])==x[4]:cm[i>>3]|=1<<(i&7)
 cn=[i for i in range(len(c))if cm[i>>3]&(1<<(i&7))]
 mt4r=[];mt4_basis=None;mt1r=[];bm_c=None
 for i,x in enumerate(c):
  if x[0]!=b'MTST':continue
  if x[2]&7==4:
   raw=I(x[4],x[2]);BB=mt_fit_check(raw)
   if BB is None:continue
   mt4r.append(i)
   if mt4_basis is None:mt4_basis=BB
  elif x[2]&7==1:mt1r.append(i)
 if mt1r:bm_c=bm(c[mt1r[0]][4][0::4][:2*MT_L1+100])
 syl_words_list=[];syl_wid={}
 for i,x in enumerate(c):
  if x[0]!=b'LOGS'or x[1]!=2:continue
  payload=x[4];strip=payload.rstrip(b'\n')
  for Lx in(strip.split(b'\n')if strip else[]):
   L2=Lx[:-1]if Lx.endswith(b'.')else Lx
   for w in L2.split(b' '):
    if w not in syl_wid:syl_wid[w]=len(syl_words_list);syl_words_list.append(w)
 lstream=bytearray();vi(len(syl_words_list),lstream)
 for w in syl_words_list:vi(len(w),lstream);lstream+=w
 lmask=bytearray(32);lids=set()
 for i,x in enumerate(c):
  if x[0]!=b'LOGS':continue
  payload=x[4];strip=payload.rstrip(b'\n');trail=len(payload)-len(strip)
  lines=strip.split(b'\n')if strip else[]
  sub=bytearray();vi(trail,sub);fmt=x[1];ok=False
  if fmt==0:ok=logse0(lines,sub)
  elif fmt==1:ok=logse1(lines,sub)
  elif fmt==2:ok=logse2(lines,sub,syl_wid)
  if ok:
   vi(len(sub),lstream);lstream+=sub
   lmask[i>>3]|=1<<(i&7);lids.add(i)
 h=[i for i,x in enumerate(c)if x[0]==b'HASH'and(x[2]==0 or i==255)]
 r30=[28,43,114,161,51,243,16,200,117]
 r110=[139,83,105,109]
 a181=[127,110,85,215,41,254,108,191,130,118,129,138,147,169,196,24,171,9,250,228,253,78,132,198,236,186,100,144,86,112,155,207]
 s2r=[181,116];s2c=[182];s2a=[i for i,x in enumerate(c)if x[0]==b'SEQ2'and x[3]==31248]
 toc=[i for i,x in enumerate(c)if x[0]==b'TOC ']
 dup=[91,247,164,201,232,251,187,15,32,238,27,103,163,227]
 W=set(h+r30+r110+a181+s2r+s2c+s2a+mt4r+mt1r+toc+dup+pr+cn+list(lids))
 z=bytearray(b''.join(c[i][4][:32]for i in h))
 for i in mt4r:
  raw=I(c[i][4],c[i][2]);z+=raw[:MT_N*4]
 for i in mt1r:z+=c[i][4][:MT_L1*4]
 for i in pr:
  x=c[i][4];w=int.from_bytes(x[:8],'little')
  z+=(w if c[i][1]==1 else q(w)).to_bytes(8,'little')
 hdr=bytearray();hdr+=bytes((1 if mt4r else 0,))
 if mt4r:
  for qq,yy in mt4_basis:hdr+=qq.to_bytes(16,'big')+yy.to_bytes(4,'big')
 hdr+=bytes((1 if mt1r else 0,))
 if mt1r:hdr+=bm_c.to_bytes(MT_CW,'big')
 CI=80+256*10
 cinfo=b''.join(x[3].to_bytes(4,'big')+x[0]+bytes([x[1],x[2]])for x in c)
 meta=y[:80]+cinfo+bytes(hdr)+bytes(pk)+bytes(prm)+bytes(cm)+bytes(lmask)
 streams=[bytes(meta),bytes(z),bytes(keytab),bytes(lstream)];xforms=[0,0,0,0]
 for(t,n),plan in F.items():
  ids=[i for i,x in enumerate(c)if x[0]==t and x[3]==n and i not in W];W.update(ids);ZZ=bytearray()
  for j,code in enumerate(plan):
   x=c[ids[j]][4]
   if code!=255:x=d(x,c[ids[code&31]][4],code>>5)
   ZZ+=x
  blk=bytes(ZZ);tk=xpick(blk)
  if tk!=0:blk=xfwd(blk,tk)
  streams.append(blk);xforms.append(tk)
 g={}
 for i,x in enumerate(c):
  if i not in W:g.setdefault((x[0],0 if x[0]==b'LOGS'else x[3]),[]).append(i)
 K={b'LOGS':0,b'SPRS':2,b'NOIZ':5,b'SEQ2':3}
 for x in g.values():
  k=K.get(c[x[0]][0])
  if k is not None:x.sort(key=lambda i:(c[i][1],i),reverse=True)
 for ids in g.values():
  blk=b''.join(c[i][4]for i in ids);tk=xpick(blk)
  if tk!=0:blk=xfwd(blk,tk)
  streams.append(blk);xforms.append(tk)
 out=bytearray();out+=len(streams).to_bytes(2,'big')
 codecs=[choose_codec(s)for s in streams]
 hbits=bytes((codecs[i]<<4)|xforms[i]for i in range(len(streams)))
 hc=L.compress(hbits,format=3,filters=Q)
 out+=len(hc).to_bytes(4,'big')+hc
 for st,cc in zip(streams,codecs):
  yy=pack(st,cc);out+=len(yy).to_bytes(4,'big')+yy
 open(p,'wb').write(bytes(out))
def D(s,p):
 y=open(s,'rb').read();nb=int.from_bytes(y[:2],'big');hc_len=int.from_bytes(y[2:6],'big')
 hbits=L.decompress(y[6:6+hc_len],format=3,filters=Q);o=6+hc_len;streams=[]
 for i in range(nb):
  cc=hbits[i]>>4;tk=hbits[i]&15
  n=int.from_bytes(y[o:o+4],'big');comp=y[o+4:o+4+n];o+=4+n
  st=unpack(comp,cc)
  if tk!=0:st=xbwd(st,tk)
  streams.append(st)
 bi=0;meta=streams[bi];bi+=1;z=streams[bi];bi+=1;keytab=streams[bi];bi+=1;lstream=streams[bi];bi+=1
 h0=meta[:80];CI=80+256*10
 lmask=meta[-32:];cm=meta[-64:-32];prm=meta[-96:-64];pk=meta[-347:-96]
 hdrend=len(meta)-347;hdr=meta[CI:hdrend]
 hp=0;has_mt4r=hdr[hp];hp+=1;basis=[]
 if has_mt4r:
  for _ in range(128):basis.append((int.from_bytes(hdr[hp:hp+16],'big'),int.from_bytes(hdr[hp+16:hp+20],'big')));hp+=20
 has_mt1=hdr[hp];hp+=1;bm_taps=[]
 if has_mt1:
  bm_c=int.from_bytes(hdr[hp:hp+MT_CW],'big');hp+=MT_CW
  bm_taps=[k for k in range(1,MT_L1+1)if(bm_c>>k)&1]
 c=[]
 for qq in range(80,CI,10):
  n=int.from_bytes(meta[qq:qq+4],'big');T=meta[qq+4:qq+8];e0=meta[qq+8];e1=meta[qq+9];c.append([T,e0,e1,n,None])
 lp=0;nd,lp=vr(lstream,lp);syl_words_list=[]
 for _ in range(nd):
  l,lp=vr(lstream,lp);syl_words_list.append(lstream[lp:lp+l]);lp+=l
 lids=set()
 for i,x in enumerate(c):
  if x[0]!=b'LOGS':continue
  if not(lmask[i>>3]&(1<<(i&7))):continue
  nb2,lp=vr(lstream,lp);sub=lstream[lp:lp+nb2];lp+=nb2
  q2=0;trail,q2=vr(sub,q2);fmt=x[1]
  if fmt==0:payload=logsd0(sub[q2:])
  elif fmt==1:payload=logsd1(sub[q2:])
  else:payload=logsd2(sub[q2:],syl_words_list)
  c[i][4]=payload+b'\n'*trail;lids.add(i)
 h=[i for i,x in enumerate(c)if x[0]==b'HASH'and(x[2]==0 or i==255)]
 r30=[28,43,114,161,51,243,16,200,117]
 r110=[139,83,105,109]
 a181=[127,110,85,215,41,254,108,191,130,118,129,138,147,169,196,24,171,9,250,228,253,78,132,198,236,186,100,144,86,112,155,207]
 s2r=[181,116];s2c=[182];s2a=[i for i,x in enumerate(c)if x[0]==b'SEQ2'and x[3]==31248]
 toc=[i for i,x in enumerate(c)if x[0]==b'TOC ']
 dup=[91,247,164,201,232,251,187,15,32,238,27,103,163,227]
 pr=[i for i in range(len(c))if prm[i>>3]&(1<<(i&7))]
 cn=[i for i in range(len(c))if cm[i>>3]&(1<<(i&7))]
 mt4r=[i for i,x in enumerate(c)if x[0]==b'MTST'and x[2]&7==4]
 mt1r=[i for i,x in enumerate(c)if x[0]==b'MTST'and x[2]&7==1]
 W=set(h+r30+r110+a181+s2r+s2c+s2a+mt4r+mt1r+toc+dup+pr+cn+list(lids))
 for i in h:
  seed=z[:32];z=z[32:];n=c[i][3];h2=seed;x=bytearray(h2)
  while len(x)<n:h2=H.sha256(h2).digest();x+=h2
  c[i][4]=bytes(x[:n])
 Tt=mt_tables(basis)if has_mt4r else None
 for i in mt4r:
  n=c[i][3];raw=z[:MT_N*4];z=z[MT_N*4:]
  words=[int.from_bytes(raw[j:j+4],'big')for j in range(0,MT_N*4,4)]
  words=mt_gen(words,n//4,Tt)
  c[i][4]=b''.join(w.to_bytes(4,'big')for w in words[:n//4])
 for i in mt1r:
  n=c[i][3];e=z[:4*MT_L1];z=z[4*MT_L1:]
  x=bytearray(n);nw=n//4
  for k in range(4):
   y2=bytearray(e[k:4*MT_L1:4]);y2+=bytearray(nw-MT_L1)
   j=MT_L1
   while j<nw:
    vv=0
    for qq in bm_taps:vv^=y2[j-qq]
    y2[j]=vv;j+=1
   x[k::4]=y2
  c[i][4]=bytes(x)
 for i in pr:
  ss=int.from_bytes(z[:8],'little');z=z[8:];n=c[i][3];o2=bytearray()
  if c[i][1]==1:
   while len(o2)<n:o2+=ss.to_bytes(8,'little');ss=(A*ss+G)&M
  else:
   while len(o2)<n:r=Y(ss);o2+=(r*X&M).to_bytes(8,'little');ss=r
  c[i][4]=bytes(o2[:n])
 u_r30=g0()
 for i in r30:c[i][4]=u_r30
 u_r110=g1()
 for i in r110:c[i][4]=u_r110
 for idx,val in[(127,0),(110,1),(85,2),(215,3),(41,4),(254,5),(108,6),(191,7)]:
  num=c[idx][3]//4;u=V(val,num+1);c[idx][4]=val.to_bytes(4,'little')+b''.join(x.to_bytes(4,'little')for x in u[1:num])
 for idx,val in[(130,0),(118,1),(129,2),(138,3),(147,4),(169,5),(196,6),(24,7)]:
  num=c[idx][3]//4;u=V(val,num+2);diff=[u[k+1]-u[k]for k in range(1,num)]
  c[idx][4]=(-val).to_bytes(4,'little',signed=True)+b''.join(x.to_bytes(4,'little',signed=True)for x in diff)
 for idx,val in[(171,1),(9,3),(250,4),(228,5),(253,6),(78,7),(155,2),(207,0)]:
  num=(c[idx][3]-4)//2;u=V(val,num+5);c[idx][4]=val.to_bytes(4,'little')+b''.join((x&65535).to_bytes(2,'little')for x in u[2:num+2])
 for idx,val in[(132,0),(198,1),(236,3),(186,5),(100,6),(144,7),(86,2),(112,4)]:
  num=(c[idx][3]-4)//3;u=V(val,num*2+5);terms=u[3:3+num*2+2]
  gen=bytearray(b'\x00\x00\x00\x01'if val==0 else val.to_bytes(4,'little'))
  for k in range(num):gen.extend([((terms[2*k]&15)<<4)|((terms[2*k-1]>>8)&15 if k>0 else 0),(terms[2*k]>>4)&255,terms[2*k+1]&255])
  lt=terms[num*2];gen.extend([((lt&15)<<4)|((terms[num*2-1]>>8)&15),(lt>>4)&255]);c[idx][4]=bytes(gen)
 for i in[86,112,155,207]:c[i][4]=bytes(a^AK[k%251]for k,a in enumerate(c[i][4]))
 u_rc=bytearray((0).to_bytes(4,'little'));ss={0};vv=0
 for k in range(1,124992//4):x=vv-k;vv=x if x>0 and x not in ss else vv+k;ss.add(vv);u_rc+=vv.to_bytes(4,'little')
 c[181][4]=bytes(u_rc);c[116][4]=bytes(u_rc)
 m_map={1:0};r_cl=bytearray((0).to_bytes(4,'little'))
 for n in range(1,249984//4):
  c_val=n;qq=[]
  while c_val not in m_map:qq.append(c_val);c_val=c_val//2 if c_val%2==0 else 3*c_val+1
  b_val=m_map[c_val]
  for j,vv in enumerate(reversed(qq)):m_map[vv]=b_val+j+1
  r_cl+=m_map[n].to_bytes(4,'little')
 c[182][4]=bytes(r_cl);c[37][4]=b'\xff'*31248
 c[4][4]=bytes([127])+b'\xff'*31247;c[64][4]=bytes([127])+b'\xff'*31247
 r_toc=bytearray((80).to_bytes(4,'big'));cur=80
 for x in c[:-1]:cur+=14+x[3];r_toc+=cur.to_bytes(4,'big')
 for i in toc:c[i][4]=bytes(r_toc)
 for i in cn:c[i][4]=cnst_gen(c[i][1],c[i][3])
 for(t,n),plan in F.items():
  ids=[i for i,x in enumerate(c)if x[0]==t and x[3]==n and i not in W];W.update(ids);x=streams[bi];bi+=1
  rawn=[x[j*n:(j+1)*n]for j in range(len(ids))];done=[None]*len(ids)
  def gget(j):
   if done[j]is None:
    code=plan[j];done[j]=rawn[j]if code==255 else U(rawn[j],gget(code&31),code>>5)
   return done[j]
  for j,i in enumerate(ids):c[i][4]=gget(j)
 g={}
 for i,x in enumerate(c):
  if i not in W:g.setdefault((x[0],0 if x[0]==b'LOGS'else x[3]),[]).append(i)
 K={b'LOGS':0,b'SPRS':2,b'NOIZ':5,b'SEQ2':3}
 for x in g.values():
  k=K.get(c[x[0]][0])
  if k is not None:x.sort(key=lambda i:(c[i][1],i),reverse=True)
 for ids in g.values():
  x=streams[bi];bi+=1;q=0
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
 groups={}
 for i,x in enumerate(c):groups.setdefault((x[0],x[3]),[]).append(i)
 gi=0
 for g in sorted(groups):
  if g[0]in SKIP:continue
  ids=groups[g]
  hid=[i for i in ids if c[i][2]&7==1]
  pln=[i for i in ids if c[i][2]&7!=1]
  if not hid or not pln:continue
  k=keytab[gi*251:(gi+1)*251];gi+=1
  for i in hid:c[i][4]=unmask(c[i][4],k)
 for x in c:
  if x[2]&7==1:
   if x[0]==b'PRNG':x[4]=bytes(a^pk[k%KP]for k,a in enumerate(x[4]))
   elif x[0]==b'LOGS':x[4]=bytes(a^LK[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'SPRS':x[4]=bytes(a^K_SPRS[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'NOIZ':x[4]=bytes(a^K_NOIZ[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'CA30':x[4]=bytes(a^KCA[k%251]for k,a in enumerate(x[4]))
   elif x[0]==b'SEQ2'and x[3]==149991:x[4]=bytes(a^KS2[k%251]for k,a in enumerate(x[4]))
 for i,x in enumerate(c):
  if i in mt4r or i in mt1r:continue
  x[4]=I(x[4],x[2])
 out=bytearray(h0)
 for x in c:
  crc=Z.crc32(x[0]+bytes([x[1],x[2]])+x[4]).to_bytes(4,'big')
  out+=x[3].to_bytes(4,'big')+x[0]+bytes([x[1],x[2]])+x[4]+crc
 open(p,'wb').write(B.b64encode(out))
if __name__=='__main__':(C if S.argv[1]=='--compress'else D)(S.argv[2],S.argv[3])
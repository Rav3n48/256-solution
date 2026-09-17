import sys as S,base64 as B,lzma as L,zlib as Z,hashlib as H
Q=[{'id':33,'preset':9,'nice_len':128}]
M=(1<<64)-1;X=0x2545F4914F6CDD1D;A=0x5851f42d4c957f2d;G=0x14057b7ef767814f
def Y(x):x^=x>>12;x^=(x<<25)&M;x^=x>>27;return x&M
def v(y,s):
 x=y
 for _ in range(8):x=y^(x>>s)
 return x&M
def q(o):
 x=(o*pow(X,-1,1<<64))&M
 x=v(x,27);x^=(x<<25)&M;x^=(x<<50)&M;x=v(x,12)
 return x&M
F={(b'IMG ',655360):bytes.fromhex('ff202121ff2420222728252aff2b2424'),(b'CA30',253952):bytes.fromhex('ff2020ff23ff4323ff242348222c2c25264724'),(b'A181',237600):bytes.fromhex('ffff2021'),(b'DUP ',174784):bytes.fromhex('ffffffffffffffff'),(b'WAVE',131090):bytes.fromhex('ffffff212124ff2327'),(b'SEQ2',174784):bytes.fromhex('64ff2421ffff'),(b'SEQ2',149991):bytes.fromhex('21ffff')}
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
 for x in c:x[4]=f(x[4],x[2])
 h=[i for i,x in enumerate(c) if x[0]==b'HASH' and(x[2]==0 or i==255)]
 r30=[28,43,114,161,51,243,16,200,117]
 r110=[139,83,105,109]
 a181=[127,110,85,215,41,254,108,191,130,118,129,138,147,169,196,24,171,9,250,228,253,78,132,198,236,186,100,144]
 s2r=[181,116];s2c=[182];s2a=[i for i,x in enumerate(c) if x[0]==b'SEQ2' and x[3]==31248]
 mt=[i for i,x in enumerate(c) if x[0]==b'MTST']
 toc=[i for i,x in enumerate(c) if x[0]==b'TOC ']
 dup=[91,247,164,201,232,251,187,15,32,238]
 pr=[i for i,x in enumerate(c) if x[0]==b'PRNG' and(x[2]&7)!=1]
 W=set(h+r30+r110+a181+s2r+s2c+s2a+mt+toc+dup+pr)
 z=bytearray(b''.join(c[i][4][:32] for i in h))
 for m,L in [(1,20188),(4,19937)]:
  C=b(c[next(i for i in mt if c[i][2]==m)][4][0::4][:2*L+100])
  z+=C.to_bytes((L+8)//8,'big')
 for i in mt:L=20188 if c[i][2]==1 else 19937;x=c[i][4];z+=x[:4*L]
 for i in pr:
  x=c[i][4];w=int.from_bytes(x[:8],'little')
  z+=(w if c[i][1]==1 else q(w)).to_bytes(8,'little')
 meta=y[:80]+b''.join(x[3].to_bytes(4,'big')+x[0]+bytes([x[1],x[2]]) for x in c)
 a(o,meta);a(o,z)
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
 y=open(s,'rb').read();meta,o=R(y,0);h0=meta[:80];c=[]
 for q in range(80,len(meta),10):
  n=int.from_bytes(meta[q:q+4],'big');T=meta[q+4:q+8];e0=meta[q+8];e1=meta[q+9];c.append([T,e0,e1,n,None])
 z,o=R(y,o)
 h=[i for i,x in enumerate(c) if x[0]==b'HASH' and(x[2]==0 or i==255)]
 r30=[28,43,114,161,51,243,16,200,117]
 r110=[139,83,105,109]
 a181=[127,110,85,215,41,254,108,191,130,118,129,138,147,169,196,24,171,9,250,228,253,78,132,198,236,186,100,144]
 s2r=[181,116];s2c=[182];s2a=[i for i,x in enumerate(c) if x[0]==b'SEQ2' and x[3]==31248]
 mt=[i for i,x in enumerate(c) if x[0]==b'MTST']
 toc=[i for i,x in enumerate(c) if x[0]==b'TOC ']
 dup=[91,247,164,201,232,251,187,15,32,238]
 pr=[i for i,x in enumerate(c) if x[0]==b'PRNG' and(x[2]&7)!=1]
 W=set(h+r30+r110+a181+s2r+s2c+s2a+mt+toc+dup+pr)
 for i in h:
  seed=z[:32];z=z[32:];n=c[i][3];h2=seed;x=bytearray(h2)
  while len(x)<n:h2=H.sha256(h2).digest();x+=h2
  c[i][4]=bytes(x[:n])
 P={}
 for m,L in [(1,20188),(4,19937)]:w=(L+8)//8;C=int.from_bytes(z[:w],'big');z=z[w:];P[m]=(L,[k for k in range(1,L+1) if(C>>k)&1])
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
 for idx,val in [(171,1),(9,3),(250,4),(228,5),(253,6),(78,7)]:
  num=(c[idx][3]-4)//2;u=V(val,num+5);c[idx][4]=val.to_bytes(4,'little')+b''.join((x&65535).to_bytes(2,'little') for x in u[2:num+2])
 for idx,val in [(132,0),(198,1),(236,3),(186,5),(100,6),(144,7)]:
  num=(c[idx][3]-4)//3;u=V(val,num*2+5);terms=u[3:3+num*2+2];gen=bytearray(b'\x00\x00\x00\x01' if val==0 else val.to_bytes(4,'little'))
  for k in range(num):gen.extend([((terms[2*k]&15)<<4)|((terms[2*k-1]>>8)&15 if k>0 else 0),(terms[2*k]>>4)&255,terms[2*k+1]&255])
  lt=terms[num*2];gen.extend([((lt&15)<<4)|((terms[num*2-1]>>8)&15),(lt>>4)&255]);c[idx][4]=bytes(gen)
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
 for x in c:x[4]=I(x[4],x[2])
 out=bytearray(h0)
 for x in c:
  crc=Z.crc32(x[0]+bytes([x[1],x[2]])+x[4]).to_bytes(4,'big')
  out+=x[3].to_bytes(4,'big')+x[0]+bytes([x[1],x[2]])+x[4]+crc
 open(p,'wb').write(B.b64encode(out))
if __name__=='__main__':(C if S.argv[1]=='--compress' else D)(S.argv[2],S.argv[3])
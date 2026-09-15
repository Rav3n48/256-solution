import sys,base64,lzma
F=[{"id":lzma.FILTER_LZMA2,"preset":9|lzma.PRESET_EXTREME}]
def c(i,o):
 r=open(i,"rb").read();m,p=0,r
 try:
  d=base64.b64decode(r)
  if base64.b64encode(d)==r:m,p=1,d
 except:pass
 open(o,"wb").write(bytes([m])+lzma.compress(p,format=lzma.FORMAT_RAW,filters=F))
def d(i,o):
 x=open(i,"rb").read();m,b=x[0],x[1:]
 p=lzma.decompress(b,format=lzma.FORMAT_RAW,filters=F)
 open(o,"wb").write(base64.b64encode(p) if m else p)
_,a,i,o=sys.argv
(c if a=="--compress" else d)(i,o)
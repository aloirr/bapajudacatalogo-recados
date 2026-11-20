import sys, os, numpy as np
from PIL import Image, ImageDraw, ImageFilter
B='/tmp/claude-0/-home-user/f35995b2-1348-5e13-9156-210bf9deaa19/scratchpad/t18/op4e/'
def recorte(f):
    im=Image.open(B+f).convert('RGBA')
    if f.endswith('.png') and np.array(im)[...,3].min()<250:
        return im.crop(im.getbbox())
    a=np.array(im).astype(int); rgb=a[...,:3]
    mn=rgb.min(2); mx=rgb.max(2)
    m=((mn>236)&(mx-mn<20)).astype(np.uint8)*255
    m=m>0; r=np.zeros_like(m); r[0,:]=m[0,:]; r[-1,:]=m[-1,:]; r[:,0]=m[:,0]; r[:,-1]=m[:,-1]
    while True:
        n=r.copy(); n[1:]|=r[:-1]; n[:-1]|=r[1:]; n[:,1:]|=r[:,:-1]; n[:,:-1]|=r[:,1:]; n&=m
        if (n==r).all(): break
        r=n
    bg=r
    al=Image.fromarray(np.where(bg,0,255).astype(np.uint8),'L').filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.1))
    im.putalpha(al)
    return im.crop(al.point(lambda v:255 if v>20 else 0).getbbox())
def compor(itens,W,H,saida):
    can=Image.new('RGBA',(W,H),(0,0,0,0))
    for f,alt,cx,base,sh in itens:   # de trás para a frente
        p=recorte(f); r=alt/p.height; p=p.resize((max(1,int(p.width*r)),alt),Image.LANCZOS)
        x=int(cx-p.width/2); y=int(base-alt)
        if sh:
            s=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(s)
            ew=p.width*0.86; eh=max(14,p.width*0.09)
            d.ellipse((cx-ew/2,base-eh*0.55,cx+ew/2,base+eh*0.45),fill=(0,0,0,int(255*sh)))
            can.alpha_composite(s.filter(ImageFilter.GaussianBlur(10)))
        can.alpha_composite(p,(x,y))
    bb=can.getbbox(); can=can.crop((max(0,bb[0]-6),max(0,bb[1]-6),min(W,bb[2]+6),min(H,bb[3]+6)))
    for q in (82,76,70,64,58):
        can.save(saida,'WEBP',quality=q,method=6,alpha_quality=80)
        if os.path.getsize(saida)<=120*1024: break
    print(saida,can.size,os.path.getsize(saida)//1024,'KB q',q)
    can.save(saida.replace('.webp','_prev.png'))
A=[ # (arquivo, altura px, centro x, base y, sombra)
 ('img/AMT7183.jpg',440,240,455,.35),
 ('assets/card3.png',290,850,410,.35),
 ('img/KAP11846D.jpg',260,470,500,.4),
 ('img/60D-TF-24.jpg',280,690,600,.5),
 ('img/SFR30019.jpg',210,250,650,.45),
 ('img/CIL8524.jpg',185,960,650,.45),
]
Bv=[
 ('assets/card3.png',290,320,370,.35),
 ('img/AMT7183.jpg',470,850,495,.35),
 ('img/60D-EFB-24.jpg',270,320,580,.5),
 ('img/KAP11846D.jpg',260,640,560,.4),
 ('img/CIL8524.jpg',185,555,640,.45),
 ('img/SFR30019.jpg',205,870,645,.45),
]
compor(A,1200,680,sys.argv[1]); compor(Bv,1200,680,sys.argv[2])

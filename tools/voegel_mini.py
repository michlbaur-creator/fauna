# Vorschaubilder images/tafeln/mini/<slug>.jpg (400x300) aus den Tafeln: großer Vogel oben links,
# Beschriftung (MÄNNCHEN, ADULTTIER …) wird überdeckt. Aufruf im fauna-Ordner: python3 tools/voegel_mini.py
# Danach Kontaktbogen prüfen; bei Enten mit langer Beschriftung ggf. tiefer ansetzen (Stock-/Tafelente: y 158/166).
import json, os
import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import uniform_filter
T='images/tafeln/'; O='images/tafeln/mini/'
os.makedirs(O, exist_ok=True)
def mini(slug):
    im=Image.open(T+slug+'.jpg').convert('RGB')
    labs=[]
    for _ in range(3):
        lab=finde(im)
        if not lab: break
        ImageDraw.Draw(im).rectangle(lab, fill=(255,255,255)); labs.append(lab)
    c=im.crop((18,116,18+340,116+255)).resize((400,300),Image.LANCZOS)
    c.save(O+slug+'.jpg',quality=80,optimize=True,progressive=True)
    return labs or None
def finde(im):
    g=np.asarray(im.convert('L')).astype(float)
    Y0,Y1,X0,X1=96,190,20,395
    sub=g[Y0:Y1,X0:X1]
    white=(sub>232).astype(float); wf=uniform_filter(white,size=7)
    cand=(sub<95)&(wf>0.45)
    rows=cand.sum(axis=1)
    lab=None
    best=None
    for y in range(len(rows)-10):
        s=rows[y:y+14].sum()
        if best is None or s>best[0]: best=(s,y)
    if best and best[0]>40:
        y=best[1]; band=cand[y:y+14]
        cols=np.nonzero(band.sum(axis=0)>0)[0]
        # größte zusammenhängende Spaltengruppe (Lücken < 14 px)
        groups=[]; start=prev=cols[0]
        for c in cols[1:]:
            if c-prev>14: groups.append((start,prev)); start=c
            prev=c
        groups.append((start,prev))
        gx=max(groups,key=lambda t:t[1]-t[0])
        if 12<gx[1]-gx[0]<300:
            rr=np.nonzero(cand[:, gx[0]:gx[1]+1].sum(axis=1)>1)[0]
            ry=[r for r in rr if y-4<=r<=y+18]
            lab=(X0+gx[0]-3, Y0+min(ry)-3, X0+gx[1]+3, Y0+max(ry)+3)
    return lab
if __name__=='__main__':
    t=json.load(open('tiere.json')); sl=[x['slug'] for x in t if x.get('gruppe')=='Vögel' and os.path.exists(T+x['slug']+'.jpg')]
    miss=[s for s in sl if mini(s) is None]
    print(len(sl),'mini; ohne Label:',miss)

# --- zweiter Durchgang: Reste der Beschriftung im Vorschaubild entfernen ---
import os, numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import uniform_filter, label, binary_dilation, find_objects
O='images/tafeln/mini/'; n=0
for f in sorted(os.listdir(O)):
    im=Image.open(O+f).convert('RGB'); a=np.asarray(im).astype(float); g=a.mean(axis=2)
    H=48; sub=g[:H]
    wf=uniform_filter((sub>228).astype(float),size=7)
    cand=(sub<110)&(wf>0.4)
    lab,k=label(binary_dilation(cand,iterations=3))
    d=ImageDraw.Draw(im); hit=False
    for sl in find_objects(lab):
        ys,xs=sl; h=ys.stop-ys.start; w=xs.stop-xs.start
        if h>26 or w<6: continue
        box=sub[ys,xs]; wfrac=(box>228).mean()
        if wfrac<0.45: continue
        d.rectangle((xs.start-2,max(0,ys.start-2),xs.stop+2,ys.stop+2),fill=(255,255,255)); hit=True
    if hit: im.save(O+f,quality=80,optimize=True,progressive=True); n+=1; print(f)
print(n)

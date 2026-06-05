from PIL import Image, ImageDraw
import os
OUT = r"C:\Users\Gelo Camero\Piste"
BG=(14,15,19,255); PANEL=(23,25,34,255); CRIMSON=(230,57,79,255); STEEL=(170,182,205,255)
def make(size):
    img=Image.new("RGBA",(size,size),BG)
    d=ImageDraw.Draw(img)
    def P(x,y): return (int(x/512*size), int(y/512*size))
    w=lambda v:max(2,int(v/512*size))
    d.rounded_rectangle([P(36,36),P(476,476)], radius=int(70/512*size), fill=PANEL)
    # sabre blade
    d.line([P(150,378),P(392,150)], fill=CRIMSON, width=w(34))
    d.line([P(356,186),P(392,150)], fill=STEEL, width=w(34))  # tip highlight
    # guard
    d.ellipse([P(108,336),P(192,420)], outline=CRIMSON, width=w(18))
    # handle
    d.line([P(150,378),P(116,414)], fill=STEEL, width=w(24))
    img.save(os.path.join(OUT,"icon-%d.png"%size))
for sz in (192,512,180):
    make(sz)
print("icons done:", [f for f in os.listdir(OUT) if f.endswith('.png')])

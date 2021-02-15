I=print
from PIL import Image,ImageEnhance as G,ImageFilter as D
import PIL,random,sys
F=sys.argv[1]
def H(img,blur=50,sat=20,shrp=200,zoom=2,rot=1):B=zoom;A=img;C,E=A.size;A=A.resize((256,256));A=A.crop((B,B,256-B,256-B));A=A.resize((C,E));A=A.filter(D.GaussianBlur(radius=blur));A=A.filter(D.DETAIL());F=PIL.ImageEnhance.Color(A);A=F.enhance(sat);H=G.Sharpness(A);A=H.enhance(shrp);A=A.rotate(rot);return A
A=sys.argv[7]
B=[]
C=Image.open(F)
for E in range(A):
	if E%10==0:I('> {}% complete'.format(str(E/A*100)))
	C=H(C,shrp=int(sys.argv[6]),blur=int(sys.argv[5]),sat=float(sys.argv[4]),zoom=int(sys.argv[3]),rot=int(sys.argv[2]));B.append(C)
B[0].save('out.gif',format='GIF',append_images=B[1:],save_all=True,duration=int(A/15),loop=0)
I('out.gif saved')
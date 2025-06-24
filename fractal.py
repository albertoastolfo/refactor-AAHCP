from matplotlib.pyplot import *
from numpy import *
value = 2
max=value
min=-value
c=value
image_size = 1240
A=zeros((image_size, image_size))
for px in range(image_size):
 x0=(px/image_size)*(max-min)-value
 for py in range(image_size):
  y0=(py/image_size)*(max-min)-value
  x=0.0
  y=0.0
  it=0
  while (((x*x)+(y*y))<(c*c)) and it<256:
   xt=(x*x)-(y*y)+x0
   y=value*x*y+y0
   x=xt
   it=it+1
  A[px,py]=it
imshow(A)
show()
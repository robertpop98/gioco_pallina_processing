x1=30
y1=30
x=10
y=10
vx=1
vy=1
xr=0
yr=0
def setup():
    global xr
    size(800,400)
    xr=height-40
def draw():
    global x,y,vx,vy,x1,y1,xr,yr,r
    yr=(width/2)-25
    background(3,25,252)
    ellipse(x,y,x1,y1)
    rect(xr,yr,80,25)
    x=x+4*vx
    y=y+4*vy
    if (x>xr and x<xr+80 and y+y1/2>yr):
        vy=-1
    if x>width or x<0:
        vx*=-1
        fill (random(255),random(255),random(255))
    if y>height or y<0:
        vy*=-1
        fill (random(255),random(255),random(255))
    # if vx==-1:
    #     x1-=1
    #     y1-=1
    # if vx==1:
    #     x1+=1
    #     y1+=1
def keyPressed():
    global xr,yr
    if keyCode==LEFT and xr>0:
        xr-=10
    if keyCode==RIGHT and xr<width-80:
        xr+=10

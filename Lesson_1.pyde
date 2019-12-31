
"""
# Task 1
size(600, 480)
background(150, 150, 150)

stroke(0, 30, 60)
fill(255, 120, 0)

point(4, 3)
line(10, 2, 50, 200)

rect(200, 200, 50, 50)

ellipse(30, 30, 20, 45) # эллипс 
triangle(100, 50, 300, 450, 400, 200) # треугольник
arc(200, 300, 300, 300, PI/4, PI) # арка


stroke(100, 50, 150)
print("hello python")
happy = False
"""

# Task 1_2

x = 0
y = 0

def setup():
    size(800, 480)

def draw():
    global x, y
    line(x, y, 100, 100)
    x = x + 10


def setup():
    size(800, 480)

def draw():
    line(pmouseX, pmouseY, mouseX, mouseY)
    rect(mouseX, mouseY, 50, 50)
"""
# Task 2
background(240)    
# Maker Faire Robot
size(750, 600)

fill(255, 0, 0)

stroke(255, 0,0)

# head
arc(310, 230, 120, 120, PI, 2*PI)
fill(255)
stroke(255)
circle(285,205, 20) 
circle(330,205, 20)
fill(255,0,0)
stroke(255,0,0)

#левое плечо
arc(200, 360, 150, 170, PI, 1.5*PI) 
rect(145, 360, 35, 30)
quad(135,  380,  130, 450, 195, 450, 190, 380);

#правое плечо
arc(420, 360, 150, 170, 1.5*PI, TWO_PI) 
rect(440, 360, 35, 30)
quad(430,  380,  425, 450, 490, 450, 485, 380);

#тело
rect(220, 240, 180, 180, 20);
fill(255)
stroke(255)
circle(310,330, 100)
rect(220, 325, 180, 10)

# Task 3
textSize(72);
fill(255, 0, 0);
text("M", 280, 355); 

# left leg
stroke(255,0,0);
rect(250, 425, 50, 40)
quad(245, 470, 235, 520, 305,520,300, 470);

# right leg
rect(320, 425, 50, 40)
quad(320, 470, 315, 520, 390,520,375, 470);

"""

"""
# Task 4

n=4
surface_sz = 640          
sq_sz = surface_sz // n 
surface_sz = n * sq_sz  
                                   
def setup():
    size(surface_sz, surface_sz)
    noLoop() # draw() выполнится только один раз

def draw():
  
    for row in range(n):           
        for col in range(n):   
                fill(random(255), random(255), random(255));
                rect(col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                
                

# Task 5

n=4
pixels2D=[]
surface_sz = 640          
sq_sz = surface_sz // n
                                   
def setup():
    size(surface_sz, surface_sz)
    for row in range(n):     
        temp=[]      
        for col in range(n):
            coord=(col*sq_sz,row*sq_sz)
            temp.append(coord)
        pixels2D.append(temp)
            
    noLoop() # draw() выполнится только один раз
    
def draw():  
    for row in range(n):           
        for col in range(n):
            if row!=col:
                fill(random(255), random(255), random(255))
                rect(pixels2D[row][col][0], pixels2D[row][col][1],sq_sz, sq_sz)
            else:
                fill(255, 0,0)
                rect(pixels2D[row][col][0], pixels2D[row][col][1],sq_sz, sq_sz)


# Task 6

n=4
pixels2D=[]
surface_sz = 640          
sq_sz = surface_sz // n

def setup():
    size(surface_sz, surface_sz)
    for row in range(n):     
        temp=[]      
        for col in range(n):
            coord=(col*sq_sz,row*sq_sz)
            temp.append(coord)
        pixels2D.append(temp)
        
    redrawPixels(False)

def redrawPixels(isAllSameColor):
    fill(random(255), random(255), random(255))
    for row in range(n):           
        for col in range(n):
            if not isAllSameColor:
                fill(random(255), random(255), random(255))
            rect(pixels2D[row][col][0], pixels2D[row][col][1],sq_sz, sq_sz)
                    
def draw():
    i=mouseX/sq_sz
    j=mouseY/sq_sz
    if i==0 and j==0:
        redrawPixels(True)
"""
# Task 7

surface_sz=640
bColor = color(0);
bColorChanged=False
isDrew=False
def setup():
    size(surface_sz, surface_sz)  
   

def draw():
    global bColorChanged
    global isDrew
    global bColor
    
    if bColorChanged:
        background(bColor)        
        bColorChanged=False        
    
    if not isDrew:
        isDrew=True
        stroke(100)
        fill(100,255,0)        
        ellipse(150, 150, 50, 60);
        ellipse(300, 100, 200, 150);
        stroke(255)
        fill(255,0,0)
        
        for i in range(6):
            for j in range(6):
                stroke(random(255))
                line(i*random(surface_sz), i*random(640)+j*random(640), 0,0)
                
        for i in range(4):
            for j in range(4):
                stroke(random(255))
                fill(random(255))
                triangle(random(0, surface_sz/3), random(surface_sz/3*2, surface_sz/3), random(0, surface_sz/3*2), random(surface_sz/3, surface_sz/3*2), random(surface_sz/3*2, surface_sz), random(0, surface_sz))
    
        
   
def mousePressed(): 
    global bColorChanged
    global isDrew
    global bColor
    
    isDrew=False
    bColorChanged=True 
    if mouseY<height/2:
        bColor=color(255)
        print("top")
    else:
        print("bottom")
        bColor=color(0)

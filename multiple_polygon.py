from turtle import *
speed(-1)
socanh=4
pencolor("red")
forward(100)
for i in range(6):
    socanh_new=socanh+i
    for k in range(socanh_new):
        if k%2==0:
            pencolor("blue")
        else:
            pencolor("red")
        goc=180-((1-(2/socanh_new))*180)
        lt(goc)
        forward(100)
lt(180)
pencolor("red")
forward(100)

        
        
        
    
    
            

    

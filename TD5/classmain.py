from tkinter import Tk, Canvas,Button,TOP,BOTTOM,LEFT,RIGHT,Label
from random import random

WIDTH = 400        # Width of the window
HEIGHT = 400       # Height of the window
BULLET_RADIUS = 10 # radius of the bullets
D = 30             # Distance between circles
N = 6              # Number of circles on the target
BULLETS_SHOT = 5   # Number of bullets shot when "fire" is pressed

class targetGUI:

    def __init__(self):
        self.score = 0
        self.root = Tk()
        self.root.title("Shooting game")
        self.canvas = Canvas(self.root, bg='red', height=HEIGHT, width=WIDTH)
        self.canvas.pack(side=TOP)

        # Drawing the circles and the numbers
        for i in range(N):
            if i == N-2:
                textColour = "ivory"
                circleColour = "red"
            else:
                textColour = "red"
                circleColour = "ivory"
            self.canvas.create_oval(int(WIDTH/2-(N-1)*D-D/2+i*D), int(HEIGHT/2-(N-1)*D-D/2+i*D), int(WIDTH/2+(N-1)*D+D/2-i*D), int(HEIGHT/2+(N-1)*D+D/2-i*D), outline='red', fill=circleColour)
            self.canvas.create_text(WIDTH/2,HEIGHT/2-(N-1)*D+i*D,text= str(i+1),font=("Times","24","bold"),fill= textColour)
        
        # Drawing the axis of the target
        self.canvas.create_line(0,HEIGHT/2,WIDTH,HEIGHT/2, width=1, fill="red")
        self.canvas.create_line(WIDTH/2,0,WIDTH/2,HEIGHT, width=1, fill="red")

        # Placing the buttons and the labels
        self.quitButton = Button(self.root, text='Quitter',command=self.root.destroy)
        self.quitButton.pack(side=RIGHT)
    
        self.fire_but = Button(self.root, text='Feu !',command=lambda : self.fire(BULLETS_SHOT))
        self.fire_but.pack(side=LEFT)

        self.scoreLabel = Label(self.root, text=f"Score : {self.score}")
        self.scoreLabel.pack(side = BOTTOM)

        self.root.bind("<f>",lambda e: self.fire(1))
        self.root.mainloop()

    def drawBullet(self,x,y):
        self.canvas.create_oval(x-BULLET_RADIUS, y-BULLET_RADIUS, x+BULLET_RADIUS, y+BULLET_RADIUS, outline='black', fill="black")
    
    def shootBullet(self,x,y):
        d = pow(pow(x-WIDTH/2,2)+pow(y-HEIGHT/2,2),1/2)
        self.drawBullet(x,y)
        if d < D/2:
            self.score += N
        else:
            self.score += max((N-1 - (d - D/2)//D),0)
        self.scoreLabel.config(text= f"Score : {self.score}")
    
    def fire(self,n):
        for i in range(n):
            x = random()*(WIDTH-BULLET_RADIUS*2)+BULLET_RADIUS
            y = random()*(HEIGHT-BULLET_RADIUS*2)+BULLET_RADIUS
            self.shootBullet(x,y)

if __name__ == "__main__":
    targetGUI()

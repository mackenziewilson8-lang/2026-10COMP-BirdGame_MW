# start modules
import pgzrun
import sys
# create constants
width = 800
height = 600

# print welcome
print("The game is about to start!")
print("click teh mouse to 'flap' upwards")
print("dodge the pipes and the floor")
print("good luck and have fun!")

# make background
background = Actor("bg")
background.x = 400
background.y = 300

# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300

# make pipes
pipes = []

topPipe1 = Actor("top")
topPipe1.x = 266
topPipe1.y = -10
pipes.append(topPipe1)

bottompipe1 = Actor("bottom")
bottompipe1.x = 266
bottompipe1.y = 800
pipes.append(bottompipe1)

topPipe2 = Actor("top")
topPipe2.x = 532
topPipe2.y = -200
pipes.append(topPipe2)

bottompipe2 = Actor("bottom")
bottompipe2.x = 532
bottompipe2.y = 560
pipes.append(bottompipe2)

topPipe3 = Actor("top")
topPipe3.x = 798
topPipe3.y = -120
pipes.append(topPipe3)

bottompipe3 = Actor("bottom")
bottompipe3.x = 798
bottompipe3.y = 710
pipes.append(bottompipe3)

# draw everything to screen
def draw():
# draw background
    background.draw()

# draw characters
    bird.draw()

# draw pipetop
    topPipe1.draw()
    topPipe2.draw()
    topPipe3.draw()

    bottompipe1.draw()
    bottompipe2.draw()
    bottompipe3.draw()
# update everything
def update():
    # update bird
    bird.y = bird.y + 1
    # update pipes
    topPipe1.x = topPipe1.x - 1
    topPipe2.x = topPipe2.x - 1
    topPipe3.x = topPipe3.x - 1
    bottompipe1.x = bottompipe1.x -1
    bottompipe2.x = bottompipe2.x -1
    bottompipe3.x = bottompipe3.x -1
    # bird hits bottom of screen
    if bird.y > 600:
        print("Game over!")
        sys.exit()
    # bird hits pipes

# moving
def on_mouse_down():
    bird.y -= 50

# runs everything
pgzrun.go()
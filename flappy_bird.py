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
topPipe1 = Actor("top")
topPipe1.x = 266
topPipe1.y = -10
# draw everything to screen
def draw():
# draw background
    background.draw()

# draw characters
    bird.draw()

# draw pipetop
    topPipe1.draw()
# update everything
def update():
    # update bird
    bird.y = bird.y + 1
    # update pipes
    topPipe1.x = topPipe1.x - 1
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
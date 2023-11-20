import turtle
import random

def draw_circle(color, size, x, y):
    # draw a circle of radius equals to size at x, y coordinates and paint it with color
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def move_circle(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
    # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
    xpos[i] += vx[i]
    ypos[i] += vy[i]

    # if the ball hits the side walls, reverse the vx velocity
    if abs(xpos[i] + vx[i]) > (canvas_width - ball_radius):
        vx[i] = -vx[i]

    # if the ball hits the ceiling or the floor, reverse the vy velocity
    if abs(ypos[i] + vy[i]) > (canvas_height - ball_radius):
        vy[i] = -vy[i]

def initilizing(xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls):
    # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
    for i in range(num_balls):
        xpos.append(random.randint(int(-1*canvas_width + ball_radius), int(canvas_width - ball_radius)))
        ypos.append(random.randint(int(-1*canvas_height + ball_radius), int(canvas_height - ball_radius)))
        vx.append(random.randint(1, int(0.01*canvas_width)))
        vy.append(random.randint(1, int(0.01*canvas_height)))
        ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


class Ball:
    def __init__(self):
        canvas_width = turtle.screensize()[0]
        canvas_height = turtle.screensize()[1]
        ball_radius = 0.05 * canvas_width
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.xpos = random.randint(int(-1*canvas_width + ball_radius), int(canvas_width - ball_radius))
        self.ypos = random.randint(int(-1*canvas_height + ball_radius), int(canvas_height - ball_radius))
        self.vx = 0
        self.vy = 0
        self.ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.ball_radius = ball_radius
        
    def draw_ball(self):
        turtle.penup()
        turtle.color(self.ball_color)
        turtle.fillcolor(self.ball_color)
        turtle.goto(self.xpos, self.ypos)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.ball_radius)
        turtle.end_fill()
        
    def move_ball(self):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos += self.vx
        self.ypos  += self.vy

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos + self.vx) > (self.canvas_width - self.ball_radius):
            self.vx = -self.vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos + self.vy) > (self.canvas_height - self.ball_radius):
            self.vy = -self.vy
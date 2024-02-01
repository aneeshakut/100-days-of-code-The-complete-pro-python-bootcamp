import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Crossing Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, -250)

# Create the obstacles
obstacles = []

def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("red")
    obstacle.shapesize(stretch_wid=1, stretch_len=3)
    obstacle.penup()
    y = random.randint(100, 250)
    obstacle.goto(random.randint(-280, 280), y)
    obstacles.append(obstacle)

for _ in range(5):
    create_obstacle()

# Set the player's movement speed
player_speed = 20

# Move the player left
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

# Move the player right
def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Main game loop
while True:
    for obstacle in obstacles:
        y = obstacle.ycor()
        y -= 10
        obstacle.sety(y)

        # Check for collision with player
        if (player.xcor() - 20 < obstacle.xcor() < player.xcor() + 20) and (player.ycor() - 20 < obstacle.ycor() < player.ycor() + 20):
            player.goto(0, -250)

        # Check if obstacle is out of screen
        if y < -300:
            obstacle.goto(random.randint(-280, 280), 250)

    screen.update()

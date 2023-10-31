
import turtle               # Import the turtle module for graphics
import os                   # Import the os module for playing sounds

win = turtle.Screen()               # Create a window for the game
win.title("Ping Pong")              # Setting the title of the window
win.bgcolor("black")                # Setting the background color of the window
win.setup(width=800, height=600)    # Setting the dimensions of the window
win.tracer(0)                       # Turnoff animation updates

# Draw screen divider
divider = turtle.Turtle()           # Create a turtle object to draw the screen divider
divider.color("white")              # Set the color of the divider
divider.penup()                     # Lift the pen up to move without drawing
divider.goto(0, -300)               # Move the turtle to the starting position of the divider
divider.pendown()                   # Put the pen down to start drawing
divider.setheading(90)              # Set the turtle's heading to face upwards
divider.pensize(2)                  # Set the width of the pen

# Draw dotted line
for _ in range(15):                 # Repeat the following steps 15 times
    divider.forward(20)             # Move the turtle forward by 20 units
    divider.penup()                 # Lift the pen up
    divider.forward(20)             # Move the turtle forward by 20 units
    divider.pendown()               # Put the pen down

# Score
score_a = 0                         # Initialize player A's score to 0
score_b = 0                         # Initialize player B's score to 0

# for left Paddle
paddle_left = turtle.Turtle()                           # Create a turtle object for the left paddle
paddle_left.speed(0)                                    # Set the speed of the left paddle's animation
paddle_left.shape("square")                             # Set the shape of the left paddle to a square
paddle_left.color("white")                              # Set the color of the left paddle to white
paddle_left.shapesize(stretch_wid=5, stretch_len=1)     # Set the size of the left paddle
paddle_left.penup()                                     # Lift the pen up
paddle_left.goto(-350, 0)                               # Move the left paddle to its initial position

# for right Paddle
paddle_right = turtle.Turtle()                          # Create a turtle object for the right paddle
paddle_right.speed(0)                                   # Set the speed of the right paddle's animation
paddle_right.shape("square")                            # Set the shape of the right paddle to a square
paddle_right.color("white")                             # Set the color of the right paddle to white
paddle_right.shapesize(stretch_wid=5, stretch_len=1)    # Set the size of the right paddle
paddle_right.penup()                                    # Lift the pen up
paddle_right.goto(350, 0)                               # Move the right paddle to its initial position

# For ball
ball = turtle.Turtle()                                  # Create a turtle object for the ball
ball.speed(10)                                           # Set the speed of the ball's animation
ball.shape("circle")                                    # Set the shape of the ball to a circle
ball.color("white")                                     # Set the color of the ball to white
ball.penup()                                            # Lift the pen up
ball.goto(0, 0)                                         # Move the ball to its initial position
ball.dx = 4                                             # Set the change in x-coordinate for each animation frame
ball.dy = -4                                            # Set the change in y-coordinate for each animation frame

# pen
pen = turtle.Turtle()                                   # Create a turtle object for the pen
pen.speed(0)                                            # Set the speed of the pen's animation
pen.color("white")                                      # Set the color of the pen to white
pen.penup()                                             # Lift the pen up
pen.hideturtle()                                        # Hide the turtle icon
pen.goto(0, 260)                                        # Move the pen to the desired position
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))        # Write the initial score


# Function
def paddle_left_up():                                   # Define a function for moving the left paddle up
    y = paddle_left.ycor()                              # Get the current y-coordinate of the left paddle
    if y < 250:                                         # Check if paddle is not at the top border
        y += 40                                         # Increase the y-coordinate by 20 units
    paddle_left.sety(y)                                 # Set the new y-coordinate for the left paddle


def paddle_left_down():                                 # Define a function for moving the left paddle down
    y = paddle_left.ycor()                              # Get the current y-coordinate of the left paddle
    if y > -240:                                        # Check if paddle is not at the bottom border
        y -= 40                                         # Decrease the y-coordinate by 20 units
    paddle_left.sety(y)                                 # Set the new y-coordinate for the left paddle


def paddle_right_up():                                  # Define a function for moving the right paddle up
    y = paddle_right.ycor()                             # Get the current y-coordinate of the right paddle
    if y < 250:                                         # Check if paddle is not at the top border
        y += 40                                         # Increase the y-coordinate by 20 units
    paddle_right.sety(y)                                # Set the new y-coordinate for the right paddle


def paddle_right_down():                                # Define a function for moving the right paddle down
    y = paddle_right.ycor()                             # Get the current y-coordinate of the right paddle
    if y > -240:                                        # Check if paddle is not at the bottom border
        y -= 40                                         # Decrease the y-coordinate by 20 units
    paddle_right.sety(y)                                # Set the new y-coordinate for the right paddle


# Keyboard binding
win.listen()                                            # Start listening for keyboard events
win.onkeypress(paddle_left_up, "s")                     # Call the paddle_left_up function when the 's' key is pressed
win.onkeypress(paddle_left_down, "w")                   # Call the paddle_left_down function when the 'w' key is pressed
win.onkeypress(paddle_right_up, "Up")                   # Call the paddle_right_up function when the 'Up' arrow key is pressed
win.onkeypress(paddle_right_down, "Down")               # Call the paddle_right_down function when the 'Down' arrow key is pressed


# Main game loop
while True:                                             # Enter an infinite loop
    win.update()                                        # Update the game window

    # move the ball
    ball.setx(ball.xcor() + ball.dx)                # Move the ball horizontally based on its x-coordinate and dx value
    ball.sety(ball.ycor() + ball.dy)                # Move the ball vertically based on its y-coordinate and dy value

    # Border checking
    if ball.ycor() > 290:                               # If the ball hits the upper border
        ball.sety(290)                                  # Reset the y-coordinate of the ball to the upper border
        ball.dy *= -1                                   # Reverse the direction of the ball vertically

    if ball.ycor() < -290:                              # If the ball hits the lower border
        ball.sety(-290)                                 # Reset the y-coordinate of the ball to the lower border
        ball.dy *= -1                                   # Reverse the direction of the ball vertically

    if ball.xcor() > 390:                               # If the ball goes beyond the right border
        ball.goto(0, 0)                                 # Reset the position of the ball to the center
        ball.dx *= -1                                   # Reverse the direction of the ball horizontally
        score_a += 1                                    # Increment the score of player A
        pen.clear()                                     # Clear the previous score display
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))  # Update the score display

    if ball.xcor() < -390:                              # If the ball goes beyond the left border
        ball.goto(0, 0)                                 # Reset the position of the ball to the center
        ball.dx *= -1                                   # Reverse the direction of the ball horizontally
        score_b += 1                                    # Increment the score of player B
        pen.clear()                                     # Clear the previous score display
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))  # Update the score display

    # paddle and ball collision
    if (340 < ball.xcor() < 350) and (paddle_right.ycor() + 50 > ball.ycor() > paddle_right.ycor() - 50):  # If the ball hits the right paddle
        ball.setx(340)                                  # Reset the x-coordinate of the ball to the right paddle
        ball.dx *= -1                                   # Reverse the direction of the ball horizontally
        os.system("afplay bounce.wav&")                 # Play a bounce sound using the afplay command (Mac)

    if (-340 > ball.xcor() > -350) and (paddle_left.ycor() + 50 > ball.ycor() > paddle_left.ycor() - 50):  # If the ball hits the left paddle
        ball.setx(-340)                                 # Reset the x-coordinate of the ball to the left paddle
        ball.dx *= -1                                   # Reverse the direction of the ball horizontally
        os.system("afplay bounce.wav&")                 # Play a bounce sound using the afplay command (Mac)


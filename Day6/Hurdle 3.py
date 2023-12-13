'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    while not at_goal():
        if wall_in_front():
            turn_left()
            move()
            turn_right()
            move()
            turn_right()
            move()
            turn_left()
        else:
            move()

       
    #for step in range(1,7):
jump()


'''

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

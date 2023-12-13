'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def moveToGoal():
    
    for step in range(1,7):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

    
moveToGoal()
'''

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

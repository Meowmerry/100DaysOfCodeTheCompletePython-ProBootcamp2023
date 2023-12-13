'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def is_at_goal():  
    while not at_goal():
       if right_is_clear():
          turn_right()
          move()
       elif front_is_clear():
            move()
       else:
            turn_left()
def jump():
    while front_is_clear():
          move()
    turn_left()
    is_at_goal()

jump()
'''


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

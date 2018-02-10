'''
the program module
'''
from robot import Robot
from environment import _2DEnvironment

def main():
    '''starts program'''
    print("Beep boop, I'm a robot")
    command = ""
    env = _2DEnvironment(5, 5)
    robot = Robot(env)
    
    while(True):
        command = input("input command: ")
        if(command.strip() == 'q'):
            break
        robot.exe(command)

main()

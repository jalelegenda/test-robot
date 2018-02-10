from consts import ORIENTATIONS

class Robot:
    '''a simple robot able to move on a 2D plane'''
    
    def __init__(self, env):
        '''initializes available commands and environment'''
        self.__commands = {
            'LEFT': self.__rotate_left__,
            'MOVE': self.__move__,
            'PLACE': self.__place__,
            'RIGHT': self.__rotate_right__,
            'REPORT': self.__report__
        }

        self.__posx = self.__posy = self.__o = None
        self.__env = env


    def exe(self, command):
        '''calls parser, then commands with return values''' 
        key, parameters = self.__parse__(command)

        if((None in (self.__posx, self.__posy)) and (key != 'PLACE')):
            print('please run place command first')
        else:
            try:
                self.__commands[key](parameters)
            except(KeyError):
                print('does not compute')
            
        
    def __parse__(self, command):
        '''parses human input f{command} {parameters}'''
        a = command.split(' ', 1)
        try:
            p = [x.strip() for x in a[1].split(',')]
        except(IndexError):
            p = None
        return a[0], p
        

    #COMMANDS
    #To allow redundant parameters don't throw KeyError

        
    def __move__(self, args=None):
        '''moves one block towards facing direction'''
        if(args != None):
            raise KeyError
        if((self.__posx < self.__env.getx()) and (self.__o == 'EAST')):
            self.__posx += 1
        elif((self.__posx > 0) and (self.__o == 'WEST')):
            self.__posx -= 1
        elif((self.__posy < self.__env.gety()) and (self.__o == 'NORTH')):
            self.__posy += 1
        elif((self.__posy > 0) and (self.__o == 'SOUTH')):
            self.__posy -= 1
        else:
            print("I--- I can't!!!")

        
    def __rotate_left__(self, args=None):
        '''rotates 90 degree left'''
        if(args != None):
            raise KeyError
        i = ORIENTATIONS.index(self.__o)
        length = len(ORIENTATIONS)

        self.__o = ORIENTATIONS[(i-1) % length]

    def __rotate_right__(self, args=None):
        '''rotates 90 degree right'''
        if(args != None):
            raise KeyError
        i = ORIENTATIONS.index(self.__o)
        length = len(ORIENTATIONS)

        self.__o = ORIENTATIONS[(i+1) % length]

    def __place__(self, args=None):
        '''jumps to coordinates'''
        try:
            x, y = int(args[0]), int(args[1])

            if((0 < x < self.__env.getx()) and (0 < y < self.__env.gety()) and (args[2] in ORIENTATIONS)):            
                self.__posx, self.__posy = x, y
                self.__o = args[2]
                self.__report__()
            else:
                raise ValueError
        except (ValueError, TypeError, IndexError):
            print('incorrect parameters')

    def __report__(self, args=None):
        '''reports current whereabouts'''
        if(args != None):
            raise KeyError
        print(f'coordinates: [x:{self.__posx}], [y:{self.__posy}], facing: {self.__o}')
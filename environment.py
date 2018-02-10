'''
environments module
'''

class _2DEnvironment:
    '''2d board'''
    def __init__(self, x, y):
        self.__x, self.__y = x, y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

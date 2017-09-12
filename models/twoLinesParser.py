
class TwoLinesParser:
    def __init__(self, lines):
        self.__buffer = []
        self.__lines = lines
        self.__readIndex = -1

    @property
    def lineOne(self):
        return "" if len(self.__buffer) == 0 else self.__buffer[0]

    @property
    def lineTwo(self):
        return "" if len(self.__buffer) == 1 else self.__buffer[1]

    @property
    def canRead(self):
        return self.__readIndex < len(self.__lines) - 1

    def read(self):
        if not self.canRead:
            return

        def beginRead():
            self.__readIndex += 1
            print('begin read')
            print(self.__lines[self.__readIndex])
            return self.__lines[self.__readIndex]
        
        def readline():
            if self.canRead:
                self.__buffer.append(beginRead())

            if len(self.__buffer) < 2:
                readline()
            elif len(self.__buffer) == 2:
                return
            else:
                print('remove first one')
                self.__buffer = self.__buffer[1:3]

        readline()
        
        

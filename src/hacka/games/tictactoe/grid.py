class Grid() :
    def __init__(self, mode= "Classic"):
        self.initializeMode(mode)

    def initialize(self, letters, numbers):
        self._= {
            line: [0]+ [0 for i in numbers ]
            for line in letters
        }

    def initializeMode(self, mode):
        if mode == 'Ultimate' :
            return self.initialize(
                ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
                range(1, 10)
            )
        return self.initialize(
            ["A", "B", "C"],
            range(1, 4)
        )

    def update( self, pods ):
        for elt in pods :
            self._[elt.status()]= [0] + elt.flags()
        return self
    
    def at(self, abs, ord):
        return self._[abs][ord]

    def at_set(self, abs, ord, value):
        self._[abs][ord]= value
        return self._[abs][ord]

    def __str__(self, playerId= 0):
        abss= self._.keys()
        ords= range(1, len(abss)+1)
        sign= [ ' ', 'x', 'o' ]
        # print player sign:
        s= f"{ sign[playerId] }:"

        # print letters references:
        for abs in abss :
            if abs in ['D', 'G']:
                s+= '  '
            s+= ' '+ abs
        s+= "\n"

        # print each lines:
        for ord in ords :
            if ord in [4, 7] :
                s+= "  -------|-------|-------\n"
            s+= str(ord) +' '
            for abs in abss :
                if abs in ['D', 'G']:
                    s+= ' |'
                s+= ' '+ sign[ self.at(abs, ord) ]
            s+= "\n"
        return s
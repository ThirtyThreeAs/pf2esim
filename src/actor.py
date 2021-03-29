class SimpleActor:
    def __init__(self,name,maxhp,ac,strat):
        """
        A simple class to encapsulate actors
        Actors are the PCs or NPCs in combat
        :param name: string, the name
        :param maxhp: int, the maximum HP
        :param ac: int, the Armor Class
        :param strat: function, describes the actions the actor will take in combat

        """
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.ac = ac
        self.strat = strat
        self.block = False

    def reset(self):
        self.roundreset()
        self.hp = self.maxhp

    def roundreset(self):
        self.block = False
    
    def raiseshield(self):
        self.block = True
    
    def getac(self):
        if(self.block):
            return self.ac+2
        else:
            return self.ac



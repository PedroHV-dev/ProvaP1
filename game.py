class Game:

    LOVE = "Love"
    FIFTEEN = "Fifteen"
    THIRTY = "Thirty"
    FORTY = "Forty"
    RESULT = ""
    DEUCE = "Deuce"

    playerAdvantaged = self.p1points > self.p2points and self.p2points >= 3

    playerWin = self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()
    
    def score(self):

        pontosPlayer1 = ""
        pontosPlayer2 = ""
        if (self.empate() and self.pontosPlayer1 < 3):
            if (self.pontosPlayer1==0):
                RESULT = LOVE
            elif (self.pontosPlayer1==1):
                RESULT = FIFTEEN
            elif (self.pontosPlayer1==2):
                RESULT = THIRTY + "ALL"
        else:
            return DEUCE
        
        P1res = ""
        P2res = ""
        if (self.p1points > 0 and self.p2points==0):
            if (self.p1points==1):
                P1res = FIFTEEN
            if (self.p1points==2):
                P1res = THIRTY
            if (self.p1points==3):
                P1res = FORTY
            
            P2res = LOVE
            RESULT = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points==0):
            if (self.p2points==1):
                P2res = FIFTEEN
            if (self.p2points==2):
                P2res = THIRTY
            if (self.p2points==3):
                P2res = FORTY
            
            P1res = LOVE
            RESULT = P1res + "-" + P2res
        
        
        if (self.p1points>self.p2points and self.p1points < 4):
            if (self.p1points==2):
                P1res=THIRTY
            if (self.p1points==3):
                P1res=FORTY
            if (self.p2points==1):
                P2res=FIFTEEN
            if (self.p2points==2):
                P2res=THIRTY
            RESULT = P1res + "-" + P2res
        if (self.p2points>self.p1points and self.p2points < 4):
            if (self.p2points==2):
                P2res=THIRTY
            if (self.p2points==3):
                P2res=FORTY
            if (self.p1points==1):
                P1res=FIFTEEN
            if (self.p1points==2):
                P1res=THIRTY
            RESULT = P1res + "-" + P2res
        
        if (playerAdvantaged):
            RESULT = "Advantage " + self.player1Name
        else:
            RESULT = "Advantage " + self.player2Name
        return RESULT
        
        if (playerWin):
            RESULT = "Win for " + self.player1Name
        else:
            RESULT = "Win for " + self.player2Name
        return RESULT
    
    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()
    
    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()
    
    def P1Score(self):
        self.p1points +=1
    
    
    def P2Score(self):
        self.p2points +=1

    def empate(self):
        return self.pontosPlayer1 == self.pontosPlayer2


class Game:

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

        PONTOS = [{
            0: LOVE,
            1: FIFTEEN,
            2: THIRTY,
            3: FORTY
        }]

        LOVE = "Love"
        FIFTEEN = "Fifteen"
        THIRTY = "Thirty"
        FORTY = "Forty"
        RESULT = ""
        DEUCE = "Deuce"

        
        if (self.empate() and self.p1points < 3):
            if (self.p1points==0):
                RESULT = LOVE
            elif (self.p1points==1):
                RESULT = FIFTEEN
            elif (self.p1points==2):
                RESULT = THIRTY + "ALL"
        else:
            return DEUCE
        
        P1res = ""
        P2res = ""
        
        if(self.verificarVencedorRound()):
            RESULT = P1res + "-" + P2res

        playerAdvantaged1 = self.p1points > self.p2points and self.p2points >= 3
        playerAdvantaged2 = self.p2points > self.p1points and self.p1points >= 3
        
        if (playerAdvantaged1 and self.p1points < 4):
            if (self.p1points==2):
                P1res=THIRTY
            elif (self.p1points==3):
                P1res=FORTY
            elif (self.p2points==1):
                P2res=FIFTEEN
            elif (self.p2points==2):
                P2res=THIRTY
            RESULT = P1res + "-" + P2res
        if (playerAdvantaged2 and self.p2points < 4):
            if (self.p2points==2):
                P2res=THIRTY
            elif (self.p2points==3):
                P2res=FORTY
            elif (self.p1points==1):
                P1res=FIFTEEN
            elif (self.p1points==2):
                P1res=THIRTY
            RESULT = P1res + "-" + P2res
        
        if (playerAdvantaged1):
            RESULT = "Advantage " + self.player1Name
        else:
            RESULT = "Advantage " + self.player2Name
        
        if (self.pontosPlayer1 >= 4):
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

    def verificarVencedorRound(self):
        pointRound = self.p1points > 0 and self.p2points==0 or self.p2points > 0 and self.p1points==0
        if (pointRound):
            if(self.p1points == self.PONTOS[self.p1points]):
                self.P1res = self.PONTOS[self.p1points]
                return self.P1res
            else:
                self.P2res = self.PONTOS[self.P2res]
                return self.P2res
class Game:

    def play(self):
        pass

    def saveScore(self):
        pass

    def hardLevel(self):
        pass

class PlayGame(Game):

    def play(self):
        return 'Game start'

    def hardLevel(self):
        return 'Level increase'

class GameScore(Game):

    def saveScore(self):
        return "Score Saved"

p1 = PlayGame()
print(p1.play(),'\n',p1.hardLevel())
s1 = GameScore()
print(s1.saveScore())
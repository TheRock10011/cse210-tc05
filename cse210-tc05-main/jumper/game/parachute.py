import random
from game.word import Word
class Jumper:
    def __init__(self):
        self.parachute = ["  ___  "," /","___","\ "," \   ","/  ","  \ ","/","   0","  /|\ ","  / \ "]
        self.count = 0

    """ how to arrage the display the parachute """
    """ print ([0])
        print ([1 + 2 + 3])
        print ([4 + 5])
        print ([6 + 7])
        print ([8])
        print ([9])
        print ([10])"""

    def parachuteDispaly(self,p):
        print (p[0])
        print (p[1] + p[2] + p[3])
        print (p[4] + p[5])
        print (p[6] + p[7])
        print (p[8])
        print (p[9])
        print (p[10])

    def keep_playing(self):
        parachute = self.parachute
        Jumper.parachuteDisplay(parachute)
        i = 0
        if i < 9 & Word.DidYouGetAtLeastOneLetterRight() == False:
            if i == 0:
                parachute[i] = ""
            elif i == 1:
                parachute[i] = " "
            elif i == 2:
                parachute[i] = "   "
            elif i == 3:
                parachute[i] = "  "
            elif i == 4:
                parachute[i] = "    "
            elif i == 5:
                parachute[i] = "   "
            elif i == 6:
                parachute[i] = "   "
            elif i == 7:
                parachute[i] = " "
            elif i == 8:
                parachute[8] = "X"
            return parachute
            i += 1
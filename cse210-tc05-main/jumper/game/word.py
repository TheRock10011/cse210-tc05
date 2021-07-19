import random

class Word:
    """Word class takes care of the word that is used in the game. It picks out the word and 
    says if someone got a letter to the word is correct
    """


    
    def __init__(self):
        #This code will run automaticlly 
        self.wordList = ["aaron", "ab", "abandoned", "abc", "aberdeen", "abilities",
        "ability", "able", "aboriginal", "about", "above", "abraham",
        "abroad", "abs", "absence", "absent", "absolute",
        "absolutely",
        "absorption",
        "abstract",
        "abstracts",
        "abu",
        "abuse",
        "ac",
        "academic",
        "academics",
        "academy",
        "acc",
        "accent",
        "accept",
        "acceptable",
        "acceptance"]
        self.wordChosen = random.randint(0, len(self.wordList))
        self.theWordToGuess = ""

        #Set the full word to be "_"
        self.fullWordGuessedSoFar = self.wordList[self.wordChosen]
        self.fullWordGuessedSoFar = Word.split(self.fullWordGuessedSoFar)
        for i in range(0, len(self.fullWordGuessedSoFar)):
            self.fullWordGuessedSoFar[i] = "_"
        
        
     
     
  
    def LetterRightOrWrong(self, letterInputed):
        #How to use from director: wordGuessedSoFar = word.LetterRightOrWrong("a")

        #This function sets adds the new letters to the word that are corerect. 
        self.theWordToGuess = self.wordList[self.wordChosen]
        theWordToArray = Word.split(self.theWordToGuess)
        for i in range(0, len(theWordToArray)):

            if letterInputed.lower() == theWordToArray[i]:
                self.fullWordGuessedSoFar[i] = letterInputed
        return self.fullWordGuessedSoFar
                
    
    def DidYouGetAtLeastOneLetterRight(self, letterInputed):
        #Example how to use from director: wasOneLetterCorrect = DidYouGetAtLeastOneLetterRight("a")

        #This function returns true if there is at least one letter used that is
        #is the word that was guessed
        self.theWordToGuess = self.wordList[self.wordChosen]
        theWordToArray = Word.split(self.theWordToGuess)
        for i in range(0, len(theWordToArray)):
            
            if letterInputed.lower() == theWordToArray[i]:
                
                return True
        return False
    
    
    def split(wordToSplit):
        return [char for char in wordToSplit]



    
    def DefinesWhatTheWordIs(self):
        #How to use from director: theWord = DefinesWhatTheWordIs()

        #This will set theWord to be the word that is to be guessed in the game
        self.theWordToGuess = self.wordList[self.wordChosen]
        return self.theWordToGuess





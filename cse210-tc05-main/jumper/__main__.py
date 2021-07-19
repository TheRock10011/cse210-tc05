#from game.director import Director
from game.word import Word
word = Word()
correntWord = word.LetterRightOrWrong("a")
thing = word.DidYouGetAtLeastOneLetterRight("a")

print(correntWord)
print(thing)
#director = Director()
#director.start_game()
# Object Orientated Programing Character Class by Elijah

# Character Class
class Character():
    def __init__(self, name, phrase1, phrase2):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0
    
    # Character speaks. If phraseNum == 1 then speak the first phrase. If its 2 then speak the second
    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.phrase1)
        elif phraseNum == 2:
            print(self.phrase2)

    # set the level to newLevel and print it out
    def setLevel(self, newLevel):
        self.level = newLevel
        print(self.level)

# characters
kungFuPanda = Character("Po", "Skadoosh", "You have been blinded by pure awesomeness!")
santaClaus = Character("Santa Claus", "Hohoho!", "Merry Christmas!")

# character method call
santaClaus.speak(1)
santaClaus.setLevel(2)
kungFuPanda.speak(2)



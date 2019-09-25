import nltk
from nltk.tokenize import TweetTokenizer
from nltk.tag import pos_tag, map_tag
from nltk.corpus import wordnet as words
from madlibs import *
import random


def prepNLTK(string):
    tweet = TweetTokenizer()
    return nltk.pos_tag(tweet.tokenize(string))

Passages = madlibs()

print("Welcome to Mad Libs. \n")
print("It's a mad mad world, please take a look at our selection of passages: ") 
print("NeverGonna : Never Gonna Give You Up by Rick Astley\n"
      "Allstar : Allstar by Smashmouth\n"
      "HungerGames : Rules of the Hunger Games\n"
      "PulpFiction : Crispy quote from the movie Pulp Fiction\n"
      "Joker : Quote by Joker from Batman\n")

x = input("So which passage would you like to play with with: \n")
x = x.lower()
      

validInput = False

while validInput == False:
    if x in Passages.passages.get():
        #print(Passages[x])
        validInput = True
    else:
        x = input("Invalid passage selected. Please input a valid passage title: \n")
        x = x.lower()


SelectedPassage = madlibPassage(Passages.passages.getVal(x))

Tags = SelectedPassage.getTags()

print("The selected passage has...")
print(str(len(Tags[0])) + ' verb(s).')
print(str(len(Tags[1])) + ' noun(s).')
print(str(len(Tags[2])) + ' pronoun(s).')
print(str(len(Tags[3])) + ' adjective(s).')
print(str(len(Tags[4])) + ' adverb(s).')

Options = ['verbs','nouns','pronouns','adjectives','adverbs']
UserSelection = [0,0,0,0,0]

i = 0
while i < len(Options):
    x = int(input("How many random " + Options[i] + " would you like to change:\n"))
    if x <= len(Tags[i]) and x >= 0:
        UserSelection[i] = x
        i = i+1

RandomArray = []

i = 0    
while i < len(UserSelection):
    j = 0
    RandomArray = []
    print("Please enter " + str(UserSelection[i]) + " " + Options[i] + ":")
    while j < UserSelection[i]:
        x = random.randint(0,len(Tags[i])-1)
        if x not in RandomArray:
            RandomArray.append(x)
            Tags[i][x][0] = input()
            o = Tags[i][x][0]
            k = Tags[i][x][1]
            SelectedPassage.passage[k] = list(SelectedPassage.passage[k])
            SelectedPassage.passage[k][0] = str(o)
            j += 1
    i += 1
final = ''
for words in SelectedPassage.passage:
    final = final + words[0] + " "
print(final)

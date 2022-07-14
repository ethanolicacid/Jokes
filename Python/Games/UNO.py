from calendar import c
from cmath import e
from ctypes import cdll
from operator import contains
import random
from this import d
import time

deckOfCards = ["red0", "red1", "red2", "red3", "red4", "red5", "red6", "red7", "red8", "red9", "redReverse", "redAdd2", "redSkip",
"yellow0", "yellow1", "yellow2", "yellow3", "yellow4", "yellow5", "yellow6", "yellow7", "yellow8", "yellow9", "yellowReverse", "yellowAdd2", "yellowSkip",
"blue0", "blue1", "blue2", "blue3", "blue4", "blue5", "blue6", "blue7", "blue8", "blue9", "blueReverse", "blueAdd2", "blueSkip",
"green0", "green1", "green2", "green3", "green4", "green5", "green6", "green7", "green8", "green9", "greenReverse", "greenAdd2", "greenSkip",
"colourChange", "Add4"]

deckOfCardsNoFunctionCards = ["red0", "red1", "red2", "red3", "red4", "red5", "red6", "red7", "red8", "red9",
"yellow0", "yellow1", "yellow2", "yellow3", "yellow4", "yellow5", "yellow6", "yellow7", "yellow8", "yellow9", 
"blue0", "blue1", "blue2", "blue3", "blue4", "blue5", "blue6", "blue7", "blue8", "blue9", 
"green0", "green1", "green2", "green3", "green4", "green5", "green6", "green7", "green8", "green9"]

functionCards = ["redReverse", "redAdd2", "redSkip", "yellowReverse", "yellowAdd2", "yellowSkip", 
"blueReverse", "blueAdd2", "blueSkip", "greenReverse", "greenAdd2", "greenSkip", "colourChange", "Add4"]

playerDeck = []
botDeck = []
depositDeck = []
drawDeck = []
firstCard = ""
def distributeCards():

    a = int(random.randint(0,53))
    playerDeck.append(deckOfCards[a])
    del deckOfCards[a]
    b = int(random.randint(0,52))
    playerDeck.append(deckOfCards[b])
    del deckOfCards[b]
    c = int(random.randint(0,51))
    playerDeck.append(deckOfCards[c])
    del deckOfCards[c]
    d = int(random.randint(0,50))
    playerDeck.append(deckOfCards[d])
    del deckOfCards[d]
    e = int(random.randint(0,49))
    playerDeck.append(deckOfCards[e])
    del deckOfCards[e]
    f = int(random.randint(0,48))
    playerDeck.append(deckOfCards[f])
    del deckOfCards[f]
    g = int(random.randint(0,47))
    playerDeck.append(deckOfCards[g])
    del deckOfCards[g]
    h = int(random.randint(0,46))
    botDeck.append(deckOfCards[h])
    del deckOfCards[h]
    j = int(random.randint(0,45))
    botDeck.append(deckOfCards[j])
    del deckOfCards[j]
    k = int(random.randint(0,44))
    botDeck.append(deckOfCards[k])
    del deckOfCards[k]
    l = int(random.randint(0,43))
    botDeck.append(deckOfCards[l])
    del deckOfCards[l]
    m = int(random.randint(0,42))
    botDeck.append(deckOfCards[m])
    del deckOfCards[m]
    n = int(random.randint(0,41))
    botDeck.append(deckOfCards[n])
    del deckOfCards[n]
    p = int(random.randint(0,40))
    botDeck.append(deckOfCards[p])
    del deckOfCards[p]

def startGame():
    card1 = int(random.randint(0,39))
    firstCard = deckOfCards[card1]
    while firstCard in functionCards():
        card1 = int(random.randint(0,39))
        firstCard = deckOfCards[card1]
    if firstCard in deckOfCardsNoFunctionCards:
        depositDeck.append(firstCard)

    

    


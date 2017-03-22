import dota2api
import json
import pickle
import time
import csv

#for documentation on dota2api
#https://dota2api.readthedocs.io/en/latest/index.html

#game is a dictionary as returned by get_match_history()["matches"]
#returns true if the game is a ranked matchmaking game
def isRankedMatchmaking(game):
    return game["lobby_type"] == 7


#currentGameDetails is a dictionary as returned by get_match_history
#returns a dictionary with direHeroes and radiantHeroes, where the 
#hero id within direHeroes and radiantHeroes list is sorted
def getHeroes(currentGameDetails):
    players = currentGameDetails["players"]
    direHeroes = []
    radiantHeroes = []
    for i in range(0, len(players)):
        currentPlayer = players.pop()
        currentPlayerHeroID = currentPlayer["hero_id"]
        #the player slot is represented in 8 bits, the details of
        #which can be found in the documentation linked at the top
        #of the file. Basically, if the 8th bit is set, i.e. if
        #player slot byte is more than or equal to 128, then the
        #8th bit is set, and so the player was a dire player
        if(currentPlayer["player_slot"] >= 128):
            direHeroes.append(currentPlayerHeroID)
        else:
            radiantHeroes.append(currentPlayerHeroID)
    direHeroes = sorted(direHeroes)
    radiantHeroes = sorted(radiantHeroes)
    return {'direHeroes': direHeroes, 'radiantHeroes': radiantHeroes}

#isDuplicateMatch checks whether a match of identical team/hero 
#composition has 
def isDuplicateMatch(radiantHeroes, direHeroes):
    found = False
    i = 0
    while (i < len(listOfRadiantHeroes)) & (not found):
        found = (radiantHeroes == listOfRadiantHeroes[i]) and \
        (direHeroes == listOfDireHeroes[i])
        i = i+1
    return found


api = dota2api.Initialise("6E87FE70D7AB385951B051E0852127B6")


#these lists will contain the resulting filtered games
#each of these lists then can be thought of as a column
#in a csv file, kinda
listOfRadiantHeroes = []
listOfDireHeroes = []
listOfMatchOutcomes = []

#a dictionary which will contain ID's of matches already
#noted. If a game has already been logged, we don't want to 
#log it again
loggedGames = {}


#just to see how long this junk takes
startTime = time.time()

while (len(listOfRadiantHeroes) < 50000):
    try:
        print "Number of samples thus far:"
        print len(listOfRadiantHeroes)
        currentResponse = api.get_match_history(skill = 3)
        #get the matches out the dictionary response
        currentGames = currentResponse["matches"]
        for currentGame in currentGames:
            currentGameID = currentGame["match_id"]
            if (isRankedMatchmaking(currentGame)):
                if currentGameID not in loggedGames:
                    print currentGameID
                    #add game to logged games
                    loggedGames[currentGameID] = currentGameID
                    #the information the currentGame dictionary contains
                    #is not enough, namely it is missing the hero details
                    #of the match. So we fire off another query to get
                    #those details
                    currentGameDetails = api.get_match_details(currentGameID)
                    heroes = getHeroes(currentGameDetails)
                    radiantWin = currentGameDetails["radiant_win"]
                    if not isDuplicateMatch(heroes["radiantHeroes"], 
                                            heroes["direHeroes"]):
                        listOfRadiantHeroes.append(heroes["direHeroes"])
                        listOfDireHeroes.append(heroes["radiantHeroes"])
                        listOfMatchOutcomes.append(radiantWin)
        time.sleep(10)
    except:
        print "EXCEPTION HAPPENED YO. So I'm just going to sleep for a while and retry."
        time.sleep(30)
        resultDictionary = {"radiantHeroes": listOfRadiantHeroes,
                            "direHeroes": listOfDireHeroes,
                            "matchOutcomes": listOfMatchOutcomes}
        pickle.dump(resultDictionary, open("resultDictionary.dict", "wb"))

resultDictionary = {"radiantHeroes": listOfRadiantHeroes,
                    "direHeroes": listOfDireHeroes,
                    "matchOutcomes": listOfMatchOutcomes}
pickle.dump(resultDictionary, open("resultDictionary.dict", "wb"))

import numpy as np

def sameHeroCount(teamA, teamB):
    samesiesCount = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if teamA[i] == teamB[j]:
                samesiesCount = samesiesCount + 1
    for i in range(5, 10):
        for j in range(5, 10):
            if teamA[i] == teamB[j]:
                samesiesCount = samesiesCount + 1
    return samesiesCount

def flipTeam(team):
    temp = np.zeros(5)
    for i in range(0, 5):
        temp[i] = team[i]
        team[i] = team[i+5]
        team[i+5] = temp[i]
    return team

def flipTeams(teams):
    for i in range(0, len(teams)):
        teams[i] = flipTeam(teams[i])
    return teams

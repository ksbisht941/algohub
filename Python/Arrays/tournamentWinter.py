# Here is your solution

HOME_TEAM_WON = 1

def tournamentWinter(competitions, results):
    currentBestTeam = ''
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        homeTeam, awayTeam = competition
        result = results[idx]

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScore(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam

def updateScore(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points

# Call the function
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]

results = [0, 0, 1]

output = tournamentWinter(competitions, results)
print('👋 Output:', output)
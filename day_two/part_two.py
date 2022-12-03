from enum import Enum

class Election(Enum):
	ROCK = 1
	PAPER = 2
	SCISSORS = 3

def convertToElection(letter):
	if letter == 'A' or letter == 'X':
		return Election.ROCK
	elif letter == 'B' or letter == 'Y':
		return Election.PAPER
	elif letter == 'C' or letter == 'Z':
		return Election.SCISSORS
	return Election.SCISSORS

def convertToResult(letter):
	if letter == 'X':
		return MatchResult.LOSE
	elif letter == 'Y':
		return MatchResult.DRAW
	return MatchResult.WIN
	
class MatchResult(Enum):
	LOSE = 0
	DRAW = 1
	WIN = 2

def checkIfWin(oponent_election, your_election):
	if oponent_election == your_election:
		return MatchResult.DRAW

	if your_election == Election.ROCK:
		if oponent_election == Election.SCISSORS:
			return MatchResult.WIN
		else:
			return MatchResult.LOSE

	if your_election == Election.PAPER:
		if oponent_election == Election.ROCK:
			return MatchResult.WIN
		else:
			return MatchResult.LOSE

	if your_election == Election.SCISSORS:
		if oponent_election == Election.PAPER:
			return MatchResult.WIN
		else:
			return MatchResult.LOSE

def findElection(oponent_election, desired_result):
	possibilities = [Election.ROCK, Election.SCISSORS, Election.PAPER]
	for p in possibilities:
		if checkIfWin(oponent_election, p) == desired_result:
			return p
	return Election.ROCK

def checkMatch(oponent_election, your_result):
	#print(your_election, oponent_election)
	oponent_election = convertToElection(oponent_election)
	your_result = convertToResult(your_result)
	your_election = findElection(oponent_election, your_result)
	# math trick...
	#print(your_election, oponent_election)
	return your_election.value + 3*(your_result.value)

def readInput(file='testInput'):
	with open(file) as f:
		lines = f.readlines()
		total_score = 0
		for l in lines:
			total_score = total_score + checkMatch(l[0], l[2])
		return total_score

print(readInput(file='input'))



















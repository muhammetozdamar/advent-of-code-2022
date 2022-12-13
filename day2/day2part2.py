# A = ROCK      = 1 # 65 - 3 - 1 - 2
# B = PAPER     = 2 # 66 - 1 - 2 - 3
# C = SCISSORS  = 3 # 67 - 2 - 3 - 1 


# X = LOSE = 0p = 88
# Y = DRAW = 3p = 89
# Z = WIN  = 6p = 90

total_score = 0
with open("day2\input.txt") as file:
    rounds = file.read().split("\n")
    for round in rounds:
        if(len(round.strip()) == 0): continue
        opponent = ord(round[0])
        me = ord(round[2])
        total_score += (me-88)*3
        if(me == 88):   # 65->67 66->65 67->66
            if(opponent == 65):  total_score += 3
            else: total_score +=(opponent-65)
        elif(me == 89): # 65->65 66->66 67->67
            total_score += (opponent-64)
        elif(me == 90): # 65->66 66->67 67->65
            if(opponent == 67):  total_score += 1
            else:  total_score += (opponent-63)

print(total_score)
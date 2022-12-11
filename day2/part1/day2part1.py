# A = X = ROCK      = 1 # 65 - 88
# B = Y = PAPER     = 2 # 66 - 89
# C = Z = SCISSORS  = 3 # 67 - 90
# Y>X X>Z Z>Y 

# WIN  = 6p 
# DRAW = 3p
# LOSE = 0p

total_score = 0
with open("day2\input.txt") as file:
    rounds = file.read().split("\n")
    for round in rounds:
        if(len(round.strip()) == 0): continue
        total_score += (ord(round[2]) - 87)
        opponent = ord(round[0])
        me = ord(round[2])-23
        if(opponent == me):
            total_score+=3
            continue
        if(me-opponent == 1 or opponent-me == 2): 
            total_score += 6
            continue

print(total_score)
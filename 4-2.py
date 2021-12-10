import numpy as np

import sys

testArray = np.loadtxt("4-entries.txt")
players = testArray.reshape(100,5,5)
drawn_numbers = [6,69,28,50,36,84,49,13,48,90,1,33,71,0,94,59,53,58,60,96,30,34,29,91,11,41,77,95,17,80,85,93,7,9,74,89,18,25,26,8,87,38,68,5,12,43,27,46,62,73,16,55,22,4,65,76,54,52,83,10,21,67,15,47,45,40,35,66,79,51,75,39,64,24,37,72,3,44,82,32,78,63,57,2,86,31,19,92,14,97,20,56,88,81,70,61,42,99,23,98]
dd = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
# iteriere durch erste zeile
for drawn in drawn_numbers:
    print(len(players))
    # iteriere durch alle matrizen
    for i in range(len(players)):
        # wenn nummer vorkommt mach -1
        players = np.where(players==drawn , -1, players)
        for j in range(len(players)):
            zeroax = np.sum(players[j], axis=0)
            oneax = np.sum(players[j], axis=1)
            if (len(players) == 1) and (np.any(oneax == -5) or np.any(zeroax == -5)):
                players = np.where(players==-1 , 0, players)
                wholesum = np.sum(players[j])
                print("wholesum kommt")
                print(wholesum * drawn)
                sys.exit()

    
            elif np.any(oneax == -5) or np.any(zeroax == -5):
                #players = np.where(players==-1 , 0, players)
                players = np.delete(players,j,0)
                break
        #print(len(players))
print(players)
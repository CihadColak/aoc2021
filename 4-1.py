import numpy as np

import sys

testArray = np.loadtxt("4-entries.txt")
players = testArray.reshape(100,5,5)
drawn_numbers = [6,69,28,50,36,84,49,13,48,90,1,33,71,0,94,59,53,58,60,96,30,34,29,91,11,41,77,95,17,80,85,93,7,9,74,89,18,25,26,8,87,38,68,5,12,43,27,46,62,73,16,55,22,4,65,76,54,52,83,10,21,67,15,47,45,40,35,66,79,51,75,39,64,24,37,72,3,44,82,32,78,63,57,2,86,31,19,92,14,97,20,56,88,81,70,61,42,99,23,98]
# iteriere durch erste zeile
for drawn in drawn_numbers:
    # iteriere durch alle matrizen
    for i in range(len(players)):
        # wenn nummer vorkommt mach -1
        players = np.where(players==drawn , -1, players)
        zeroax = np.sum(players[i], axis=0)
        oneax = np.sum(players[i], axis=1)
        
        # wenn summe von irgendeiner zeile oder spalte -5
        print(players[i])
        if np.any(oneax == -5) or np.any(zeroax == -5):
            players = np.where(players==-1 , 0, players)
            wholesum = np.sum(players[i])
            print("wholesum kommt")
            print(wholesum * drawn)
            print(drawn)
            sys.exit()
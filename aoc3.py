import os


def flip(number):
    res = ""
    for i in str(number):
        if i == "1":
            res += "0"
        else:
            res += "1"
    return res

flip("1010")

f = open("3.txt", "r")

firstline = f.readline()
lines = f.readlines()
print(lines[0])
res = ""
for i in range(len(firstline)  -1):
    ones = 0
    zeros = 0
    curr_col = lines[i]
    for j in range(len(lines)):
        if lines[j][i] == '1':
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        res = res + "1"
    else:
        res = res + "0"

print("gamma rate in decimal:" + str(int(res,2)))
flipped_eps = flip(res)
print("epsilon rate in dec:" + str(int(flipped_eps,2)))
print("multi:" + str(int(res,2) * int(flipped_eps,2)))
import os


def flip(number):
    res = ""
    for i in str(number):
        if i == "1":
            res += "0"
        else:
            res += "1"
    return res


f = open("3.txt", "r")

#firstline = f.readline()
lines = f.readlines()
res_arr = lines
for i in range(len(lines[0])  -1):
    ones = []
    zeros = []
    for j in range(len(res_arr)):
        if res_arr[j][i] == '1':
            ones.append(res_arr[j])
        else:
             zeros.append(res_arr[j])
    if len(ones) >= len(zeros):
        res_arr = ones        
    else:
        res_arr = zeros
oxygen = res_arr[0].strip()

res_arr = lines

for i in range(len(lines[0])  -1):
    ones = []
    zeros = []
    for j in range(len(res_arr)):
        if res_arr[j][i] == '1':
            ones.append(res_arr[j])
        else:
             zeros.append(res_arr[j])

    if(len(res_arr) == 1):
        break
   
    if len(zeros) > len(ones):
        res_arr = ones        
    else:
        res_arr = zeros
cotwo = res_arr[0].strip()


print("gamma rate in decimal:" + str(int(oxygen,2)))
print("epsilon rate in dec:" + str(int(cotwo,2)))
print("multi:" + str(int(oxygen,2) * int(cotwo,2)))


# print("gamma rate in decimal:" + str(int(res,2)))
# flipped_eps = flip(res)
# print("epsilon rate in dec:" + str(int(flipped_eps,2)))
# print("multi:" + str(int(res,2) * int(flipped_eps,2)))




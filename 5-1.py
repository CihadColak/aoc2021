import numpy as np

f = open("5.txt", "r")
lines = f.readlines()
count = 0
#coords = np.arange(0,1000).reshape(100,100)
coords = np.zeros((1000,1000))
for line in lines:
    line_arr = line.split('->')
    start, finish = line_arr[0].strip().split(','), line_arr[1].strip().split(',')
    x1, y1 = int(start[0]), int(start[1])
    x2, y2 = int(finish[0]), int(finish[1])
    if x1 == x2:
        for i in range(min(y1,y2), max(y1,y2) + 1):
            coords[x1, i] = coords[x1, i] + 1
    elif y1 == y2:
       for i in range(min(x1,x2), max(x1,x2) + 1):
           coords[i, y1] = coords[i, y1] + 1
#print(coords)
coords = np.where(coords <2 , 0, coords)
coords = np.where(coords >1 , 1, coords)
suhm = np.sum(coords)
print(coords)
print(suhm)
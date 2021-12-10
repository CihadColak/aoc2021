import numpy as np

f = open("aoc2021/5.txt", "r")
lines = f.readlines()
count = 0
#coords = np.arange(0,1000).reshape(100,100)
coords = np.zeros((1000,1000), dtype=int)
for line in lines:
    line_arr = line.split('->')
    start, finish = line_arr[0].strip().split(','), line_arr[1].strip().split(',')
    x1, y1 = int(start[0]), int(start[1])
    x2, y2 = int(finish[0]), int(finish[1])
    #  diagonal
    if abs(x1-x2) == abs(y1-y2):
        # both going up or both going down
        if (x1 >= x2 and y1 >= y2) or (x2 >= x1 and y2 >= y1):
            print("XXXXXXX")
            for i in range(max(x1,x2) - min(x1,x2) +1):
                print(min(x1,x2) +i,min(y1,y2)+i)
                print(line)
                coords[min(x1,x2) +i,min(y1,y2)+i] += 1
        # only one going up also known as annoying diagonal
        else:
            for i in range(max(x1,x2) - min(x1,x2) +1):
                coords[min(x1,x2) +i,max(y1,y2)-i] += 1
        
    
    
        
            
    elif x1 == x2:
        for i in range(min(y1,y2), max(y1,y2) + 1):
            coords[x1, i] = coords[x1, i] + 1
    elif y1 == y2:
       for i in range(min(x1,x2), max(x1,x2) + 1):
           coords[i, y1] = coords[i, y1] + 1
    
print(coords)
coords = np.where(coords <2 , 0, coords)
coords = np.where(coords >1 , 1, coords)
suhm = np.sum(coords)
#print(coords)
print(suhm)
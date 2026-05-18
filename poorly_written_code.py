import os
import sys

def process(data):
    r = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
            if data[i] == data[j]:
                if data[i] not in r:
                    r.append(data[i])
    
    total = 0
    for x in r:
        total += x
        
    average = total / len(r)
    
    return average, r

print(process([1, 2, 3, 4, 5]))
print(process([1, 2, 2, 3, 4, 4, 5]))

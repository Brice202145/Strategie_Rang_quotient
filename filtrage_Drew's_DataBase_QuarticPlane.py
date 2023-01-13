import os
#import ast

result=[]
with open("t3.txt", "r") as shubaFile:
    lines=shubaFile.readlines()
for line in lines:
    try:
        result.append(line[line.index("[")+1:line.index("]")])
    except:
        pass
result
print('[%s]'%', '.join(map(str, listy)))
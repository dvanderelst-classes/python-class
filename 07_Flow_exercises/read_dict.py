dictionary = {}
f = open('minions.txt')
lines = f.readlines()
for x in lines:
    x = x.replace('\n','')
    entry = x.split(',')
    dictionary[entry[1]] = entry[0]













    
    
    





with open('short.txt') as f:
    lines = f.readlines()

url = []    

for i in lines:
    #print i[:-2]    
    url.append(i[:-2])

print url

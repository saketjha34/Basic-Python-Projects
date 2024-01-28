n = [
    [12,36],
    [3,9],
    [26,52],
    [13,26]

]
def rect(n):
    list = []
    count = 0
    for i in range(len(n)):
        for j in range(1,2):
            list.append(n[i][1]/n[i][0])
    
    return list    

#print(rect(n))

list1 = [3.0, 3.0, 2.0, 2.0]
emp = []

for i in range(len(list1)):
    if i in emp:
        break

print(emp)   
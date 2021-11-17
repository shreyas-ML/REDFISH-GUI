def checkpop(li,n,k):
    pop = li[5]
    lisum = {}
    #print(sum(li[3]))
    for i in range(0,n):
        lisum[i] = sum(li[i])
    
    sorteddict = sorted(lisum.items(), key=lambda kv: kv[1],reverse = True)
    for i,j in sorteddict.items():
        k = k - pop[i]

n = 5
k = 3 
#li = [[0,1,0,1,1,0,0,0,0][1,0,1,0,0,0,0,1,1]]
li = [[0,1,1,1,0],[1,0,0,1,1],[1,0,0,1,0],[1,1,1,0,0],[0,1,0,0,0],[1,1,1,1,1]]

#print(li[5][3])

checkpop(li,n,k)
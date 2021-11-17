'''
str1 = "Hello Shreyas"
d = {}
for i in str1:
    if i not in d:
        d[i] = 1

li = []
for k,v in d.items():
    if v == 1:
        li.append(k)

print(li)
'''
'''
n = 11
flag = 0 
for i in range (2,n//2):
    if n%i == 0:
        flag = 1
        break

if(flag == 1):
    print("Not prime number")
else:
    print("Prime number")
'''

import cProfile
import re

amount = {50:10,100:10,200:10,500:10}
li = [50,100,200,500]


def withdraw(amt):
    netamt = 0
    if amt % 50 != 0:
        print("Please enter in multiples of 50")
        return
    for k,v in amount.items():
        netamt = netamt + k*v

    if amt > netamt:
        print("amount exhausted")
        return
    else:
        notes = { }
        c = 3
        while amt != 0 and c >=0:
                
            denom = li[c]
            temp = countnotes(denom,amt)
            amt = amt-(temp*denom)
            amount[denom]= amount[denom] - temp
            notes[denom] = temp
            c = c-1
        
    print (notes)
    print(amount)

                 

def countnotes(val,amt):
    temp = amt // val
    #print(temp)
    if temp<=10 and temp <= amount[val]:
        return temp
    elif temp > amount[val]:
        return amount[val]      
    else:
        return temp

cProfile.run("10 + 10")
cProfile.run('withdraw(5000)')
#cProfile.run(withdraw(8000))




#withdraw(100)
#withdraw(450)

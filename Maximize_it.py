deets = []
temp1 = []
temp2 = []
main1 = []
main2 = []
sum1 = 0
deets = input().split()
mod= int(deets[1])

for i in range(int(deets[0])):
    temp1=input().split()
    main1.append(temp1)
    temp1 = []

for i in range(int(deets[0])):
    del main1[i][0]


#for i in range(int(deets[0])):
    #for j in range(len(deets[i])):
        #main1=int(main1[i][j])
main2 = [list(map(int, lst)) for lst in main1]
#main2 = [int(i) for j in main1 for i in j]

for r in range(len(main2)):
    main2[r].sort()

print(main2)
for v in range(len(main2)):
    temp2.append(main2[v][-1])

for z in range(len(temp2)):
    product = temp2[z]*temp2[z]
    sum1 = product + sum1
print(mod)
final_result = sum1%mod
print(final_result)
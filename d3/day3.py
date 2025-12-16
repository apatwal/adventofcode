ans = 0

input = open('d3/input.txt').read().strip()
lines = input.split('\n')

'''
better approach. find the largest battery from battery[0] to battery[i-1]. this would be lmax
find the largest battery from battery[i+1] to battery[n-1]. this would be
'''
for bank in lines:
    lmax = 0
    index = 0
    for i in range(0, len(bank)-1):
        if int(bank[i]) > lmax:
            index = i
            lmax = int(bank[i])
    
    rmax = 0
    for j in range(index+1, len(bank)):
        if int(bank[j]) > rmax:
            rmax = int(bank[j])

    battery = str(lmax) + str(rmax)
    ans += int(battery)
    

print(ans)

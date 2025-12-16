ans = 0

input = open('d3/input.txt').read().strip()
lines = input.split('\n')
for bank in lines:
    batteries = int(bank) # int representation of the battery bank
    l, r = 0, len(bank) - 1
    lmax, rmax = 0, 0
    while l < r:
        if int(bank[l]) > int(bank[r]):
            rmax = max(rmax, int(bank[r]))
            lmax = max(lmax, int(bank[l]))
            r-=1
        elif int(bank[l]) <= int(bank[r]):
            lmax = max(lmax, int(bank[l]))
            rmax = max(rmax, int(bank[r]))
            l+=1

    if rmax > lmax and r+1 in range(len(bank)):
        # set lmax to rmax and then find largest right
        lmax = rmax
        rmax = 0
        for i in range(r+1, len(bank)):
            rmax = max(rmax, int(bank[i]))
    maxbat = str(lmax) + str(rmax)
    ans += int(maxbat)

print(ans)

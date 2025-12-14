'''
Day 1 advent of code

dial starts at 50

L goes toward lower numbers -> CCW
R goes toward higher numbers -> CW

0,1,2... 50.... 98,99,0,1

          99 0 1
        75      25
            50

            
count exactly how many times the dial points at 0

'''

input = open('d1/input.txt').read().strip()

dial = 50
count = 0
iter = -1

for command in input.split():
    iter+=1
    direction = command[0]
    steps = int(command[1:])

    if steps > 100: # mod 100 to reduce unnecessary full rotations
        steps = steps % 100

    if direction == 'L':
        '''
        subtract and check if we hit negative numbers,
        if we do then subtract the abs val from 100
        '''
        if dial - steps < 0:
            x = abs(dial - steps)
            dial = 100 - x
        else:
            dial -= steps

    elif direction == 'R':
        '''
        add and check if we go over 99,
        if we do then subtract 100 from the new value
        '''
        if dial + steps > 99:
            dial = (dial + steps) - 100
        else:
            dial += steps
    

    if dial == 0:
        count += 1

print(count)

''' PART 2'''
dial = 50
count = 0

for command in input.split():
    direction = command[0]
    steps = int(command[1:])

    dir = 1 if direction == 'R' else -1
    for i in range(steps):
            dial += dir
            if dial < 0 or dial > 99:
                dial = 99 if dial < 0 else 0
            if dial == 0:
                count += 1
        
print(count)
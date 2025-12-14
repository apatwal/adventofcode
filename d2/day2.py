answer = 0

input = open('d2/input.txt').read().strip()

def isValid(num):   # inputed as a string
    if len(num) %2 != 0:
        return False
    half = len(num)//2
    return num[:half] == num[half:]


for id in input.split(','):
    l, r = map(int, id.split('-'))
    for i in range(l, r+1):
        if(isValid(str(i))):
            answer += i


print(answer)
# Test
# print(isValid("123123"))  # True
# print(isValid("55"))  # True
# print(isValid("101"))  # False
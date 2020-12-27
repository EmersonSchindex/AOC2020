file = open("day6_input.txt", "r")

teststring = "abcdefghijklmnopqrstuvwxyz"
res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nolines = 0
count = 0

while True:
    line = file.readline()

    if line.strip():
        nolines = nolines + 1
        for i in line.strip():
            res[teststring.find(i.lower())] = res[teststring.find(i.lower())] + 1

    if not line.strip():
        for x in range(26):
            if res[x] == nolines:
                count += 1
        print(count, nolines, res)
        res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        nolines = 0

    if not line:
        break

print(count)

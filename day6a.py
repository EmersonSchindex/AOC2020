from collections import counter

file = open("day6_input_test.txt", "r")

count = 0
countevery = 0
lines = 0
totalcount = 0
temp = []
tempevery = []

while True:
    line = file.readline()

    if line.strip():
        lines += 1
        for i in line.strip():
            temp.append(i)

    if not line.strip():
        for i in temp:
            if(i not in tempevery):
                countevery += 1
                tempevery.append(i)

        print(lines, countevery, temp, tempevery)
        totalcount = totalcount + count
        lines = 0
        count = 0
        countevery = 0
        temp = []
        tempevery = []

    if not line:
        break

print(totalcount)

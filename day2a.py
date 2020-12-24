import re

file1 = open("day2_input.txt", "r")
count = 0
f = open("filetest2.txt", "w")
while True:
  line = file1.readline()
  if not line:
    break
  
  temp = re.findall(r'\d+', line)
  res = list(map(int, temp))
  low = res[0]
  high = res[1]
  result = line.find(":")
  testchar = line[result - 1]
  counter = line.count(testchar) - 1
  result1 = line.find(str(counter))
  if counter >= low and counter <= high:
    count += 1
  
  print(line.rstrip(), res, low, high, testchar, counter, result1, count, file=f)
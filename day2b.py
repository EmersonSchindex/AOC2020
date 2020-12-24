import re

file1 = open("day2_input.txt", "r")
count = 0

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
  
  splitat = result + 2
  r = line[splitat:]
  lowchar = r[low - 1]
  highchar = r[high - 1]
    
  if (lowchar == testchar and highchar != testchar) or (lowchar != testchar and highchar == testchar):
    count += 1
  
  #print(r.rstrip(), res, low, high, lowchar, highchar, count, file=f)
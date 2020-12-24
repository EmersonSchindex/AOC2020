file = open("day3_input_new.txt", "r")
count = 0
position = 1
linenumber = 0

next(file)
while True:
  line = file.readline()
  linenumber = linenumber + 1
  if not line:
    break
  
  if (linenumber % 2) == 0:
    testchar = line[position]
    if testchar == "#":
      count = count + 1
  
    position = position + 1
    linenumber = 0

  print(linenumber, count)
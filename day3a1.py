file = open("day3_input.txt", "r")
count = 0
filenew = open("day3_input_new.txt", "w")
while True:
  line = file.readline()
  if not line:
    break
  
  newline = line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip()  + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip() + line.rstrip()

  print(newline, file=filenew)

import math

file = open("day5_input.txt", "r")
# filenew = open("day5_input_new.txt", "w")

totalrows = 128
totalseats = 8

minro = 0
maxro = 127
minseat = 0
maxseat = 7
seatid = 0
finalseat = 0
seatlist = []

def f_lower(min, max):
  
  global maxro
  global minro

  maxro = math.floor((max + min) / 2)
  minro = min

#  print("in function lower" , minro, maxro)

def r_lower(min, max):
  
  global maxseat
  global minseat

  maxseat = math.floor((max + min) / 2)
  minseat = min

#  print("in function lower" , minseat, maxseat)  

def f_upper(min, max):
  
  global maxro
  global minro

  maxro = max
  minro = math.ceil((max + min) / 2)

#  print("in function upper" , minro, maxro)

def r_upper(min, max):
  
  global maxseat
  global minseat

  maxseat = max
  minseat = math.ceil((max + min) / 2)

#  print("in function upper seat" , minseat, maxseat)  

while True:
  line = file.readline()
  
  if line.strip():
    minro = 0
    maxro = 127
    minseat = 0
    maxseat = 7
    
#    print(seatid, file = filenew)
    for i in line:
      if i == 'F':
#        print("in call to function lower row", minro, maxro)
        f_lower(minro, maxro)

      if i == 'B':
#        print("in call to function upper row", minro, maxro)
        f_upper(minro, maxro)

      if i == 'L':
#        print("in call to function lower seat", minseat, maxseat)
        r_lower(minseat, maxseat)

      if i == 'R':
#        print("in call to function upper seat", minseat, maxseat)
        r_upper(minseat, maxseat)             
    
    seatid = (minro * 8) + minseat

    seatlist.append(seatid)

    if seatid > finalseat:
      finalseat = seatid

  if not line.strip():
    seatlist.sort()
    teller = 0
    for seat in seatlist:
      if seatlist[teller + 1] - seatlist[teller] == 2:
        finalseat = seatlist[teller + 1] - 1
      if teller == len(seatlist) - 2:
        break
      teller = teller + 1
    
  if not line:
    break
  
print(finalseat)
file = open("day4_input.txt", "r")
filenew = open("day4_input_new.txt", "w")

count = 0
linenumber = 0
byr = -9
iyr = -9
eyr = -9
hgt = -9
ecl = -9
pid = -9
cid = -9
hcl = -9

while True:
  line = file.readline()
  
  if line.strip():
    byrt = line.find('byr:')
    iyrt = line.find('iyr:')
    eyrt = line.find('eyr:')
    hgtt = line.find('hgt:')
    eclt = line.find('ecl:')
    pidt = line.find('pid:')
    cidt = line.find('cid:')
    hclt = line.find('hcl:')
    print(line.rstrip(), file=filenew)
    if byrt >= 0:
      byr = 0
    if iyrt >= 0:
      iyr = 0
    if eyrt >= 0:
      eyr = 0
    if hgtt >= 0:
      hgt = 0
    if eclt >= 0:
      ecl = 0
    if pidt >= 0:
      pid = 0
    if cidt >= 0:
      cid = 0
    if hclt >= 0:
      hcl = 0

  if not line.strip():
    print("validate", byr, iyr, eyr, hgt, ecl, pid, hcl, cid, file=filenew)    
    if byr == 0 and iyr ==0 and eyr == 0 and hgt == 0 and ecl == 0 and pid == 0 and hcl == 0:
      count = count + 1

    byr = -9
    iyr = -9
    eyr = -9
    hgt = -9
    ecl = -9
    pid = -9
    cid = -9
    hcl = -9
    print(count, file=filenew)

  if not line:
    break
  
print(count)
file = open("day4_input.txt", "r")
filenew = open("day4_input_new.txt", "w")

eyecolor_list = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
haircolor_list = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
pid_list = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

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
byear = '0'
iyear = '0'
eyear = '0'
hgtincm = 0
hgtinin = 0

print("validate", 'pid', 'pidt', 'passportid', file=filenew)  

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
#    print(line.rstrip(), file=filenew)
    if byrt >= 0:
      byear = line[byrt + 4 : byrt + 8]
      if byear.isdigit():
        if int(byear) >= 1920 and int(byear) <= 2002:
          byr = 0
    if iyrt >= 0:
      iyear = line[iyrt + 4 : iyrt + 8]
      if iyear.isdigit():
        if int(iyear) >= 2010 and int(iyear) <= 2020:
          iyr = 0
    if eyrt >= 0:
      eyear = line[eyrt + 4 : eyrt + 8]
      if eyear.isdigit():
        if int(eyear) >= 2020 and int(eyear) <= 2030:
          eyr = 0
    if hgtt >= 0:
      hgttcm = line.find('cm')
      hgttin = line.find('in')
      if hgttcm > 0:
        hgtincm = line[hgtt + 4 : hgttcm]
        if hgtincm.isdigit():
          if int(hgtincm) >= 150 and int(hgtincm) <= 193:
            hgt = 0
      if hgttin > 0:
        hgtinin = line[hgtt + 4 : hgttin]
        if hgtinin.isdigit():
          if int(hgtinin) >= 59 and int(hgtinin) <= 76:
            hgt = 0
    if eclt >= 0:
      eyecolor = line[eclt + 4 : eclt + 7]
      if eyecolor in eyecolor_list:
        ecl = 0
    if pidt >= 0:
      passportid = line[pidt + 4 : pidt + 14]
      if len(passportid.rstrip()) == 9 and pid_list.issuperset(passportid.rstrip()):
        pid = 0
    if cidt >= 0:
      cid = 0
    if hclt >= 0:
      haircolor = line[hclt + 4 : hclt + 11]
      if len(haircolor) == 7 and haircolor[0] == '#' and haircolor_list.issuperset(haircolor[1:len(haircolor)-1]):
        hcl = 0

  if not line.strip():
    print("validate", pid, pidt, passportid, file=filenew)   
#    print("validate", byr, iyr, eyr, hgt, ecl, pid, hcl, cid, file=filenew)  
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
    byear = '0'
    iyear = '0'
    eyear = '0'
    hgtincm = 0
    hgtinin = 0
#    print(count, file=filenew)

  if not line:
    break
  
print(count)
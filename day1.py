import xlrd

loc = "day1_input.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

j = 1

for i in range(sheet.nrows):
  x = sheet.cell_value(i, 0)

  for k in range(j, sheet.nrows):
    y = sheet.cell_value(k, 0)
    
    if x + y == 2020:
      print(i, x, y, x * y)
      break
  
  j = j + 1  
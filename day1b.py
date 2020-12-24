import xlrd

loc = "day1_input.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

for i in range(sheet.nrows):
  x = sheet.cell_value(i, 0)
  j = 1
  l = 2

  for k in range(j, sheet.nrows):
    y = sheet.cell_value(k, 0)
  
    for m in range(l, sheet.nrows):
      z = sheet.cell_value(m, 0)
      if x + y + z == 2020:
        print(x + y + z, x * y * z)
        break

    l = l + 1
  j = j + 1
 
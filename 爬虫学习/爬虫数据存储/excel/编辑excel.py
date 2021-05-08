# -*- coding: UTF-8 -*-
import xlrd
import xlwt

rwb = xlrd.open_workbook("成绩表.xlsx")
rsheet = rwb.sheet_by_index(0)
nrows = rsheet.nrows
ncols = rsheet.ncols
print(ncols)
rsheet.put_cell(0, 4, xlrd.XL_CELL_TEXT, "总分", None)
for row in range(1, rsheet.nrows):
    rsheet.put_cell(
        row, 4, xlrd.XL_CELL_NUMBER, sum(rsheet.row_values(row, 1, ncols)), None
    )

ncols = rsheet.ncols
rsheet.put_cell(19, 0, xlrd.XL_CELL_TEXT, "平均分", None)
for col in range(1, ncols - 1):
    rsheet.put_cell(
        19, col, xlrd.XL_CELL_NUMBER, sum(rsheet.col_values(col, 1, nrows))/18, None
    )

wwb = xlwt.Workbook()

wwsheet = wwb.add_sheet("sheet1")
nrows = rsheet.nrows
ncols = rsheet.ncols

for nrow in range(nrows):
    for ncol in range(ncols):

        wwsheet.write(nrow, ncol, rsheet.cell_value(nrow, ncol))
wwb.save("成绩表2.xls")

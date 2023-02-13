from openpyxl import *
wb = load_workbook(r'F:\Prog\Py\b1.xlsx')
sheet_ranges = wb['123']
for row in sheet_ranges.iter_rows(min_col=1, max_col=6):
    for cell in row:
        print(cell.value)
    print()
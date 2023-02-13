from openpyxl import *
wb = load_workbook(r'...')
sheet_ranges = wb['...']
for row in sheet_ranges.iter_rows(min_col=., max_col=.):
    for cell in row:
        print(cell.value)
    print()
